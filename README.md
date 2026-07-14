# Portfolio Site Draft

Static resume-friendly portfolio draft for Matt Andersen.

## Purpose

This portfolio site presents resume-backed software verification, QA automation, API validation, and reliability-testing experience without inventing unsupported claims.

## Current status

- Static HTML/CSS/JS only
- No bundler/framework required
- Small deploy build script copies public site files into `dist/`
- Designed for GitHub Pages or any static host
- Email/contact details are based on the user-provided resume
- Phone number is intentionally omitted from the public page unless explicitly confirmed
- Content evidence and publish blockers are tracked under `content/`

## Featured projects

- Guild Task Tracker — verified live app and public repository
- Twilio / OpenClaw Intake Agent — local architecture/design package, not a launched production system
- Sage-Nexus — public repository, conservatively framed until README/details are strengthened

## Before publishing

Replace or confirm:

- LinkedIn URL
- Resume PDF
- Whether to publish the phone number publicly
- Whether Sage-Nexus should be featured publicly
- Whether Twilio/OpenClaw intake should link to a public artifact or remain a local case study

See:

- `content/SOURCES.md`
- `content/PLACEHOLDERS.md`

## Local preview

Use any static server. Example:

```bash
python -m http.server 4173
```

Then open:

```text
http://localhost:4173
```

## Validation

```bash
python tools/validate_site.py
```

This checks linked local assets, internal anchors, and expected portfolio content.

## Build deploy artifact

```bash
python tools/build_static.py
```

This creates `dist/` with only the public website files:

- `index.html`
- `styles.css`
- `script.js`
- `assets/`
- `.nojekyll`

It intentionally does **not** publish `content/`, `tools/`, or this README as site pages.

## GitHub Pages Actions deployment

A Pages workflow is included at:

```text
.github/workflows/deploy.yml
```

It runs on pushes to `main` and manual `workflow_dispatch`:

1. Checks out the repo.
2. Sets up Python.
3. Runs `python tools/validate_site.py`.
4. Runs `python tools/build_static.py`.
5. Uploads `dist/` to GitHub Pages.
6. Deploys via `actions/deploy-pages`.

Recommended repo for publishing:

```text
Mandersen1208.github.io
```

Recommended live URL:

```text
https://mandersen1208.github.io/
```

Alternative: use a dedicated project repo such as `matt-andersen-portfolio`, which would publish under a subpath.

Do **not** deploy this directly from the broader `workspace-roy` repo.

## Deployment options

- New GitHub Pages user site repo: `Mandersen1208.github.io` (recommended)
- New project Pages repo: `matt-andersen-portfolio`
- Existing GitHub Pages resume repo after review
- Custom domain later

Keep this as a static site unless the resume needs dynamic content or CMS editing.
