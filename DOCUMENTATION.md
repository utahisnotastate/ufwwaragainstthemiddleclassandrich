# UFW Repository Documentation

Documentation is **split by language**. Each language has its own folder with **no mixed-language pages**.

## Choose your language

**[M5-Utah/docs/README.md](M5-Utah/docs/README.md)** — language picker (English, Estonian, Finnish, Russian, Chinese, Japanese)

| Language | Start here |
|----------|--------------|
| English | [M5-Utah/docs/en/README.md](M5-Utah/docs/en/README.md) |
| Eesti | [M5-Utah/docs/et/README.md](M5-Utah/docs/et/README.md) |
| Suomi | [M5-Utah/docs/fi/README.md](M5-Utah/docs/fi/README.md) |
| Русский | [M5-Utah/docs/ru/README.md](M5-Utah/docs/ru/README.md) |
| 中文 | [M5-Utah/docs/zh/README.md](M5-Utah/docs/zh/README.md) |
| 日本語 | [M5-Utah/docs/ja/README.md](M5-Utah/docs/ja/README.md) |

---

## What is documented

### M5-Utah (buildable hardware)

Inside each language folder:

| Guide | File |
|-------|------|
| Children | `01-FOR_CHILDREN.md` |
| Non-technical users | `02-FOR_NON_TECHNICAL_USERS.md` |
| Technical users | `03-FOR_TECHNICAL_USERS.md` |
| Scientists | `04-FOR_SCIENTISTS.md` |
| Skeptics | `05-FOR_SKEPTICS.md` |
| **Migration (original → M5)** | `06-MIGRATION_FROM_ORIGINAL.md` |
| **Original pre-M5 approach** | `07-ORIGINAL_WORLDA_APPROACH.md` |
| Glossary | `GLOSSARY.md` |
| Artifact catalog | `ARTIFACTS.md` |

### UFW archive (27 original projects)

Per-project manuals remain in each project folder (`*_MANUAL.md`, `*_SCIENCE.md`). The **original World-A approach** is summarized in `07-ORIGINAL_WORLDA_APPROACH.md` in your language folder.

---

## Quick commands (same in all locales)

```bash
cd M5-Utah
py -3 run_studio.py --list
py -3 run_omni_flash.py
py -3 run_studio.py --artifact zero_point_gpu
```
