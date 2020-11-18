## About The Project

Interacts with the Guild Wars 2 market data API to evaluate and output projected profits for T6 material flipping.

This project also serves as an example for how a basic python project should be structured.

### Getting Setup
* From terminal, navigate to the folder on your machine (cd ...) where you would like for this project to live.
* Next, clone this project to your machine using "git clone https://github.com/pauldevnull/GWMarketData.git"
* Navigate to the cloned project ("cd GW-Market-Data")
* Finally, install dependencies for this project by running "pip3 install -r requirements.txt"
* Run the project with "python gw_market_data.py"

### Stuff To Note
* The "requirements.txt" file can be used to store all dependencies and their versions for the project for easy installation. This allows anyone (including yourself) to easily clone the project and get it up and running without having to figure out each of the dependencies.
* This project uses examples of classses (MaterialEvaluator and MaterialCollector). It isn't exactly necessary here, but serves as a good example of how to do this. A class is a noun (i.e. a "thing") and can have one or more instances created. It also helps to organize code.
* The "__init__.py" file is needed inside folders to allow importing of classes within the project. This file can usually just be empty but is needed to tell python that the directory should be treated as a package.
* The entry point of the project is a file with the same name as the project, except all lowercase ("gw_market_data.py"). This file contains a main() method which is called at the end of the file.
* The main() method serves as the entry point to the code and contains only high-level logic that should describe the general flow of the script

### Naming Conventions
* Project names should be all lowercase OR kabobcase ("GW-Market-Data")
* Files and folder/package names should be snakecase ("material_collector")
* Class names should be camelcase ("MaterialEvaluator")
