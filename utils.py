import os
import re
import json
from bs4 import BeautifulSoup


def get_config_dir():
    """Get the platform-specific configuration directory."""
    if os.name == "nt":  # Windows
        config_dir = os.path.join(os.environ.get("APPDATA", ""), "http-cli")
    else:  # macOS and Linux
        config_dir = os.path.join(os.path.expanduser("~"), ".config", "http-cli")

    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    return config_dir


def truncate_to_words(text, max_words=100):
    """Truncate text to a maximum number of words."""
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words]) + "..."


def parse_html_to_json(html_file_path):
    """Parse the HTML file and extract HTTP status codes and descriptions."""
    try:
        with open(html_file_path, "r", encoding="utf-8") as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, "html.parser")
        status_codes = {}

        # Find all dl elements directly in the document
        dl_elements = soup.find_all("dl")

        for dl in dl_elements:
            dt_elements = dl.find_all("dt")
            dd_elements = dl.find_all("dd")

            for i in range(len(dt_elements)):
                dt = dt_elements[i]
                dd = dd_elements[i] if i < len(dd_elements) else None

                # Extract the status code from dt
                code_text = dt.get_text().strip()
                code_match = re.match(r"^(\d{3})\s", code_text)

                if code_match:
                    code = code_match.group(1)

                    # Extract description from dd
                    if dd:
                        description = dd.get_text().strip()
                        # Clean up the description
                        description = re.sub(r"\s+", " ", description)
                        description = truncate_to_words(description)
                        status_codes[code] = description

        return status_codes

    except Exception as e:
        print(f"Error parsing HTML file: {e}")
        return {}


def save_original_data(data, config_dir):
    """Save the original HTTP status codes data to a JSON file."""
    original_data_path = os.path.join(config_dir, "original_data.json")
    try:
        with open(original_data_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        return original_data_path
    except Exception as e:
        print(f"Error saving original data: {e}")
        return None


def load_original_data(config_dir):
    """Load the original HTTP status codes data from a JSON file."""
    original_data_path = os.path.join(config_dir, "original_data.json")
    try:
        if os.path.exists(original_data_path):
            with open(original_data_path, "r", encoding="utf-8") as file:
                return json.load(file)
        return {}
    except Exception as e:
        print(f"Error loading original data: {e}")
        return {}


def load_custom_data(config_dir):
    """Load the custom HTTP status codes data from a JSON file."""
    custom_data_path = os.path.join(config_dir, "custom_descriptions.json")
    try:
        if os.path.exists(custom_data_path):
            with open(custom_data_path, "r", encoding="utf-8") as file:
                return json.load(file)
        return {}
    except Exception as e:
        print(f"Error loading custom data: {e}")
        return {}


def save_custom_data(data, config_dir):
    """Save the custom HTTP status codes data to a JSON file."""
    custom_data_path = os.path.join(config_dir, "custom_descriptions.json")
    try:
        with open(custom_data_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Error saving custom data: {e}")
        return False
