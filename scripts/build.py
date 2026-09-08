from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "index.template.html"

text = TEMPLATE.read_text(encoding="utf-8")
text = text.replace("__INLINE_CSS__", (ROOT / "assets/css/style.css").read_text(encoding="utf-8"))
text = text.replace("__INLINE_JS__", (ROOT / "assets/js/main.js").read_text(encoding="utf-8"))

components = ["NAVBAR", "HERO", "ABOUT", "SKILLS", "PROJECTS", "EXPERIENCE", "EDUCATION", "CONTACT", "FOOTER"]
for name in components:
    path = ROOT / "components" / (name.lower() + ".html")
    text = text.replace(f"__COMPONENT_{name}__", path.read_text(encoding="utf-8"))

out = ROOT / "dist" / "index.html"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(text, encoding="utf-8")
print(f"Built {out}")
