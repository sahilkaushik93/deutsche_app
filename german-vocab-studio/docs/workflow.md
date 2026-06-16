# Workflow

This file documents the end-user and developer workflows for the German Vocabulary Studio MVP (Excel → PowerPoint) and describes how future phases (narration, audio, video) will plug into the system.

## User workflow (MVP)

1. Prepare an Excel file (`.xlsx`) with columns: `Word`, `Meaning`, `Synonyms`, `Sentences`, `Image`.
	 - `Synonyms` may be a comma-separated string.
	 - `Sentences` may be a single sentence or multiple separated by `|` or `.`; the service will split heuristically.
	 - `Image` should be the filename located under `data/images/`.
2. Place the Excel in `data/excel/` or upload it using the Streamlit UI (`Upload Words`).
3. Use the Streamlit UI (`Generate PPT`) or run the CLI script: `python scripts/generate_ppt.py`.
4. The generator writes output to `data/generated/ppt/` (file named `German_Words.pptx` by default).
5. Download or open the PPT file and review the slides.

## Developer workflow

- Install dependencies in a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

- Run validator to check your Excel:

```bash
python scripts/validate_excel.py data/excel/words.xlsx
```

- Generate PPT from default Excel:

```bash
python scripts/generate_ppt.py
```

- Run the interactive UI:

```bash
streamlit run app/ui/streamlit_app.py
```

## Internals of generation

- `scripts/generate_ppt.py` calls `app.services.ppt_service.generate_ppt()` which:
	- Loads Excel and builds a `Deck` via `excel_service`.
	- Loads template and `placeholders.json`.
	- Iterates each `Word` and creates a slide with text and, when available, an image.

## File locations

- Input Excel files: `data/excel/`
- Source images: `data/images/`
- Generated PPTs: `data/generated/ppt/`
- Thumbnails / processed images: `data/generated/thumbnails/`

## Future phases (narration & video)

- Narration: `narration_service` will generate text scripts from `Deck` content (word, meaning, sentence) and produce items to be fed to a TTS engine.
- Audio: generated audio files will be stored in `data/generated/audio/`.
- Video: `video_service` will combine slides (or rendered frames) with audio and transitions to produce `data/generated/video/*.mp4`.

## CI / Testing suggestions

- Add unit tests for `excel_service` with small sample Excel files to verify parsing behavior and column validation.
- Add a test for `ppt_service` that generates a PPT into a temp folder and asserts the output file exists and contains the expected number of slides.

## Troubleshooting common issues

- Missing module import errors when running Streamlit: ensure the project root is discoverable by Python. The Streamlit entry adds the project root to `sys.path`, but if you run into import errors ensure you start Streamlit from the project root:

```bash
cd german-vocab-studio
streamlit run app/ui/streamlit_app.py
```

- Excel read errors: ensure the `.xlsx` file is valid (not empty) and uses a supported engine (`openpyxl` recommended). Use the validator script to diagnose problems.
- Image errors: check `data/images/` for the referenced filename and validate image format.

## Maintenance notes

- When upgrading `python-pptx` or `openpyxl`, re-check template behavior; picture placeholder handling has historically changed across versions.
- Keep the `placeholders.json` mapping updated when templates change.

