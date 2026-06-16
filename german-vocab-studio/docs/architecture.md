# Architecture

## Overview

German Vocabulary Studio is a small, modular application designed to transform vocabulary data (Excel) into PowerPoint presentations and — in future phases — into narrated, animated video lessons. The codebase is intentionally layered so that IO, business logic, rendering, and UI are separable and replaceable.

Goals:
- Keep slide generation template-driven (no hard-coded coordinates)
- Make services testable and independent of UI
- Allow future expansion (narration, audio generation, video) without changing core data flow

## High-level Components

- `app.models` — Domain models representing vocabulary content (e.g., `Word`, `Deck`).
- `app.services` — Reusable services that perform the heavy lifting:
	- `excel_service` — read/validate Excel and build `Deck` model
	- `ppt_service` — load PPT template, map placeholders, create slides, save output
	- `image_service` — validate, crop/resize images
	- `narration_service` (future) — build narration scripts
	- `video_service` (future) — render MP4 from slides + audio
- `app.utils` — small helpers for file IO, image processing, PPT helpers and logging
- `app.ui` — Streamlit-based UI for interactive upload and generation
- `scripts/` — simple CLI entrypoints for common tasks (validate, generate, bulk import)
- `data/` — storage for input decks, images, and generated outputs

Directory relationships and responsibilities are intentionally simple so that each folder can be run or tested independently.

## Data Flow

1. User provides an Excel file (`data/excel/*.xlsx`) with columns such as `Word`, `Meaning`, `Synonyms`, `Sentences`, `Image`.
2. `excel_service` reads the file, validates required columns and constructs a `Deck` containing `Word` objects.
3. `ppt_service` loads a PowerPoint template (master slides with named placeholders) and the placeholder mapping (`app/templates/ppt/placeholders.json`).
4. For each `Word` in the `Deck`, the service creates a new slide, replaces placeholder content (text and images), and writes the final `.pptx` to `data/generated/ppt/`.
5. Optional: `narration_service` and `video_service` (future) will consume the same `Deck` to produce scripts, voice, animations, and MP4 output.

## Template-driven slide generation

The key design decision is to rely on named placeholders inside the PowerPoint template rather than hard-coded coordinates. The template must contain shapes (textboxes or picture placeholders) whose shape `name` or `alt_text` identifies them (e.g., `WORD_BOX`, `MEANING_BOX`, `IMAGE_BOX`). A JSON file maps these placeholder names to model keys (e.g., `WORD_BOX` → `word`). This allows slide designers to change layout and style without changing code.

## Integration and Extensibility Points

- To add a new output format (e.g., PDF export), implement a new service under `app.services` that accepts a `Deck`.
- To change how images are processed, replace or extend `app.services.image_service` and `app.utils.image_utils`.
- To change template mapping, update `app/templates/ppt/placeholders.json` or support multiple mapping files.

## Error handling & logging

- Services log errors to a module-scoped logger (`app.utils.logger`) and raise exceptions for fatal issues (missing required columns, missing files). UI layers catch exceptions and present user-friendly messages.
- Long-running operations (video generation, narration) should be asynchronous in future — consider a task queue (Celery/RQ) for production workloads.

## Running the application

- Install dependencies: `pip install -r requirements.txt` (uses `pandas`, `python-pptx`, `pillow`, `streamlit`, `moviepy` for future phases).
- Run Streamlit UI: `streamlit run app/ui/streamlit_app.py`.
- CLI scripts live in `scripts/` and are runnable directly, they add the project root to `sys.path` to support `from app.*` imports.

## Testing

- Unit tests should target services (Excel parsing, deck modeling, PPT generation logic) rather than Streamlit UI.
- Add tests under `tests/` that create small sample decks and assert exported files exist and contain expected content.

## Security & Data

- The application processes user-provided files — treat uploaded content as untrusted. Validate file types and content before processing.
- Do not run arbitrary code embedded in input files. Treat binary and text content conservatively.

## Diagram (text)

User -> Streamlit / CLI -> excel_service -> Deck -> ppt_service -> generated PPT

