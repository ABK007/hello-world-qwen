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

## Running Tests

To run the project tests:

```bash
uv run pytest
```

## Project Structure

```
.
├── main.py                 # Main application script
├── pyproject.toml          # Project configuration
├── tests/                  # Test directory
│   └── test_main.py        # Tests for main functionality
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)