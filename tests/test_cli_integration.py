import subprocess
import sys
import pytest


class TestCLIIntegration:
    """Test CLI application integrating with calculator module"""

    def run_cli(self, *args):
        """Helper method to run CLI and capture output"""
        cmd = [sys.executable, "src/cli.py"] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
        return result

    def test_cli_add_integration(self):
        """Test CLI can perform addition"""
        result = self.run_cli("add", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "8"

    def test_cli_subtract_integration(self):
        """Test CLI can perform subtraction"""
        result = self.run_cli("subtract", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "2"

    # <<< REPLACE THE OLD METHOD WITH THIS ONE >>>
    def test_cli_subtract_missing_operand_error(self):
        """Test CLI handles missing operand for subtraction gracefully"""
        # Call subtract with only one operand; CLI should exit with non-zero and print an error
        result = self.run_cli("subtract", "5")
        assert result.returncode == 1
        # CLI prints a proper error message for missing operand
        assert result.stdout.strip().startswith(
            "Error: Subtract operation requires two numbers"
        )
