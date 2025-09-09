import os
import sys
from utils import (
    get_config_dir,
    parse_html_to_json,
    save_original_data,
    load_original_data,
    load_custom_data,
    save_custom_data,
)


class DataManager:
    def __init__(self, html_file_path):
        self.config_dir = get_config_dir()
        self.html_file_path = html_file_path
        self.original_data = {}
        self.custom_data = {}
        self.initialize_data()

    def initialize_data(self):
        """Initialize the data by loading or parsing the original data and loading custom data."""
        # Try to load original data from JSON file
        self.original_data = load_original_data(self.config_dir)

        # If original data is empty, parse the HTML file and save it
        if not self.original_data:
            print("Parsing HTML file to extract HTTP status codes...")
            self.original_data = parse_html_to_json(self.html_file_path)
            if self.original_data:
                save_original_data(self.original_data, self.config_dir)
                print(
                    f"Original data saved to {os.path.join(self.config_dir, 'original_data.json')}"
                )
            else:
                print("Error: Could not parse HTML file or extract HTTP status codes.")
                sys.exit(1)

        # Load custom data
        self.custom_data = load_custom_data(self.config_dir)

    def get_description(self, code):
        """Get the description for a given HTTP status code.

        Args:
            code (str): The HTTP status code.

        Returns:
            str: The description for the code, or None if not found.
        """
        # Check if code is valid (3 digits)
        if not code.isdigit() or len(code) != 3:
            return None

        # First check custom data
        if code in self.custom_data:
            return self.custom_data[code]

        # Then check original data
        return self.original_data.get(code)

    def set_custom_description(self, code, description):
        """Set a custom description for a given HTTP status code.

        Args:
            code (str): The HTTP status code.
            description (str): The custom description.

        Returns:
            bool: True if successful, False otherwise.
        """
        # Check if code is valid (3 digits)
        if not code.isdigit() or len(code) != 3:
            return False

        # Check if code exists in original data
        if code not in self.original_data:
            return False

        self.custom_data[code] = description
        return save_custom_data(self.custom_data, self.config_dir)

    def reset_custom_description(self, code):
        """Reset the custom description for a given HTTP status code.

        Args:
            code (str): The HTTP status code.

        Returns:
            bool: True if successful, False otherwise.
        """
        # Check if code is valid (3 digits)
        if not code.isdigit() or len(code) != 3:
            return False

        # Check if code exists in custom data
        if code not in self.custom_data:
            return False

        del self.custom_data[code]
        return save_custom_data(self.custom_data, self.config_dir)

    def reset_all_custom_descriptions(self):
        """Reset all custom descriptions.

        Returns:
            bool: True if successful, False otherwise.
        """
        self.custom_data = {}
        return save_custom_data(self.custom_data, self.config_dir)

    def get_all_codes(self):
        """Get all HTTP status codes.

        Returns:
            list: A list of all HTTP status codes.
        """
        return list(self.original_data.keys())

    def has_custom_description(self, code):
        """Check if a custom description exists for a given HTTP status code.

        Args:
            code (str): The HTTP status code.

        Returns:
            bool: True if a custom description exists, False otherwise.
        """
        return code in self.custom_data
