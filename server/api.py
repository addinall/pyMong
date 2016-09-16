## vim: set expandtab tabstop=4 shiftwidth=4 autoindent:
##
## File:   api.py
## Mark Addinall - September 2016 
##
## Synopsis: This is the basis for the server side API of a RESful
## web service writteny using Python and Flask.
## this will be tied to a MONGO document store and use JSON
## to communicate complex data.  day one, we are just chucking
## text around
##
## It will be tested against a Javascript framework client.
## Probably REACT or native javascript.

from flask import Flask, url_for
app = Flask(__name__)         ## get an instance of the Flask server

## this is slack just for now.  wrap it into an OOD shape on the weekend

@app.route('/')
def api_root():
    return 'You hit the root Page'

@app.route('/agriculture')
def api_aggies():
    return 'Here is a list of Farm vehicles at' + url_for('api_aggies')

@app.route('/agriculture/<vehicle_id>')
def api_aggie(vehicle_id):
    return 'You are inspecting ' + vehicle_id

if __name__ == '__main__':
    app.run()

