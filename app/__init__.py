import os
import pkgutil
import importlib
import sys
from app.commands import CommandHandler
from app.commands import Command
from dotenv import load_dotenv
from app.plugins.menu import MenuCommand  # Import MenuCommand

class App:
    def __init__(self): # Constructor
        load_dotenv()
        self.settings = {}  # Initialize settings as an empty dictionary
        # Load all environment variables into settings
        for key, value in os.environ.items():
            self.settings[key] = value
        # Default to 'PRODUCTION' if 'ENVIRONMENT' not set
        self.settings.setdefault('ENVIRONMENT', 'TESTING')        
        self.command_handler = CommandHandler()

    def getEnvironmentVariable(self, envvar: str = 'ENVIRONMENT'):
        return self.settings[envvar]
    
    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_packages = [
            'app.plugins.addition',
            'app.plugins.subtraction',
            'app.plugins.multiplication',
            'app.plugins.division',
            'app.plugins.menu'
        ]
        for plugins_package in plugins_packages:
            for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
                if is_pkg:  # Ensure it's a package
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    for item_name in dir(plugin_module):
                        item = getattr(plugin_module, item_name)
                        try:
                            if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                                self.command_handler.register_command(plugin_name, item())
                        except TypeError:
                            continue  # If item is not a class or unrelated class, just ignore

    def start(self):
        # Register commands here
        self.load_plugins()
        print("Type 'exit' to exit.")
        while True:  # REPL (Read, Evaluate, Print, Loop)
            user_input = input(">>> ").strip()
            if user_input.lower() == 'menu':  # Check if user input is 'menu'
                MenuCommand().execute([])  # Execute MenuCommand
            else:
                self.command_handler.execute_command(user_input)
