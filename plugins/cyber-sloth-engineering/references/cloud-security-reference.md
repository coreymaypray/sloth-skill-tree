# Cloud Security Reference Library

> Source: [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) (Apache 2.0)
> Curated for `cyber-sloth-engineering:cloud-security-engineer`

---

## Quick Lookup

### By Cloud Provider

| Provider | IAM Audit | Storage Audit | Network Audit | Key Tools |
|----------|-----------|--------------|---------------|-----------|
| AWS | `aws iam`, Access Analyzer, Prowler | `aws s3api`, S3 Block Public Access | Security Groups, VPC Flow Logs | Pacu, ScoutSuite, Prowler |
| Azure | Microsoft Graph, `az ad`, ScoutSuite | Blob container ACLs, SAS tokens | NSGs, Azure Firewall | AzureADRecon, ScoutSuite |
| GCP | `gcloud asset`, IAM Recommender, Policy Analyzer | Bucket IAM, ACLs | VPC Firewall Rules | ScoutSuite, Forseti |
| Kubernetes | `kubectl`, rbac-tool, KubiScan | etcd encryption, Secret management | NetworkPolicy, Calico | Kubeaudit, Trivy |

### By Service Type

| Service Type | Security Concerns | Key Checks |
|-------------|-------------------|------------|
| IAM/Identity | Over-privileged roles, stale accounts, missing MFA | Credential reports, role bindings, access analyzer |
| Object Storage | Public access, missing encryption, overly broad policies | ACLs, bucket policies, Block Public Access, versioning |
| Compute | Metadata service exposure, unpatched instances, user data secrets | IMDSv2 enforcement, security groups, startup scripts |
| Serverless | Hardcoded credentials, excessive function permissions, injection | Function code review, execution role scoping |
| Containers | Image vulnerabilities, RBAC misconfig, privileged pods | Trivy scanning, RBAC audit, pod security standards |
| Databases | Public endpoints, default credentials, unencrypted storage | Network ACLs, encryption at rest, access logging |

---

## Detailed References

### AWS IAM Security

**Inventory and credential report:**
```bash
aws iam generate-credential-report
aws iam get-credential-report --query 'Content' --output text | base64 -d > iam-report.csv

# Find users with access keys older than 90 days
aws iam list-users --query 'Users[*].UserName' --output text | while read user; do
  aws iam list-access-keys --user-name "$user" \
    --query "AccessKeyMetadata[?CreateDate<='$(date -d '-90 days' +%Y-%m-%d)']" \
    --output table
done
```

**Access Analyzer for least-privilege policy generation:**
```bash
aws accessanalyzer create-analyzer --analyzer-name account-analyzer --type ACCOUNT

# Generate scoped policy from 90 days of CloudTrail activity
aws accessanalyzer start-policy-generation --policy-generation-details '{
  "principalArn": "arn:aws:iam::123456789012:role/AppRole",
  "cloudTrailDetails": {
    "trailArn": "arn:aws:cloudtrail:us-east-1:123456789012:trail/mgmt-trail",
    "startTime": "2025-01-01T00:00:00Z",
    "endTime": "2025-03-01T00:00:00Z"
  }
}'
```

**Permission boundaries (prevent privilege escalation):**
```bash
aws iam create-policy --policy-name DevBoundary --policy-document file://boundary.json
aws iam put-role-permissions-boundary --role-name DevRole \
  --permissions-boundary "arn:aws:iam::123456789012:policy/DevBoundary"
```

**MFA enforcement via SCP:**
```bash
aws organizations create-policy --name RequireMFA --type SERVICE_CONTROL_POLICY \
  --content '{"Version":"2012-10-17","Statement":[{
    "Sid":"DenyAllExceptMFA","Effect":"Deny",
    "NotAction":["iam:CreateVirtualMFADevice","iam:EnableMFADevice","sts:GetSessionToken"],
    "Resource":"*",
    "Condition":{"BoolIfExists":{"aws:MultiFactorAuthPresent":"false"}}
  }]}'
```

### AWS S3 Bucket Auditing

```bash
# Check account-level Block Public Access
aws s3control get-public-access-block \
  --account-id $(aws sts get-caller-identity --query Account --output text)

# Per-bucket audit loop
for bucket in $(aws s3api list-buckets --query 'Buckets[*].Name' --output text); do
  echo "=== $bucket ==="
  # Check Block Public Access
  aws s3api get-public-access-block --bucket "$bucket" 2>/dev/null \
    || echo "  No Block Public Access configured"
  # Check for public ACL grants
  aws s3api get-bucket-acl --bucket "$bucket" \
    --query 'Grants[?Grantee.URI==`http://acs.amazonaws.com/groups/global/AllUsers`]'
  # Check encryption
  aws s3api get-bucket-encryption --bucket "$bucket" 2>/dev/null \
    || echo "  Encryption: DISABLED"
  # Check versioning
  aws s3api get-bucket-versioning --bucket "$bucket" --query 'Status'
done

# Remediation: Lock down a bucket
aws s3api put-public-access-block --bucket TARGET \
  --public-access-block-configuration \
  'BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true'
```

**Prowler S3 checks:**
```bash
prowler aws --checks s3_bucket_public_access s3_bucket_default_encryption \
  s3_bucket_policy_public_write_access s3_bucket_versioning_enabled \
  -M json-ocsf -o ./prowler-s3-audit/
```

### Azure / Entra ID Auditing

**Tenant configuration:**
```powershell
Connect-MgGraph -Scopes "Directory.Read.All","Policy.Read.All","AuditLog.Read.All"
Get-MgPolicyIdentitySecurityDefaultEnforcementPolicy | Select-Object IsEnabled
Get-MgIdentityConditionalAccessPolicy | Select-Object DisplayName, State
```

**Privileged role and account audit:**
```bash
# List role assignments
az rest --method GET \
  --url "https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments?\$expand=principal" \
  --query "value[*].{Role:roleDefinitionId,Principal:principal.displayName}" -o table

# Guest users, stale accounts, MFA gaps
az ad user list --filter "userType eq 'Guest'" -o table
az rest --method GET \
  --url "https://graph.microsoft.com/v1.0/reports/authenticationMethods/userRegistrationDetails" \
  --query "value[?!isMfaRegistered].{UPN:userPrincipalName}" -o table
```

### GCP IAM Auditing

**Organization-wide IAM enumeration:**
```bash
# Find all primitive role bindings (Owner/Editor -- should be minimized)
gcloud asset search-all-iam-policies --scope=organizations/ORG_ID \
  --query="policy:roles/owner OR policy:roles/editor" \
  --format="table(resource, policy.bindings.role, policy.bindings.members)"

# Find public access bindings
gcloud asset search-all-iam-policies --scope=organizations/ORG_ID \
  --query="policy:allUsers OR policy:allAuthenticatedUsers" \
  --format="table(resource, policy.bindings.role)"
```

**Service accounts, Recommender, and Policy Analyzer:**
```bash
# Audit service account keys (minimize user-managed keys)
for sa in $(gcloud iam service-accounts list --project=PROJECT_ID --format="value(email)"); do
  gcloud iam service-accounts keys list --iam-account="$sa" --managed-by=user
done

# ML-based least-privilege suggestions
gcloud recommender recommendations list --project=PROJECT_ID \
  --recommender=google.iam.policy.Recommender --location=global

# Who can access a specific resource?
gcloud asset analyze-iam-policy --organization=ORG_ID \
  --full-resource-name="//storage.googleapis.com/projects/_/buckets/sensitive-data"

# What can a specific user access?
gcloud asset analyze-iam-policy --organization=ORG_ID \
  --identity="user:developer@company.com"
```

### Kubernetes RBAC Auditing

**Key RBAC queries:**
```bash
# rbac-tool who-can queries (critical checks)
kubectl rbac-tool who-can get secrets          # Secret access
kubectl rbac-tool who-can create pods/exec     # Container exec
kubectl rbac-tool who-can bind clusterroles    # Privilege escalation
kubectl rbac-tool who-can create pods          # Pod creation (escape risk)
kubectl rbac-tool analysis                     # Full RBAC report
```

**KubiScan risky permissions scan:**
```bash
python3 -m kubiscan -rcr     # Risky ClusterRoles
python3 -m kubiscan -rs       # Risky service accounts
python3 -m kubiscan -pe       # Privilege escalation vectors
python3 -m kubiscan -a        # All checks
```

### Container Image Scanning with Trivy

```bash
# Basic vulnerability scan
trivy image --severity CRITICAL,HIGH nginx:latest

# All scanners (vuln + misconfig + secret + license)
trivy image --scanners vuln,misconfig,secret,license myapp:latest

# Generate SBOM
trivy image --format cyclonedx --output sbom.cdx.json myapp:latest

# Scan Kubernetes manifests and Dockerfiles
trivy config Dockerfile
trivy config k8s-deployment.yaml
trivy config ./terraform/

# CI/CD gate (exit code 1 if CRITICAL found)
trivy image --exit-code 1 --severity CRITICAL myapp:latest
```

---

## Tool Guidance

| Tool | Provider | Purpose |
|------|----------|---------|
| **AWS CLI** | AWS | IAM queries, S3 auditing, Security Group analysis |
| **Prowler** | AWS/Azure | 300+ CIS/PCI/HIPAA checks, S3 and IAM auditing |
| **IAM Access Analyzer** | AWS | External access detection, least-privilege policy generation |
| **ScoutSuite** | Multi-cloud | Automated posture assessment with risk-scored HTML reports |
| **Pacu** | AWS | AWS exploitation framework (IAM enum, privesc, data exfil) |
| **CloudFox** | AWS | Exploitable attack path identification |
| **Microsoft Graph** | Azure | Entra ID config, roles, conditional access, audit logs |
| **gcloud CLI** | GCP | IAM policies, service accounts, asset inventory |
| **IAM Recommender** | GCP | ML-based permission reduction recommendations |
| **Policy Analyzer** | GCP | Effective access analysis across org hierarchy |
| **Trivy** | Containers | Image CVE scanning, SBOM generation, misconfig detection |
| **kubectl** | Kubernetes | RBAC queries, resource inspection |
| **rbac-tool** | Kubernetes | Who-can queries, RBAC visualization |
| **KubiScan** | Kubernetes | Risky RBAC permissions and privesc path detection |
| **Kubeaudit** | Kubernetes | Pod security and RBAC anti-pattern detection |
| **Steampipe** | Multi-cloud | SQL-based queries across cloud provider APIs |

### Cloud Pentest Methodology (from repo)

1. **Reconnaissance**: `aws sts get-caller-identity`, enumerate users/roles/buckets/functions
2. **IAM Exploitation**: Check for `iam:CreatePolicyVersion`, `iam:PassRole` + `lambda:CreateFunction`, `sts:AssumeRole` cross-account trust
3. **Storage Exposure**: Public bucket access (`--no-sign-request`), versioning for deleted data, secrets in objects
4. **Compute Exploitation**: IMDS credential theft (`169.254.169.254`), Lambda code review, user data scripts
5. **Network Assessment**: Security groups allowing `0.0.0.0/0`, VPC peering, cross-account access

### IAM Policy Best Practices

| Practice | AWS | Azure | GCP |
|----------|-----|-------|-----|
| Least privilege | Access Analyzer + CloudTrail | Conditional Access + PIM | IAM Recommender + Policy Analyzer |
| No long-lived keys | IAM roles + STS AssumeRole | Managed Identities | Workload Identity Federation |
| MFA enforcement | SCP DenyAllExceptMFA | Conditional Access policies | Context-Aware Access |
| Privileged access | Permission boundaries | PIM time-bound activation | IAM Conditions + org policies |
| Monitoring | CloudTrail + EventBridge | Sign-in logs + Defender | Cloud Audit Logs + SCC |
| Compliance | Config Rules + Security Hub | Defender for Cloud | Security Command Center |
