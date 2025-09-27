# hello-world-qwen

A simple Python project that displays a colorful "Hello, World!" message using the Rich library and prompts for the user's name to create a personalized greeting.

## Features

- Colorful "Hello, World!" message using Rich
- Prompts for user's name
- Personalized greeting with Rich styling
- Easy to run and extend

## Installation

Make sure you have Python 3.12+ and uv installed on your system.

```bash
# Clone the repository
git clone https://github.com/your-username/hello-world-qwen.git

# Navigate to the project directory
cd hello-world-qwen

# Install dependencies
uv sync

# Run the application
uv run python main.py
```

## Installing the Qwen CLI with Node / npm

If a JavaScript/Node version of the Qwen CLI is published to the npm registry you can install it with npm. These instructions assume the package name is `qwen-cli`; if the actual package name differs (for example `qwen` or `@org/qwen-cli`) substitute that name in the commands below.

Prerequisite: Node.js and npm must be installed.

### Windows (cmd.exe)

```cmd
:: Install globally
npm install -g qwen-cli

:: Run the CLI
qwen --help
```

### macOS (bash / zsh)

```bash
# Install globally (may require sudo depending on your setup)
sudo npm install -g qwen-cli

# Or install without sudo to your user directory (recommended when possible)
npm install --location=global qwen-cli

# Run the CLI
qwen --help
```

### Linux (bash)

```bash
# Install globally (may require sudo)
sudo npm install -g qwen-cli

# Or install for the current user (no sudo)
npm install --location=global qwen-cli

# Run the CLI
qwen --help
```

### Run without installing (npx)

```bash
# Use npx to run the package without a global install
npx qwen-cli --help
```

If the `qwen` command is not found after a global install, check the global npm binaries path with:

```bash
npm bin -g
```

Then ensure that directory is on your PATH (Windows: typically %APPDATA%\npm, macOS/Linux: the output of `npm bin -g`).

## Running Tests

To run the project tests:

```bash
uv run pytest
```

## Project Structure

```text
.
├── main.py                 # Main application script
├── pyproject.toml          # Project configuration
├── tests/                  # Test directory
│   └── test_main.py        # Tests for main functionality
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
