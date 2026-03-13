# ATS Optimization — Complete Reference

## How ATS Systems Work

Every resume submission passes through three stages before human eyes see it:

1. **File Ingestion** — System accepts upload, converts to processable text
2. **Parsing & Data Extraction** — Scans for name, contact info, job titles, dates, education, skills; extracts into structured fields
3. **Keyword Matching & Ranking** — Compares extracted data against job requirements; ranks candidates

**Scale of the problem:**
- 97.8% of Fortune 500 companies use ATS
- 75% of resumes are filtered out before a human reads them
- Three ATS generations coexist: keyword matching (most common), semantic/NLP (synonyms), AI/LLM parsing (cutting edge)
- **Optimize for keyword matching first** — it's still the dominant method

---

## Langstaff's 9 ATS Rules

1. **Use simple, standard section headers** the system recognizes:
   - ✓ "Professional Summary," "Work Experience," "Education," "Skills"
   - ✗ "My Journey," "What I Bring," "Career Story"

2. **No images, graphics, logos, or icons** — ATS cannot read them and they break parsing

3. **No text boxes or tables** — content inside is often skipped entirely

4. **Standard bullet points only** (• or –) — fancy symbols may become garbled characters

5. **Include keywords from the job posting** — use both full terms AND acronyms:
   - "Search Engine Optimization (SEO)" — not just one or the other

6. **Consistent date format with months** — MM/YYYY or Month YYYY throughout
   - iCIMS requires MM/YYYY format specifically

7. **Submit as DOCX (safest) or text-based PDF**
   - Never: image-based PDF, .pages, .odt, Google Docs export without checking

8. **Single-column layout only**
   - The ONLY format safe across ALL ATS platforms
   - Two-column resumes fail in 39%+ of Workday implementations

9. **The Notepad Test** — paste resume into Windows Notepad
   - If text is clean and in correct order → ATS can read it
   - If words are scrambled or missing → reformat the template

---

## ATS Platform Reference Guide

| Platform | Market Share | Strictness | Key Rules |
|----------|-------------|------------|-----------|
| **Workday** | 39%+ Fortune 500 | Strict | No multi-column. 43% of formatting rejections from tables/columns. Simplest formatting. |
| **Taleo / Oracle** | Large enterprise | Strictest | Cannot process multi-column at all. Struggles with PDFs. Requires absolute simplicity. |
| **iCIMS** | Global leader 10.7% | Moderate | Strict on date formats (MM/YYYY required). Handles clean formatting well. |
| **Greenhouse** | 19.3% broader market | Lenient | Handles 2-column reasonably. Shows resumes largely as submitted. |
| **Lever** | Mid-market | Lenient | Similar to Greenhouse. 2-column tolerance. |
| **SAP SuccessFactors** | Large enterprise | Strict | Similar to Workday. Simple formatting recommended. |

> **Rule of thumb:** Format for the STRICTEST system (Taleo/Workday). You almost never know which ATS a company uses.

---

## Keyword Strategy

**Target: 75–80% match rate** with the job description (per Jobscan data).
- Below 60%: very likely filtered
- 75–80%: optimal — feels natural, clears most filters
- Above 90%: may trigger keyword stuffing detection in modern AI parsers

**Keyword placement priority (highest to lowest impact):**
1. Professional summary — first place scanners look
2. Bullet points — embed keywords in context with achievements
3. Skills section — dedicated keyword delivery vehicle
4. Job title / role descriptions — exact match to target titles
5. Education and certifications — spell out full credential names

**Both full terms AND acronyms in the same document:**
```
"Certified Information Systems Security Professional (CISSP)"
"Search Engine Optimization (SEO)"
"Key Performance Indicators (KPIs)"
```

**Keyword mining process:**
1. Copy job description into a Google Doc
2. Highlight every skill, tool, technology, credential, and behavior mentioned
3. Count frequency — terms mentioned 3+ times are high priority
4. Cross-reference against your current resume
5. Add missing high-priority terms to summary, bullets, and skills section

---

## ATS Optimization Tools

| Tool | Best For | Cost |
|------|----------|------|
| **Jobscan** | Industry standard. Upload resume + JD for detailed match report simulating different ATS engines. Users report 3x interview increases at 75–80% match. | Free tier + paid |
| **Resume Worded** | Content quality + ATS. Scores writing impact line-by-line. Suggests bullet transformations. | Paid |
| **SkillSyncer** | Budget option. Chrome extension for quick JD scanning. Good for high-volume applications. | ~$14.95/mo |
| **ResyMatch.io** (Belcak) | Quick free ATS compatibility check. | Free |

---

## File Naming Convention

Always name your file:
```
FirstName_LastName_Resume.docx
```

Never: "resume.docx", "My Resume Final v3.docx", "resume2024.pdf"

---

## Format Safety Quick Check

Before submitting any resume, verify:

- [ ] Single-column layout only
- [ ] No tables used (exception: simple skills grid with no critical content)
- [ ] No images, icons, or graphics of any kind
- [ ] No text boxes
- [ ] Standard section headings used
- [ ] Dates include months and are formatted consistently
- [ ] File is DOCX or text-based PDF
- [ ] File is named FirstName_LastName_Resume
- [ ] Passed the Notepad Test
- [ ] 75–80% keyword match to target JD (verified with Jobscan or similar)
- [ ] Both full terms AND acronyms included for key credentials/skills
