import sys


def handle_get(data_manager, code):
    """Handle the 'get' command to display the description for an HTTP status code.

    Args:
        data_manager: The DataManager instance.
        code (str): The HTTP status code.
    """
    description = data_manager.get_description(code)

    if description is None:
        print(
            f"Error: Invalid HTTP code '{code}'. Please provide a numeric code between 100 and 599."
        )
        print("Use 'http help' for more information.")
        sys.exit(1)

    if description:
        print(f"{code}: {description}")
    else:
        print(f"Error: HTTP code '{code}' not found.")
        print("Use 'http help' for more information.")
        sys.exit(1)


def handle_edit(data_manager, code, description):
    """Handle the 'edit' command to edit the description for an HTTP status code.

    Args:
        data_manager: The DataManager instance.
        code (str): The HTTP status code.
        description (str): The new description.
    """
    # Check if the code is valid
    if not code.isdigit() or len(code) != 3:
        print(
            f"Error: Invalid HTTP code '{code}'. Please provide a numeric code between 100 and 599."
        )
        print("Use 'http help' for more information.")
        sys.exit(1)

    # Check if the code exists in the original data
    if code not in data_manager.original_data:
        print(f"Error: HTTP code '{code}' not found in the original data.")
        print("Use 'http help' for more information.")
        sys.exit(1)

    # Set the custom description
    if data_manager.set_custom_description(code, description):
        print(f"Description for HTTP code '{code}' has been updated.")
    else:
        print(f"Error: Failed to update description for HTTP code '{code}'.")
        sys.exit(1)


def handle_reset(data_manager, code=None, all=False, yes=False):
    """Handle the 'reset' command to reset descriptions for HTTP status codes.

    Args:
        data_manager: The DataManager instance.
        code (str, optional): The HTTP status code to reset.
        all (bool, optional): Whether to reset all custom descriptions.
        yes (bool, optional): Whether to skip confirmation prompts.
    """
    if all:
        # Reset all custom descriptions
        if not data_manager.custom_data:
            print("No custom descriptions to reset.")
            return

        if not yes:
            print(
                "Alle benutzerdefinierten Beschreibungen werden zurückgesetzt. Fortfahren? (yes/NO)"
            )
            confirmation = input().strip().lower()
            if confirmation != "yes":
                print("Operation cancelled.")
                return

        if data_manager.reset_all_custom_descriptions():
            print("All custom descriptions have been reset to their original values.")
        else:
            print("Error: Failed to reset custom descriptions.")
            sys.exit(1)
    elif code:
        # Reset a specific code
        if not code.isdigit() or len(code) != 3:
            print(
                f"Error: Invalid HTTP code '{code}'. Please provide a numeric code between 100 and 599."
            )
            print("Use 'http help' for more information.")
            sys.exit(1)

        if not data_manager.has_custom_description(code):
            print(f"HTTP code '{code}' has no custom description to reset.")
            return

        if data_manager.reset_custom_description(code):
            print(
                f"Description for HTTP code '{code}' has been reset to its original value."
            )
        else:
            print(f"Error: Failed to reset description for HTTP code '{code}'.")
            sys.exit(1)
    else:
        print("Error: Either specify a code or use --all to reset all descriptions.")
        print("Use 'http help' for more information.")
        sys.exit(1)


def handle_help(data_manager, command=None):
    """Handle the 'help' command to display help information.

    Args:
        data_manager: The DataManager instance.
        command (str, optional): The specific command to show help for.
    """
    if command == "reset":
        print("Usage: http reset <code>")
        print("       http reset --all [--yes]")
        print()
        print("Reset the description for an HTTP status code to its original value.")
        print()
        print("Arguments:")
        print("  <code>          The HTTP status code to reset (e.g., 200, 404)")
        print()
        print("Options:")
        print(
            "  --all           Reset all custom descriptions to their original values"
        )
        print(
            "  --yes, -y       Skip confirmation prompt when resetting all descriptions"
        )
        print()
        print("Examples:")
        print("  http reset 404           Reset the description for HTTP code 404")
        print(
            "  http reset --all         Reset all custom descriptions with confirmation"
        )
        print(
            "  http reset --all --yes   Reset all custom descriptions without confirmation"
        )
        return

    print("HTTP Status Code CLI Tool")
    print()
    print("Usage:")
    print(
        "  http <code>                 Display the description for an HTTP status code"
    )
    print("  http edit <code> <desc>     Edit the description for an HTTP status code")
    print("  http reset <code>           Reset the description for an HTTP status code")
    print("  http reset --all [--yes]    Reset all custom descriptions")
    print("  http help                   Display this help message")
    print()
    print("Commands:")
    print(
        "  <code>                      Display the description for an HTTP status code"
    )
    print("                              Example: http 200")
    print()
    print("  edit <code> <description>   Edit the description for an HTTP status code")
    print("                              Example: http edit 404 'Custom Not Found'")
    print()
    print("  reset <code>                Reset the description for an HTTP status code")
    print("                              Example: http reset 404")
    print()
    print("  reset --all [--yes]         Reset all custom descriptions")
    print("                              Example: http reset --all")
    print("                              Example: http reset --all --yes")
    print()
    print("  help                        Display this help message")
    print()
    print("Error Handling:")
    print("  If an invalid or unknown HTTP code is provided, an error message will be")
    print("  displayed along with a hint to use 'http help'.")
