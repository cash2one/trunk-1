#!/usr/bin/env python

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	return '<p>Your broser is %s</p>' % user_agent


if __name__ == "__main__":
	app.run(debug=True)
