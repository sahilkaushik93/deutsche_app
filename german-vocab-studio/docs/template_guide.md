# PPT Template Guide

This document explains how to author and maintain PowerPoint templates for German Vocabulary Studio. The generator maps named placeholders in a PPTX template to fields on the `Word` model so slide design can change without code changes.

## Placeholder concept

- Placeholders are shapes in the slide master or layout that are given a recognizable name or alt text (for example in PowerPoint: select a shape → Format Shape → Alt Text → Title, or use the Selection Pane to rename shapes).
- The project expects a JSON mapping file at `app/templates/ppt/placeholders.json` which maps template placeholder names to model keys.

Example `placeholders.json`:

```json
{
	"WORD_BOX": "word",
	"MEANING_BOX": "meaning",
	"SYNONYM_BOX": "synonyms",
	"SENTENCE_BOX": "sentences",
	"IMAGE_BOX": "image"
}
```

## Recommended placeholder names and behavior

- `WORD_BOX` — primary word text. Large font, bold. Expected single-line or short phrase.
- `MEANING_BOX` — short English meaning. Medium font.
- `SYNONYM_BOX` — comma-separated synonyms. Smaller font; may be omitted if empty.
- `SENTENCE_BOX` — example sentence(s). Support up to N lines; generator will take a list and join with newlines.
- `IMAGE_BOX` — picture placeholder or a free-form shape where a generated image can be inserted. Use a picture placeholder when possible so PowerPoint maintains aspect ratio and position.

Notes:
- If your template uses different names, update `placeholders.json` to map them to `word`, `meaning`, `synonyms`, `sentences`, `image`.
- The generator currently inserts images with a fixed bounding box (controlled by code). Templates with a picture placeholder will look better because PowerPoint can apply sizing rules.

## Creating a template (authoring checklist)

1. Open PowerPoint and create a new presentation.
2. Create one master slide/layout for the vocabulary slide.
3. Add textboxes and name them via the Selection Pane or Alt Text.
4. Add a picture placeholder (Insert → Picture Placeholder) and name it `IMAGE_BOX` (or your chosen name mapped in placeholders.json).
5. Set default fonts, colors, and sizes in the master so slides inherit consistent styling.
6. Save template to `app/templates/ppt/german_template.pptx`.

## Practical tips

- Use large, legible fonts for `WORD_BOX` (e.g., 28-36pt) and slightly smaller for meanings and sentences as defined in `app/config/layout_config.json`.
- Keep margins consistent; the code places textboxes at fixed positions unless extended to read shape coordinates from the template (future improvement).
- If you plan to include additional fields (e.g., `EXAMPLE_TRANSLATION`), add the placeholder name to `placeholders.json` and extend code to handle that key.

## Versioning templates

- Keep template files under `app/templates/ppt/` and treat them like assets. When changing the template, increment a small version indicator in the file name (e.g., `german_template_v2.pptx`) to avoid breaking existing generated decks.

## Troubleshooting

- If generated slides are missing text, confirm the mapping in `placeholders.json` matches the shape names in the template.
- If images fail to appear, confirm the image file name referenced in the Excel exists under `data/images/` and is a valid image.

