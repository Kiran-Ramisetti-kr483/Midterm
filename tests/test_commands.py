from io import StringIO
import pytest
from app import App
from app.plugins.division import DivisionCommand
from app.plugins.addition import AdditionCommand
from app.plugins.multiplication import MultiplicationCommand
from app.plugins.subtraction import SubtractionCommand
from app.plugins.Menu import MenuCommand
from app.commands import Command, CommandHandler
from unittest.mock import MagicMock

class MockCommand(Command):
    def execute(self):
        pass

def test_app_add_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'add' command."""
    inputs = iter(['add 2 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()

def test_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'menu' command."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('sys.stdin', StringIO('\n'.join(inputs)))
    command = MenuCommand()
    command.execute([])
    captured = capfd.readouterr()
    assert captured.out.strip() == "Menu"

def test_command_handler_register_command():
    """Test registering command in command handler."""
    handler = CommandHandler()
    mock_command = MockCommand()
    handler.register_command('mock', mock_command)
    assert handler.commands['mock'] == mock_command

def test_command_handler_execute_command():
    """Test executing command in command handler."""
    handler = CommandHandler()
    mock_command = MagicMock()
    handler.register_command('mock', mock_command)
    handler.execute_command('mock')
    mock_command.execute.assert_called_once()

def test_command_handler_execute_command_no_args():
    """Test executing command in command handler with no args."""
    handler = CommandHandler()
    mock_command = MagicMock()
    handler.register_command('mock', mock_command)
    handler.execute_command('mock')
    mock_command.execute.assert_called_once()

def test_addition_command_no_args(capfd):
    """Test that addition command handles no arguments."""
    command = AdditionCommand()
    command.execute([])
    captured = capfd.readouterr()
    assert captured.out.strip() == "nothing to add"

def test_addition_command_with_args(capfd):
    """Test that addition command handles arguments."""
    command = AdditionCommand()
    command.execute(["2", "3"])
    captured = capfd.readouterr()
    assert captured.out.strip() == "5.0"

def test_division_command_no_args(capfd):
    """Test that division command handles no arguments."""
    command = DivisionCommand()
    command.execute([])
    captured = capfd.readouterr()
    assert captured.out.strip() == "nothing to Divide"

def test_division_command_division_by_zero(capfd):
    """Test that division command handles division by zero."""
    command = DivisionCommand()
    command.execute(["5", "0"])
    captured = capfd.readouterr()
    assert captured.out.strip() == "division by zero error"

def test_division_command_with_args(capfd):
    """Test that division command handles arguments."""
    command = DivisionCommand()
    command.execute(["10", "2"])
    captured = capfd.readouterr()
    assert captured.out.strip() == "Division result : 5.0"



def test_app_multiplication_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'multiply' command."""
    inputs = iter(['multiply 2 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()

def test_multiplication_command_no_args(capfd):
    """Test that multiplication command handles no arguments."""
    command = MultiplicationCommand()
    command.execute([])
    captured = capfd.readouterr()
    assert captured.out.strip() == "nothing to multiply"

def test_multiplication_command_with_args(capfd):
    """Test that multiplication command handles arguments."""
    command = MultiplicationCommand()
    command.execute(["2", "3"])
    captured = capfd.readouterr()
    assert captured.out.strip() == "multiplication result : 6.0"

def test_app_subtraction_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'subtract' command."""
    inputs = iter(['subtract 5 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()

def test_subtraction_command_no_args(capfd):
    """Test that subtraction command handles no arguments."""
    command = SubtractionCommand()
    command.execute([])
    captured = capfd.readouterr()
    assert captured.out.strip() == "nothing to subtract"

def test_subtraction_command_with_args(capfd):
    """Test that subtraction command handles arguments."""
    command = SubtractionCommand()
    command.execute(["5", "3"])
    captured = capfd.readouterr()
    assert captured.out.strip() == "Subtraction result : 2.0"