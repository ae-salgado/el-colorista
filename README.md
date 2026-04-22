# Colorista

Extract the real color palette from any image — with emotions, vibe, and optional AI description. Runs 100% locally, no API keys needed.

---

## What it does

Drop any image in. Colorista pulls the actual colors from it, maps each one to an emotion and a vibe, and prints a clean palette to your terminal. Optionally, ask the AI to describe the mood of the whole palette.

```
uv run main.py golden.jpg
uv run main.py golden.jpg --vibe        # + AI description via Ollama
uv run main.py golden.jpg --count 8    # extract 8 colors instead of 6
```

---

## Stack

- **Python + UV** — dependency management
- **ColorThief** — extracts real dominant colors from images
- **Rich** — terminal palette display with color swatches
- **Pydantic** — data validation
- **Ollama + LLaMA 3.2** — local AI description (optional, `--vibe` flag)

---

## Setup

### 1. Install Ollama (only needed for `--vibe`)
```bash
# Download from https://ollama.com
ollama pull llama3.2:3b
```

### 2. Clone and install
```bash
git clone https://github.com/ae-salgado/colorista.git
cd colorista
uv sync
```

---

## Usage

```bash
# Basic palette extraction
uv run main.py photo.jpg

# More colors
uv run main.py photo.jpg --count 8

# With AI vibe description (requires Ollama)
uv run main.py photo.jpg --vibe
```

---

## Project Structure

```
colorista/
└── pyproject.toml
└── src/
    ├── main.py           # CLI entry point
    ├── image_parser.py   # Extracts colors from image
    ├── color_parser.py   # Hex ↔ HLS conversion
    ├── emotions_lib.py   # Color → emotion mapping
    ├── models.py         # Pydantic data models
    ├── display.py        # Rich terminal output
```

---

## How it works

```
Image → ColorThief extracts N real colors
      → Each color converted to HLS
      → Hue mapped to emotion + vibe
      → Rich renders swatches in terminal
      → (optional) Ollama describes the full palette
```

---

## Why no fake palette generation?

Most color tools extract 1 dominant color then *mathematically generate* the rest using color theory offsets. Colorista skips that — every color in the output actually exists in your image.

---

Made with 🤙