# PythonPackageTutorial

This repository is a step-by-step tutorial designed to show developers how to create a reusable Python package using modern tooling.

## Package Structure

Below is the structure of the Python package with descriptions for each file and directory:

```
WenntechTutorialPackage/   # The root package, this is what you will see during import
├── stats/                 # Statistical calculations module
│   ├── __init__.py        # Initializes the stats module
│   └── stats.py           # Contains functions for statistical analysis
|── __init__.py            # Initializes the root package
├── .gitignore             # Specifies which files to ignore in git
├── LICENSE                # The license under which this package is released
├── poetry.lock            # Lock file for specifying exact versions of dependencies
├── pyproject.toml         # Config file for build system and dependencies
├── README.md              # The file you are reading that provides package information
└── test_notebook.ipynb    # A Jupyter notebook for testing the package interactively
```

## Detailed File Descriptions
- stats/__init__.py: Signals to Python that this directory should be treated as a package. This can also be used to automatically load submodules or package-wide constants.
- stats/stats.py: The core of the stats package, containing functions such as mean, median, standard deviation, etc.
- .gitignore: Text file that tells Git which files or folders to ignore in a project.
- LICENSE: Contains the legal terms under which the software is released. Typically, for open-source software, a permissive license like MIT, BSD, or GPL is used.
-poetry.lock: A generated file that ensures consistent installation of package versions. This file should be committed to the repository to ensure all contributors and deployments are using the same package set.
- pyproject.toml: The configuration file for poetry, which is a tool for dependency management and packaging in Python.
- README.md: Provides an overview of the package, including how to install, configure, and use it.
- test_notebook.ipynb: A Jupyter notebook that can be used to demonstrate the package's capabilities in an interactive environment.

## Installation
To install the package, ensure you have Poetry installed and run:
```
poetry install
```
## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
