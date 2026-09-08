# Md. Tahsinul Hoque Siddiki — Portfolio

This repository keeps the existing portfolio presentation intact while separating the source into maintainable files.

## Structure

- `index.template.html` — page shell and original document structure
- `components/` — page sections/content
- `assets/css/style.css` — original CSS extracted from the page
- `assets/js/main.js` — original JavaScript extracted from the page
- `scripts/build.py` — assembles the source into the deployable `dist/index.html`
- `netlify.toml` — Netlify build configuration
- `.github/workflows/ci.yml` — build validation on GitHub

## Local build

```bash
python3 scripts/build.py
```

The generated `dist/index.html` is assembled from the extracted source files. The original inline CSS and JavaScript are preserved, so the rendered portfolio behavior remains unchanged.

## Updating content

Edit the relevant file under `components/`. For example, portfolio projects are maintained in `components/projects.html` instead of the main page file.
