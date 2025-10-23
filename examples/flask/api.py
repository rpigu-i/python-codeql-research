import re
import os
import subprocess
from flask import Flask, request
from django.db import connection, models
from django.db.models.expressions import RawSQL

app = Flask(__name__)


# A badly designed Admin API
class User(models.Model):
    pass

@app.route("/executecode")
def code_execution():
    """
    Badly designed endppoint for 
    executing code
    """
    code = request.args.get("code")
    exec(execute)
    eval(execute)

@app.route("/filelist")
def file_list():
    """
    API to list files
    """
    files = request.args.get('files', '')
    os.system("ls " + files) # $result=BAD


@app.route("/filelistadvanced")
def filelist_advanced():
    """
    Advanced API to list files
    """
    files = request.args.get('files', '')
    subprocess.Popen("ls al " + files, shell=True)


@app.route("/users/<user>")
def get_user():
    user = request.args.get("user")
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username = '%s'" % user)
