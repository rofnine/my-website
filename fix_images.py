import os
from PIL import Image

assets_dir = "./assets"
files_to_fix = ["youtube_record.png", "instagram_record.png", "naver_record.png"]

for f in files_to_fix:
    path = os.path.join(assets_dir, f)
    if os.path.exists(path):
        try:
            with Image.open(path) as img:
                print(f"{f}: format={img.format}, size={img.size}")
                # Re-save to guarantee it's a valid PNG
                img.save(path, format="PNG")
                print(f"Fixed {f}")
        except Exception as e:
            print(f"Failed to process {f}: {e}")
    else:
        print(f"{f} not found at {path}")
