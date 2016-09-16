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
##
## we will implement the API as a re-usable object that can be
## imported, or run as a stand alone server.
##
## there are a few ways of doing this, either as a RESTful architecture,
## or by imposing a strict application only type of API.
## I will implement the RESTful model first and have a thing about it.

class API:
    """ This class communicates with the api.js on the client side, and with 
        database routines here on the server side.
    """


    from flask import Flask, url_for

    server_count = 0;               ## this is used if we have multiple instanciations
                                    ## of a server on the same machine.  not sure
                                    ## why we would want to do that, but as an experiment
                                    ## it is worthwhile.
    def __init__(self, id):
        self.id = id                ## keep track of WHICH server we want to communicate with.
                                    ## this may be handy for splitting geographic distribution
                                    ## of the network.
        API.server_count += 1   
        self.app = Flask(__name__)  ## get an instance of the Flask server
        self.app.run()              ## start the API default port 5000


    @self.app.route('/')
    def api_root():
        return 'You hit the root Page, no sense for an API'

    @self.app.route('/agriculture')
    def api_aggies():
        return 'Here is a list of Farm vehicles at' + url_for('api_aggies')

    @self.app.route('/agriculture/<vehicle_id>')
    def api_aggie(vehicle_id):
        return 'You are inspecting ' + vehicle_id

if __name__ == '__main__':
    server = API("Marky")

## ------------------   EOF API -----------------------



