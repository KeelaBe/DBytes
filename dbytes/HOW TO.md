# How To: DBYTES POS
## Running Locally

1. First you will need to download and install python to your computer. [Download Python | Python.org](https://www.python.org/downloads/)
2. After downloading Python, you will need to download and install a Python package for a backend framework called Django. To do this open cmd (or terminal on mac) and type: pip install django
3. Download/pull the DBytes repository to your local machine.
4. After download the DBytes repository, open cmd (or terminal on mac) and navigate to where it downloaded using 'cd' shell command. An easier shortcut to do with on widows is to navigate to where the file is located in file explorer and type 'cmd' where the folder path is. This will open a cmd window in that path. EX:
![](https://i.imgur.com/FowXjt6.png)
![](https://i.imgur.com/LHxux0f.png)
![](https://i.imgur.com/GBqXqtW.png)
5. Type 'cd dbtytes' to change into the dbytes sub folder.
![](https://i.imgur.com/h3VkzrN.png)
6. Type 'python manage.py runserver' into cmd this will locally start a server running the application. Depending on what version of python you have and OS the command may be different. Try 'py manage.py runserver' or 'py3 manage.py runserver' or 'python3 manage.py runserver'.
![](https://i.imgur.com/2G01BSk.png)
7. That last command should spit out some information saying about the server starting and what where the server is running at. The default is http://127.0.0.1:8000/ . Either control click the URL in the terminal or enter that ip into a browser and it should take you to the application.
## File Structure
Using Django as the backend, the html and css files need to be arranged in a certain way. 

The html files are located in: [DBytes](https://github.com/KeelaBe/DBytes)/[dbytes](https://github.com/KeelaBe/DBytes/tree/main/dbytes)/[main](https://github.com/KeelaBe/DBytes/tree/main/dbytes/main)/[templates](https://github.com/KeelaBe/DBytes/tree/main/dbytes/main/templates)/main

The CSS file is loacated in: [DBytes](https://github.com/KeelaBe/DBytes)/[dbytes](https://github.com/KeelaBe/DBytes/tree/main/dbytes)/[main](https://github.com/KeelaBe/DBytes/tree/main/dbytes/main)/[static](https://github.com/KeelaBe/DBytes/tree/main/dbytes/main/static)/css

The code for the backend table data models are located at (not important unless wanted to add more tables or change table structure): [DBytes](https://github.com/KeelaBe/DBytes)/[dbytes](https://github.com/KeelaBe/DBytes/tree/main/dbytes)/[main](https://github.com/KeelaBe/DBytes/tree/main/dbytes/main)/**models.py** 

This is the code that handles the API (passes data in html forms to backend SQLite database using a POST http request):[DBytes](https://github.com/KeelaBe/DBytes)/[dbytes](https://github.com/KeelaBe/DBytes/tree/main/dbytes)/[main](https://github.com/KeelaBe/DBytes/tree/main/dbytes/main)/**views.py**

## Jinja 
You may see some Jinja in the HTML code. Jinja usually is formated in curly braces EX:{% for order in orders %}. It makes HTML more dynamic and allows us to pass data into HTML using query from the SQLite DB.