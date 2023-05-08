import os
import webbrowser


# RUNSERVER
def runserver():
    path = r".\dbytes"
    os.chdir(path)
    os.system("python manage.py runserver")


runserver()