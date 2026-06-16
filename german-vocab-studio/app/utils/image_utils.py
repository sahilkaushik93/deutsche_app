from PIL import Image
from pathlib import Path


def validate_image(path: str) -> bool:
	try:
		with Image.open(path) as img:
			img.verify()
		return True
	except Exception:
		return False


def resize_to_fit(path: str, max_width: int, max_height: int, dest_path: str = None) -> str:
	dest = dest_path or path
	with Image.open(path) as img:
		img.thumbnail((max_width, max_height), Image.LANCZOS)
		Path(dest).parent.mkdir(parents=True, exist_ok=True)
		img.save(dest)
	return dest


def open_image(path: str) -> Image.Image:
	return Image.open(path)
