import time
from utils import parse_html_to_json

print("Starting HTML parsing test...")
start_time = time.time()

try:
    # Test the HTML parsing
    result = parse_html_to_json("status codes.html")
    end_time = time.time()

    print(f"Parsing completed in {end_time - start_time:.2f} seconds")
    print(f"Found {len(result)} HTTP status codes")

    # Print first few codes as a sample
    for i, (code, desc) in enumerate(result.items()):
        if i >= 5:  # Only print first 5
            break
        print(f"{code}: {desc[:50]}...")

except Exception as e:
    print(f"Error during parsing: {e}")
