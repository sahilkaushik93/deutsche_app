from pathlib import Path
import shutil
import sys

# Ensure project root is on sys.path so `from app...` imports work if needed
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def import_folder(src: str, dest: str):
	s = Path(src)
	d = Path(dest)
	d.mkdir(parents=True, exist_ok=True)
	for f in s.iterdir():
		if f.is_file():
			shutil.copy2(f, d / f.name)


if __name__ == '__main__':
	# example usage: adjust paths as needed
	import_folder('data/images', 'data/generated/images')
