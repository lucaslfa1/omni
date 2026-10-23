"""Package the standalone skills (standalone/) for upload, and optionally install them locally.

The plugin versions in skills/ ship with the omni plugin and are not packaged here.

    python scripts/build.py            # dist/<skill>.zip for claude.ai, ChatGPT, Gemini
    python scripts/build.py --install  # also copy each skill to ~/.agents/skills (Codex, Antigravity)
"""
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STANDALONE = ROOT / "standalone"
DIST = ROOT / "dist"
AGENTS = Path.home() / ".agents" / "skills"


def build(skill: Path) -> Path:
    DIST.mkdir(exist_ok=True)
    out = DIST / f"{skill.name}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(skill.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(STANDALONE).as_posix())
    return out


def install(skill: Path) -> Path:
    target = AGENTS / skill.name
    shutil.copytree(skill, target, dirs_exist_ok=True)
    return target


if __name__ == "__main__":
    for skill in sorted(p for p in STANDALONE.iterdir() if (p / "SKILL.md").is_file()):
        print("built    ", build(skill))
        if "--install" in sys.argv:
            print("installed", install(skill))
