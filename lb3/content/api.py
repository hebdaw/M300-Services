#!/usr/bin/python
# -*- coding: utf-8 -*-
# Product Service

# Import framework

from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app

app = Flask(__name__)
api = Api(app)


class Product(Resource):

    def get(self):
        return {'products': [   # returns JSON
            'Mainframe',
            'TV',
            'Keyboard',
            'Laptop',
            'Server',
            'HDD',
            'Printer',
            'Monitor',
            'Power Supply',
            ]}


# Create routes

api.add_resource(Product, '/')

# Run the application

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

# A real API would output much more information and details but for an example this will do.