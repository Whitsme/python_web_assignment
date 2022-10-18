"""
Aaron Whitaker
10/7/2022
CRN: 10235
CIS 226: Advanced Python Programming
Aprox Time: 5 hours
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # points flask to the home page
    return render_template(
        'home.html',
        title='home',
        )

@app.route('/contact/')
def contact():
    # points flask to the contact page
    return render_template(
        'contact.html',
        title='contact',
    )

@app.route('/projects/')
def projects():
    # points flask to the projects page
    return render_template(
        'projects.html',
        title='projects',
    )

"""
Design: I'm also taking David Barns Web Application Programming course, so I've designed several web pages so far this semester and I intended to mainly focus on Flask.
Develop: Flask is surprisingly similar to Django. I was able to use what I had learned in Django easily for this assignment. 
Test: I tested the html and css pages that I copied over from a Django project to test in Flask. After some minor syntax modifications they operated as expected.
    I also tested adding in static images and css files to the project. I also tested the routes and the templates. I spun up a local server [export FLASK_DEBUG=1] + [flask run] 
    and tested the pages, drop downs, and links. 
Docs: This is a basic Flask website application. The above points Flask to each of the webpages in the templates folder. The CSS and images are in the static folder. 
    You can edit the webpages by changing the html and css files. Basic function of the website to display the Dalle II images with links to 'contact' and 'favorite' pages.
"""