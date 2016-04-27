from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector('friendsdb')

@app.route('/')
def index():
    friends = mysql.fetch("SELECT * FROM friends")
    return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(request.form['first_name'], request.form['last_name'], request.form['occupation'])
    print query
    mysql.run_mysql_query(query)
    return redirect('/')

@app.route('/delete/<id>', methods=['POST'])
def destroy(id):
	query = "DELETE FROM friends WHERE id = '{}'".format(id)
	print query
	mysql.run_mysql_query(query)
	return redirect('/')

@app.route('/editpage/<id>', methods=['POST'])
def editpage(id):
    friends = mysql.fetch("SELECT * FROM friends WHERE id = '{}'".format(id))
    return render_template('edit.html', friends=friends)

@app.route('/edit/<id>', methods=['POST'])
def update(id):
    update = "UPDATE friends SET first_name = '{}', last_name = '{}', occupation = '{}' WHERE id = '{}'".format(request.form['first_name'], request.form['last_name'], request.form['occupation'], id)
    print update
    mysql.run_mysql_query(update)
    return redirect('/')

app.run(debug=True)

