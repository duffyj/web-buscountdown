#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      duffyj
#
# Created:     01/09/2013
# Copyright:   (c) duffyj 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys

from flask import Flask
from flask import render_template
from app import app

from app.busdatareader import BusDataReader

dbo = BusDataReader()



@app.route('/')
def hello_world():
    return 'Hello World 3'

@app.route('/<user_id>')
@app.route('/<user_id>/<username>')
def show(user_id = 'no_id', username = 'no_name'):
    return "User " + user_id + " " + "username" + username + "."

def main():
    sys.stdout.write("start test");

@app.route('/')
@app.route('/bus/<username>')
def showbus(username = 'no_name'):
    filtered_results = dbo.get_data()
    return render_template("bus_result.html",
        title = 'bus',
        results = filtered_results,
        user = username)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id = 1):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


if __name__ == '__main__':
    main()
  #  sys.stdout.write(app.test_request_context().url_for('index'));
    app.run(debug=True)

   # with app.test_request_context():
   #     print url_for('index');