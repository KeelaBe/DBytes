import os
import webbrowser


# RUNSERVER
def runserver():
    path = r".\Dbytes"
    os.chdir(path)
    os.system("python manage.py runserver")
