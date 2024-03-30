# **Midterm Project.**

**1. Design Patterns Used:**

**a. Command Pattern:** Implemented in the Command and CommandHandler classes, providing a way to encapsulate requests as objects, allowing parameterization of clients with queues, and supporting undoable operations.

*Code snipped:*

```python
from abc import ABC, abstractmethod
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
class CommandHandler:
    def __init__(self):
        self.commands = {}
    def register_command(self, command_name: str, command_class):
        self.commands[command_name] = command_class
    def execute_command(self, command_name: str):
        command = self.create_command(command_name)
        if command:
            command.execute()
```
**b. Factory Pattern:** Utilized in the AppFactory class to dynamically create instances of command objects based on specified packages.

*Code snipped:*
```python
import pkgutil
import importlib
class AppFactory:
    @staticmethod
    def create_command_objects():
        commands = {}
        plugins_packages = [
            'app.plugins.addition',
            'app.plugins.subtraction',
            'app.plugins.multiplication',
            'app.plugins.division'
        ]
        for plugins_package in plugins_packages:
            for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
                if is_pkg:  
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    for item_name in dir(plugin_module):
                        item = getattr(plugin_module, item_name)
                        try:
                            if issubclass(item, Command):  
                                commands[plugin_name] = item
                        except TypeError:
                            continue
        return commands ```
```

*c. Facade Pattern:* Applied in the AppFacade class to provide a simplified interface (perform_data_manipulation()) to complex operations (Pandas data manipulation).

*Code snipped:*

```python
class AppFacade:
    @staticmethod
    def perform_data_manipulation(data):
        # Perform complex Pandas data manipulations here
        # This could involve operations like filtering, transformation, aggregation, etc.
        pass
    ```

**2. Environment Variables Usage:**
Environment variables are used for settings such as defining the environment (ENVIRONMENT), which defaults to 'TESTING'. These variables are loaded from a .env file using python-dotenv.

*Example snippet:*
```python
def getEnvironmentVariable(self, envvar: str = 'ENVIRONMENT'):
   return self.settings[envvar]
```

**3. Logging:**
Logging is configured using Python's built-in logging module. Log messages are written to a file (app.log) located in a directory named logs. The logging level is set to INFO, and a specific format is defined for the log messages.

*Example snippet:*
```python
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
Try/Except and Exceptions:
Exceptions are used for error handling in various parts of the code. For example, in the DivisionCommand class, a try/except block catches a ZeroDivisionError if the divisor is zero, and an error message is printed.

*Example snippet:*
```python
python
Copy code
try:
    return a / b
except ZeroDivisionError:
    print("Division by zero error")
```

This demonstrates the "Look Before You Leap" (LBYL) approach, where potential errors are anticipated and handled explicitly.
On the other hand, the "Easier to Ask for Forgiveness than Permission" (EAFP) approach is used in various parts of the code, where actions are attempted first, and exceptions are caught and handled if they occur.


**4. Working:**
a. first set up the github repository and then link it to your wsl-2 IDE.
    
```php
git remote add origin <paste your github repository ssh link>
git add .
git commit -m "add your commit statement"
git push orign master 
ssh-keygen -t rsa -b 2048  (this command will create a ssh key)
vi ~/.ssh/id_rsa.pub (This will open the file containing th essh key. Paste this key in the github profile ssh key section)
```
    

b. Setup the python environment

```python
sudo apt update -y
sudo apt install python3-pip
pip3 --version
(the above commands will update the wsl-2 and installs the python-3 packages)
pip3 install virtualenv (This command will install virtual environment)
virtualenv venv (This command will create a virtual environment venu)
source ./venv/bin/activate (This command will activate the virtual environment.)
pip3 install -r requirments.txt (This command will install all the required packages)
pytest (Runs the tests)
pytest --pylint  (Runs tests with pylint static code analysis)
pytest --pylint --cov (Runs tests, pylint, and coverage to check if you have all your code tested.)
python3 main.py 
```

c. The above command will start the app and asks you to enter the prompt menu to display the menu. From there you can select the option you want to interact with and after that command operation is done it will again as you to enter menu again so that you can choose the option to interact with. This goes on till you select exit from the menu.

** Video for the Calculator app demo** 

[![Video](https://drive.google.com/file/d/1YozkMscs2g5La1fV8Mbo9scNzbT8_wxy/view?usp=drive_link.jpg)](https://drive.google.com/file/d/1YozkMscs2g5La1fV8Mbo9scNzbT8_wxy/view?usp=drive_link)