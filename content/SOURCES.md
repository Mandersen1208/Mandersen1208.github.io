# Portfolio Sources and Evidence

This file tracks which public/site claims are backed by known artifacts. Keep this updated before publishing or adding stronger claims.

## Profile

- Name used: Matthew / Matt Andersen
- Source: user-provided resume text in chat on 2026-07-13.
- Public location: New Hill, NC.
- Public email: `mattandersen2016@gmail.com`.
- Public GitHub profile: `https://github.com/Mandersen1208` (primary account confirmed by user).
- Public LinkedIn profile: `https://www.linkedin.com/in/matthew-steven-andersen/` (provided by user on 2026-07-13).
- Phone number appears in the provided resume, but is intentionally omitted from the public web page unless the user explicitly confirms that it should be public.
- Resume PDF is not yet provided.

## Resume / experience

Status: `user-provided-resume`

Source: user-provided resume text in chat on 2026-07-13.

Allowed claims:

- Target: Software Verification Engineer, QA Automation, API & System Reliability Testing.
- 6 years of experience validating enterprise applications, APIs, backend workflows, and performance-sensitive systems.
- Applied Information Sciences — Software Tester / QA Analyst, Remote, Dec 2024 – Present.
- General Motors — Software Quality Engineer / QA Automation Lead, Roswell, GA, Oct 2020 – Aug 2023.
- General Motors — Software Engineer, Roswell, GA, Aug 2023 – Aug 2024.
- B.S. Computer Information Systems — Software Development, DeVry University, Lawrenceville, GA, Dec 2020.
- Microsoft Certified: Azure Fundamentals (AZ-900).
- Microsoft Certified: Azure AI Fundamentals (AI-900).
- Skills listed in the resume: Python scripting, Java, SQL, JavaScript, TypeScript, Selenium, Playwright, JMeter, LoadRunner, Microsoft Graph API testing, Git, Jenkins, Azure DevOps, GitHub Actions, Docker, Kubernetes, CI/CD QA workflows, Spring, Angular, React exposure.

Avoid / qualify:

- Do not publish phone number without explicit confirmation.
- Do not add a downloadable resume PDF until the user provides it.
- Keep metrics tied to resume wording: approximately `$50K per month` savings, 16 engineers trained.

## Guild Task Tracker

Status: `live-demo`

Evidence:

- Live app: `https://mandersen1208.github.io/guild-task-tracker/`
- Public repo: `https://github.com/Mandersen1208/guild-task-tracker`
- Local source: `../guild-task-tracker/README.md`
- Local docs:
  - `../guild-task-tracker/docs/GUILD_REVIEW_TRACKER.md`
  - `../guild-task-tracker/docs/DATA_MODEL.md`
  - `../guild-task-tracker/docs/QA_CHECKLIST.md`
  - `../guild-task-tracker/docs/DECISIONS.md`

Allowed claims:

- React/Vite/TypeScript task tracker.
- localStorage persistence.
- Optional due date and due time.
- Best-effort browser/PWA reminders when app is open or active.
- End-of-day reminder settings.
- GitHub Pages deployment.
- Service-worker/PWA foundation with documented limits.
- QA/data/decision tracking documentation exists.

Avoid / qualify:

- Do not claim reliable background scheduled notifications.
- Do not claim account sync, cloud backup, or backend infrastructure.
- Live app branding currently says Kawaii Daily; portfolio card should explain that this is the published product name.

## Twilio / OpenClaw Intake Agent

Status: `local-case-study` / `planning-package`

Evidence:

- `../twilio-intake-architecture-phase1.md`
- `../twilio-intake-implementation-phase1.md`
- `../twilio-intake-ux-design-phase1.md`
- `../PHASE_ONE_MVP_CRITERIA.md`
- `../twilio-intake/DATA-STRATEGY.md`

Allowed claims:

- Phase One architecture/design/implementation-outline package.
- Conversational UX and prompt strategy were drafted.
- Structured field + free-form notes model was defined.
- Guardrail, QA, and data strategy criteria were documented.

Avoid / qualify:

- Do not claim production deployment.
- Do not claim live Twilio number or real call traffic.
- Do not claim customers/users.
- Do not claim full backend implementation unless later built and verified.

## Sage-Nexus

Status: `external-repo-inspected`

Evidence:

- Public repo: `https://github.com/Mandersen1208/Sage-Nexus`
- README inspected via GitHub API on 2026-07-13.
- `docs/STATUS.md` inspected via GitHub API on 2026-07-13.

Allowed claims:

- Standalone Sage runtime extracted from OpenClaw.
- Go manager/orchestration control plane.
- React/Vite dashboard.
- TypeScript MCP tool service.
- Go ACP admission service.
- Redis for task events, chat sessions, work context, and runtime state.
- Postgres/pgvector canonical skill registry.
- Docker Compose startup flow, runtime status docs, provider auth notes, and verification commands.
- Systems thinking around orchestration, tool governance, session memory, and operational handoff.

Avoid / qualify:

- Do not claim production deployment or external users.
- Do not claim performance, scale, uptime, security compliance, or business outcomes without fresh evidence.

## Other public repositories

Status: `github-public-repo-inventory`

Evidence:

- Public GitHub repo inventory inspected via GitHub API on 2026-07-13.
- ProjectDashbored README inspected via GitHub API on 2026-07-13.
- Fintech-Bot- README inspected via GitHub API on 2026-07-13.
- `matts-resume-site` and `ProfessionalPage` READMEs are Create React App boilerplate; describe only as earlier React/resume-page iterations.
- `EmailApi` and `EmailAPIv2` have sparse/garbled README evidence; describe only by public repo name/language and conservative API-practice framing.

Allowed linked repos:

- `https://github.com/Mandersen1208/ProjectDashbored`
- `https://github.com/Mandersen1208/Fintech-Bot-`
- `https://github.com/Mandersen1208/EmailAPIv2`
- `https://github.com/Mandersen1208/EmailApi`
- `https://github.com/Mandersen1208/matts-resume-site`
- `https://github.com/Mandersen1208/ProfessionalPage`

Avoid / qualify:

- Do not imply these are production systems unless the repo itself proves it.
- Keep sparse repositories labeled as practice, historical, or earlier iterations.

## Publish blockers

See `PLACEHOLDERS.md`.
