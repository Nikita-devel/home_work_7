[Main page](https://github.com/Nikita-devel) | [Python Core Page](https://github.com/Nikita-devel/Python_Core)

# Clean Folder

## Project Description

The Clean Folder project transforms a Python script for folder parsing into a Python package and a console script <br>
that can be executed from any location within the system using the command `clean-folder`. The project structure <br>
should be organized as follows:<br>
├── clean_folder <br>
│ ├── clean_folder<br>
│ │ ├── clean.py<br>
│ │ └── init.py<br>
│ └── setup.py<br>

The contents of the `clean_folder/clean_folder/clean.py` file should encapsulate the folder parsing functionality <br>
from previous assignments. Your primary task is to create the `clean_folder/setup.py` file, allowing Python's <br>
built-in tools to install this package, and enabling the operating system to utilize this package as a console command.<br>

## Key Features

- Transformation of folder parsing script into a Python package.
- Integration of a console script (`clean-folder`) accessible system-wide.
- Organized project structure with a clear separation of concerns.

## Installation

Ensure Python is installed on your system. Navigate to the project's root directory and execute the following 
command to install the package:

## Usage
Once installed, you can use the clean-folder command from any location within the system to parse and clean folders.<br>
The detailed usage instructions for the clean-folder command should be provided within the clean_folder/clean_folder/clean.py script.<br>

  ```bash
  python setup.py install
