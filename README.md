# HTTP Status Code CLI Tool

A command-line interface tool for looking up and managing HTTP status codes and their descriptions.

## Features

- Look up HTTP status codes and their descriptions
- Add custom descriptions for status codes
- Reset custom descriptions to default
- List all available HTTP status codes
- Interactive mode for easy exploration
- Shell completion support

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone or download this repository
2. Navigate to the project directory
3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Making the Tool Executable

To make the `http` script executable and available system-wide:

1. Make the script executable:
```bash
chmod +x http
```

2. Add the script to your PATH (choose one of the following methods):

   **Method 1: Create a symbolic link in /usr/local/bin**
   ```bash
   sudo ln -s $(pwd)/http /usr/local/bin/http
   ```

   **Method 2: Add to your shell profile**
   
   For bash (add to ~/.bashrc):
   ```bash
   echo 'export PATH="'$(pwd)':$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```
   
   For zsh (add to ~/.zshrc):
   ```bash
   echo 'export PATH="'$(pwd)':$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

After completing these steps, you can use the tool directly with:
```bash
http get 200
```

## Usage

### Basic Commands

```bash
# Look up a status code
python main.py get 200

# Look up multiple status codes
python main.py get 200 404 500

# Add a custom description
python main.py set 404 "My custom not found message"

# Reset a custom description
python main.py reset 404

# Reset all custom descriptions
python main.py reset-all

# List all status codes
python main.py list

# Show help
python main.py --help
```

### Interactive Mode

```bash
# Start interactive mode
python main.py interactive
```

In interactive mode, you can:
- Enter a status code to look it up
- Type `set <code> <description>` to set a custom description
- Type `reset <code>` to reset a custom description
- Type `reset-all` to reset all custom descriptions
- Type `list` to see all available codes
- Type `help` for available commands
- Type `exit` to quit

## Configuration

The tool stores data in the following locations:

- **Windows**: `%APPDATA%\http-cli\`
- **macOS/Linux**: `~/.config/http-cli/`

Two files are maintained:
- `original_data.json` - Parsed HTTP status codes from the HTML file
- `custom_descriptions.json` - Your custom descriptions

## Project Structure

```
http-tool/
├── main.py                 # Main entry point
├── argument_parser.py      # Command-line argument parsing
├── command_handlers.py     # Command implementations
├── data_manager.py         # Data management and persistence
├── utils.py                # Utility functions
├── requirements.txt        # Python dependencies
├── status codes.html       # Source of HTTP status codes
├── test_*.py              # Test files
└── README.md              # This file
```

## Development

### Running Tests

```bash
# Run all tests
python test_simple.py

# Run specific tests
python test_config.py
python test_parsing.py
```

### Adding New Features

1. Implement the feature in the appropriate module
2. Add tests to verify functionality
3. Update documentation in README.md

## Dependencies

- beautifulsoup4 - HTML parsing
- lxml - XML/HTML parser

## License

This project is for educational use as part of Agile Methods course at HWR Berlin.

## Contributing

This is a course project. Contributions are limited to course participants.