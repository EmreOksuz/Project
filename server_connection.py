
import sys

from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

@app.route('/list')
def output():
	# serve index template
	return render_template('index.html')


@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['form']

						 
@app.route('/receiver', methods = ['POST'])
def worker():
	# read json + reply
	data = request.get_json()
	result = ''

	for item in data:
		# loop over every row
		result += str(item['make']) + '\n'

	return result

if __name__ == '__main__':
	# run!
	app.run()