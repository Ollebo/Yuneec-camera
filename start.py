#
#
#
# File to start
#
# Lissen for events from the que
#!/usr/bin/env python
import time
import time
import json
from flask import Flask, request, render_template, url_for, redirect
from functions.default import *


app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def start():
	if request.method == 'POST':
		return "Move along nothing to see"
	else:
		return "Get along nothing to see"

@app.route("/cgi-bin/cgi", methods = ['GET'])
def commands():
	#we get a command to act on
	CMD = request.args.get('CMD')
	print(request.args)
	return commandSelect(CMD,request.args)