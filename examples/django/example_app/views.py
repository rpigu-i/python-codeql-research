from django.db import connection
from django.shortcuts import render

def my_view(request):
    # Intentional error for debugging example
    data = {"name": "Django"}
    # Attempting to access a non-existent key will cause an error
    print(data["age"]) 
    return render(request, 'myapp/index.html', {'data': data})


def show_user(request, username):
   with connection.cursor() as cursor:
       cursor.execute("SELECT * FROM users WHERE username = '%s'" % username)
