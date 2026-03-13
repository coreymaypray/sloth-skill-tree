# The Complete ChatGPT / AI Prompt System — Langstaff's 24 Prompts

## The Golden Rule Before Any Prompt

**Always start a new session with Prompt 1.** Load the job descriptions first — every subsequent prompt builds on that context. Without it, the AI has no grounding in what the employer actually needs.

---

## Core Resume Prompts (1–7)

### Prompt 1 — Turn AI Into a Hiring Manager (Start EVERY Session Here)
> "I am going to be sharing information about the job I am applying for and about my own experience. I want you to act as a hiring manager and help me craft a strong and effective resume. I'm going to share with me two or three job postings that are representative of the types of jobs I'm applying for. Is that okay?"

Then paste 2–3 representative job descriptions. This loads the hiring context so every subsequent response is calibrated to what employers in this role actually need.

---

### Prompt 2 — Build the Key Skills / Areas of Expertise Section
> "Based on the jobs I provided you, can you please provide a list of the 25 most important skills required to do these jobs well. Please make each skill 1–3 words long and focus more on hard skills over soft skills."

**Use:** After Prompt 1. Pick 10–16 from the 25 for your Areas of Expertise section. Also keeps the remaining 9–15 as a keyword bank for bullets.

---

### Prompt 3 — Write the Professional Summary
> "Based on the requirements for the job and the information below regarding my values, skills, and career highlights, can you please write me a short concise professional summary that is 3 sentences long to add to my resume? Please make the tone direct, professional, and do not write in first person."

Then paste 3–5 bullet points about your background, key skills, and values.

**Use:** After Prompt 1. Review the output against the 4-sentence formula in `references/01-resume-architecture.md` and adjust.

---

### Prompt 4 — Write the Job Overview for Each Role
> "Can you please provide me with a one sentence overview for my resume that provides context about this job? Structure: 'Hired by the [blank] company to take on responsibilities including [blank]'"

Then describe the company type and your core responsibilities.

**Use:** For each job in your experience section. Creates the 2–3 line context paragraph that goes above the bullet points.

---

### Prompt 5 — Write Individual Bullet Points
> "Based on the job description, can you help me write an effective bullet point for my resume? I want to focus on my accomplishments and highlight skills that are relevant to the job I am applying for. Here is the task/accomplishment I would like to write about: [description of what you did]"

**Rules:**
- One bullet at a time — don't dump all accomplishments at once
- Include as much specific detail as you can: numbers, tools, context, team size, results
- Review and rewrite in your voice before using

---

### Prompt 6 — Generate More Bullet Point Ideas
> "Can you look at the bullets I have already written (below) and the job description and suggest 3–5 additional skill areas or accomplishments I may want to highlight that aren't currently represented?"

Then paste your existing bullets.

**Use:** After you've written your initial set — surfaces gaps you may have missed.

---

### Prompt 7 — Rewrite Existing Bullets
> "Can you rewrite the following bullet point to be more exciting and professional with a stronger focus on accomplishments? [paste bullet]"

**Use:** For any bullet that feels flat, duties-focused, or vague.

---

## Rewrite Command Prompts (8–19)

These refine AI-generated content. Apply after any generation prompt.

| # | Command | When to Use |
|---|---------|-------------|
| 8 | "Can you make this shorter and more concise?" | Bullet or summary running too long |
| 9 | "Can you make this more direct and professional?" | Output sounds casual or hedging |
| 10 | "Can you remove unnecessary adjectives and filler words?" | Output feels padded or AI-ish |
| 11 | "Can you put the accomplishment or result first?" | Bullet buries the lead |
| 12 | "Can you remove first person and third person language?" | Output uses "I" or "she/he" |
| 13 | "Can you make this more exciting while keeping it professional?" | Output is technically correct but bland |
| 14 | "Can you replace any uncommon or overly complex language with simpler alternatives?" | Output sounds stilted or uses jargon |
| 15 | "Can you try a completely different approach to writing this?" | Output misses the mark entirely |
| 16 | "Can you integrate some of these key skills naturally into the bullet? [paste skills]" | Bullet needs keyword reinforcement |
| 17 | "Can you make this sound more like these example bullets? [paste 2–3 strong bullets]" | Calibrating tone and style |
| 18 | "Can you make this sound more like an executive-level accomplishment?" | Elevating language for Director+ roles |
| 19 | "Can you rewrite this without including [specific false claim]?" | Removing anything you can't stand behind |

---

## Job Search Bonus Prompts (20–24)

### Prompt 20 — Write the Cover Letter
> "Based on the job description and the resume information I've provided, can you please write a cover letter for this position? Use a bullet point structure for the body of the letter with 4–5 bullets that highlight my most relevant experience for this role. Keep the tone professional but warm."

Then paste the JD and your resume (or key accomplishments).

**Review against:** The Badass Cover Letter framework in `references/04-cover-letters.md`

---

### Prompt 21 — Write an Intro Message to the Hiring Manager
> "Can you write a brief LinkedIn message (under 100 words) introducing myself to the hiring manager for a [Job Title] role at [Company]? I want to express genuine interest, reference one specific thing about the company or role, and invite a conversation. Keep it natural, not salesy."

**Use:** Before or after applying — direct outreach dramatically increases visibility.

---

### Prompt 22 — Predict Interview Questions
> "Based on this job description, what are the 15 most likely behavioral interview questions I will be asked? Please organize them by theme (leadership, problem-solving, communication, etc.)."

Then paste the job description.

**Use:** As the starting point for Phase 2 of the interview prep system in `references/06-interview-prep.md`

---

### Prompt 23 — Write an Informational Interview Request
> "Can you write a LinkedIn message requesting a 15-minute informational interview with someone who works at [Company] in [Department]? I want to learn more about the culture and what it's like to work there. Keep it under 75 words and make it easy to say yes."

**Use:** For networking and intelligence-gathering before applying or interviewing.

---

### Prompt 24 — Write a Post-Interview Thank You Email
> "Can you write a post-interview thank you email for a [Job Title] position at [Company]? I interviewed with [Name, Title]. One specific thing we discussed was [topic]. Keep it professional, genuine, and under 150 words."

**Use:** Within 24 hours of every interview. Same-day is better.

---

## The 4 Critical ChatGPT Mistakes (Langstaff's Warnings)

| Mistake | Why It's Dangerous |
|---------|-------------------|
| **Adding untrue content** | AI fabricates plausible-sounding details you can't defend in an interview. If you didn't do it, don't use it. |
| **Asking for too much at once** | "Write my whole resume" produces generic garbage. One section, one bullet at a time. |
| **Pasting output without reading it** | AI output frequently contains false statements, vague language, and the red-flag words. Read every word. |
| **Not removing AI red flag words** | "Meticulously," "Pioneered," "Realm," "Prowess" — experienced reviewers spot these instantly. Find and delete before submitting. |

---

## AI Red Flag Word Removal Checklist

Scan every AI-generated section and delete or replace:

> Meticulously · Pioneered · Prowess · Realm · Helm · Fostered (overused) ·
> Spearheaded (overused) · Innovative (without proof) · Energetic · Team player ·
> Self-starter · Good communicator · Results-driven (without numbers) ·
> Passionate (vague) · Dynamic · Exceptional · Leverage (overused) · Utilize (use "use") ·
> Synergy · Holistic · Robust · Transformative (without evidence)
