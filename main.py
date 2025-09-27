from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt


def main():
    console = Console()

    # Create a colorful hello world message
    hello_text = Text("Hello, World! ", style="bold blue")
    hello_text.append("Welcome to ", style="green")
    hello_text.append("hello-world-qwen", style="bold magenta")
    console.print(hello_text)

    # Get user's name
    name = Prompt.ask("[bold yellow]What's your name?[/bold yellow]")

    # Display personalized greeting
    greeting = Text(f"Nice to meet you, {name}!", style="bold cyan")
    console.print(greeting)


if __name__ == "__main__":
    main()
