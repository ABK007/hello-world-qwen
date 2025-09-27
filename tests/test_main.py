"""Tests for the main module."""
import io
import sys
import os
from unittest.mock import patch

# Add the project root to the path so we can import main
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import main  # Import main after adding the path


def test_main_function(capsys):
    """Test that the main function runs without errors."""
    # Mock user input to avoid waiting for input during tests
    with patch('rich.prompt.Prompt.ask', return_value="Test User"):
        main.main()
    
    # Capture output to verify it ran correctly
    captured = capsys.readouterr()
    
    # Check that something was printed
    assert "Hello, World!" in captured.out
    assert "hello-world-qwen" in captured.out
    assert "Test User" in captured.out


def test_main_runs_without_error():
    """Test that main function doesn't raise any exceptions."""
    try:
        # Mock user input to avoid waiting for input during tests
        with patch('rich.prompt.Prompt.ask', return_value="Test User"):
            main.main()
        # If no exception was raised, the test passes
        assert True
    except Exception as e:
        # If an exception was raised, the test fails
        assert False, f"Main function raised an exception: {e}"