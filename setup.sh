#!/bin/bash

# Setup script for HTTP Status Code CLI Tool

set -e

echo "Setting up HTTP Status Code CLI Tool..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

# Check Python version
python_version=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
required_version="3.7"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "Error: Python 3.7 or higher is required. Found Python $python_version."
    exit 1
fi

echo "Python $python_version found."

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip is not installed. Please install pip."
    exit 1
fi

echo "Installing dependencies..."
pip3 install -r requirements.txt

# Create directories for shell completion if they don't exist
mkdir -p completion/bash
mkdir -p completion/zsh

# Create bash completion file
cat > completion/bash/http-completion.bash << 'EOF'
#!/bin/bash

# Bash completion for HTTP Status Code CLI Tool

_http_completion() {
    local cur prev commands
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    commands="get set reset reset-all list interactive shell help"

    if [[ ${COMP_CWORD} -eq 1 ]] ; then
        COMPREPLY=( $(compgen -W "${commands}" -- ${cur}) )
        return 0
    fi

    case "${prev}" in
        get|reset)
            # Suggest common HTTP status codes
            local status_codes="100 101 200 201 202 204 301 302 304 400 401 403 404 500 502 503"
            COMPREPLY=( $(compgen -W "${status_codes}" -- ${cur}) )
            return 0
            ;;
        set)
            # Suggest common HTTP status codes for setting custom descriptions
            local status_codes="100 101 200 201 202 204 301 302 304 400 401 403 404 500 502 503"
            COMPREPLY=( $(compgen -W "${status_codes}" -- ${cur}) )
            return 0
            ;;
        *)
            ;;
    esac
}

complete -F _http_completion python3 main.py
complete -F _http_completion python main.py
EOF

# Create zsh completion file
cat > completion/zsh/_http << 'EOF'
#compdef http

# Zsh completion for HTTP Status Code CLI Tool

_http() {
    local state line
    typeset -A opt_args

    _arguments -C \
        '1: :->command' \
        '*: :->args'

    case $state in
        command)
            _alternative 'commands:command:((
                get:"Get description for HTTP status code"
                set:"Set custom description for HTTP status code"
                reset:"Reset custom description for HTTP status code"
                reset-all:"Reset all custom descriptions"
                list:"List all HTTP status codes"
                interactive:"Start interactive mode"
                shell:"Start shell mode"
                help:"Show help message"
            ))'
            ;;
        args)
            case $line[1] in
                get|reset)
                    _values 'HTTP Status Codes' \
                        100:"Continue" \
                        101:"Switching Protocols" \
                        200:"OK" \
                        201:"Created" \
                        202:"Accepted" \
                        204:"No Content" \
                        301:"Moved Permanently" \
                        302:"Found" \
                        304:"Not Modified" \
                        400:"Bad Request" \
                        401:"Unauthorized" \
                        403:"Forbidden" \
                        404:"Not Found" \
                        500:"Internal Server Error" \
                        502:"Bad Gateway" \
                        503:"Service Unavailable"
                    ;;
                set)
                    _values 'HTTP Status Codes' \
                        100:"Continue" \
                        101:"Switching Protocols" \
                        200:"OK" \
                        201:"Created" \
                        202:"Accepted" \
                        204:"No Content" \
                        301:"Moved Permanently" \
                        302:"Found" \
                        304:"Not Modified" \
                        400:"Bad Request" \
                        401:"Unauthorized" \
                        403:"Forbidden" \
                        404:"Not Found" \
                        500:"Internal Server Error" \
                        502:"Bad Gateway" \
                        503:"Service Unavailable"
                    ;;
            esac
            ;;
    esac
}

_http "$@"
EOF

echo "Setup completed successfully!"
echo ""
echo "To use the tool:"
echo "  python3 main.py --help"
echo ""
echo "For shell completion:"
echo "  Bash: source completion/bash/http-completion.bash"
echo "  Zsh: source completion/zsh/_http"
echo ""
echo "To make completion permanent, add the source command to your shell's startup file."