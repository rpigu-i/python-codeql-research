import re
import os
import subprocess
from flask import Flask, request

app = Flask(__name__)


# A badly designed Admin API
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

