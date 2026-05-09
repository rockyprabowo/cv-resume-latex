# Personal CV LaTeX

This repository contains a LaTeX-based CV with automated tag-based release flows for both GitHub Actions and GitLab CI.

## Structure

- `main.tex`: main document entrypoint
- `commands.tex`: shared layout/macros (`section` style, `jobentry`, `tech`, toggles)
- `sections/`: modular content files
  - `header.tex`
  - `summary.tex`
  - `skills.tex`
  - `experience.tex`
  - `education.tex`
  - `certifications.tex`
  - `languages.tex`
  - `organizational.tex` (currently not included in `main.tex`)
- `scripts/next_tag.py`: generates next date-based tag in `YYYYMMDD-N` format
- `Makefile`: helper target for signed-off commit + tagging + push

## Local Build

Build PDF locally:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

Output:

- `main.pdf`
- `main.log`

## Committing new revision

Use:

```bash
make signoff MSG="your commit message"
```

This will:

1. Generate next tag using `scripts/next_tag.py` (`YYYYMMDD-N`)
2. `git add -A`
3. `git commit -s -m "<MSG>"`
4. Create annotated tag with generated value
5. Push branch
6. Push tags
