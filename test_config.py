import os
from utils import get_config_dir, load_original_data

print("Checking config directory...")
config_dir = get_config_dir()
print(f"Config directory: {config_dir}")

print("\nChecking if original_data.json exists...")
original_data_path = os.path.join(config_dir, "original_data.json")
print(f"Original data path: {original_data_path}")
print(f"File exists: {os.path.exists(original_data_path)}")

print("\nTrying to load original data...")
original_data = load_original_data(config_dir)
print(f"Loaded {len(original_data)} entries from original data")

if not original_data:
    print("Original data is empty. The HTML file will be parsed on next run.")
