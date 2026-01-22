import os
import requests
import sys
from pathlib import Path

# URLs for 36UUD Aug 28 2023 - Can be parameterized later
BASE_URL = "http://sentinel-s2-l2a.s3.amazonaws.com/tiles/36/U/UD/2023/8/28/0"
BANDS = {
    "B03": "R10m/B03.jp2",
    "B04": "R10m/B04.jp2",
    "B05": "R20m/B05.jp2",
    "B08": "R10m/B08.jp2",
    "B11": "R20m/B11.jp2",
    "B12": "R20m/B12.jp2"
}

def download_file(url, filepath):
    """Downloads a file from a URL to a local path."""
    print(f"Downloading {url} to {filepath}...")
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print("Done.")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def download_sentinel_data(output_dir):
    """Downloads Sentinel-2 bands to the specified directory."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"Starting Sentinel-2 Data Download (36UUD, 2023-08-28) to {output_path}...")
    
    for band_name, relative_path in BANDS.items():
        url = f"{BASE_URL}/{relative_path}"
        filename = f"T36UUD_20230828_{band_name}.jp2"
        filepath = output_path / filename
        
        if filepath.exists():
            print(f"File {filename} already exists. Skipping.")
        else:
            download_file(url, filepath)

    print("All downloads complete.")
