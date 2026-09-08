# Md. Tahsinul Hoque Siddiki - Portfolio

Personal portfolio website showcasing my background, technical skills, projects, experience, education, and contact information.

🌐 **Live Portfolio:** https://tahsinulhoque.netlify.app/

This project was restructured from a single HTML file into a maintainable source structure without changing the existing website's design, content, or behavior.

## ✨ Features

- Responsive personal portfolio website
- Hero, About, Skills, Projects, Experience, Education, and Contact sections
- Mobile-friendly navigation
- Typing animation and scroll-based effects
- Netlify contact form
- Modular HTML components
- Centralized CSS and JavaScript
- Python-based build process
- GitHub Actions CI validation
- Automatic Netlify deployment from GitHub

## 🛠️ Technologies

- HTML5
- CSS3
- JavaScript
- Python
- Git & GitHub
- GitHub Actions
- Netlify

## 📁 Project Structure

```text
Portfolio-Website/
├── .github/
│   └── workflows/
│       └── ci.yml
├── assets/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── components/
│   ├── about.html
│   ├── contact.html
│   ├── education.html
│   ├── experience.html
│   ├── footer.html
│   ├── hero.html
│   ├── navbar.html
│   ├── projects.html
│   └── skills.html
├── dist/
│   └── index.html
├── scripts/
│   └── build.py
├── .gitignore
├── index.template.html
├── netlify.toml
└── README.md
```

## 🔄 How It Works

The editable source files are separated into `components/`, `assets/`, and `index.template.html`.

The Python build script combines these source files and generates the deployable file:

```text
dist/index.html
```

This keeps the project organized and makes future portfolio updates easier.

## 💻 Local Development

### Clone the repository

```bash
git clone https://github.com/tahsinulhoque/Personal-portfolio-website.git
cd Personal-portfolio-website
```

### Build the project

Make sure Python 3 is installed, then run:

```bash
python scripts/build.py
```

On Linux/macOS:

```bash
python3 scripts/build.py
```

### Preview locally

```bash
python -m http.server 8000 --directory dist
```

Then open `http://localhost:8000` in your browser.

## ✏️ Updating the Portfolio

Edit the source files instead of editing `dist/index.html`.

| Section | File |
|---|---|
| Hero | `components/hero.html` |
| About | `components/about.html` |
| Skills | `components/skills.html` |
| Projects | `components/projects.html` |
| Experience | `components/experience.html` |
| Education | `components/education.html` |
| Contact | `components/contact.html` |
| Navbar | `components/navbar.html` |
| Footer | `components/footer.html` |
| Styling | `assets/css/style.css` |
| JavaScript | `assets/js/main.js` |

After making changes:

```bash
python scripts/build.py
```

## 🚀 CI/CD Pipeline

The portfolio is connected to GitHub Actions and Netlify for automated validation and deployment.

```text
VS Code
   ↓
Edit Source Files
   ↓
git add .
   ↓
git commit
   ↓
git push
   ↓
GitHub
   ↓
GitHub Actions
   ↓
Build Validation
   ↓
Netlify
   ↓
Live Portfolio
```

### GitHub Actions

Every push to `main` and every pull request targeting `main` runs the CI workflow.

The workflow:

1. Checks out the repository
2. Sets up Python
3. Runs the portfolio build
4. Verifies that `dist/index.html` is generated successfully

Workflow:

```text
.github/workflows/ci.yml
```

### Netlify

Netlify automatically deploys the latest version from the GitHub `main` branch.

**Build command:**

```bash
python3 scripts/build.py
```

**Publish directory:**

```text
dist
```

## 📦 Deployment Workflow

For normal updates, simply run:

```bash
git add .
git commit -m "Update portfolio"
git push
```

GitHub Actions validates the build, and Netlify automatically deploys the updated version.

No manual upload is required.

## 🔗 Links

- **Live Portfolio:** https://tahsinulhoque.netlify.app/
- **GitHub:** https://github.com/tahsinulhoque/Personal-portfolio-website
- **LinkedIn:** https://www.linkedin.com/in/tahsinulhoque/

## 👤 Author

**Md. Tahsinul Hoque Siddiki**

Computer Science Graduate | DevOps, Cloud & Operations Enthusiast

## 📄 License

This project is intended for personal portfolio use.
