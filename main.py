#!/usr/bin/env python3
import sys
import os

from data_manager import DataManager
from argument_parser import parse_arguments
from command_handlers import handle_get, handle_edit, handle_reset, handle_help


def main():
    """Main entry point for the HTTP CLI tool."""
    # Get the path to the HTML file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_file_path = os.path.join(script_dir, "status codes.html")

    # Check if the HTML file exists
    if not os.path.exists(html_file_path):
        print(
            f"Error: HTML file 'status codes.html' not found in the script directory."
        )
        sys.exit(1)

    # Initialize the data manager
    try:
        data_manager = DataManager(html_file_path)
    except Exception as e:
        print(f"Error initializing data manager: {e}")
        sys.exit(1)

    # Parse command-line arguments
    try:
        command, args = parse_arguments(sys.argv[1:])
    except SystemExit:
        # argparse calls sys.exit on error, which is fine
        sys.exit(1)

    # Handle the command
    try:
        if command == "get":
            handle_get(data_manager, args["code"])
        elif command == "edit":
            handle_edit(data_manager, args["code"], args["description"])
        elif command == "reset":
            handle_reset(
                data_manager,
                code=args.get("code"),
                all=args.get("all", False),
                yes=args.get("yes", False),
            )
        elif command == "help":
            handle_help(data_manager, args.get("command"))
        else:
            print("Error: Unknown command.")
            handle_help(data_manager)
            sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
