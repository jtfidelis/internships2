from flask import Flask, render_template, request, redirect, url_for
from data import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/internships/<program_type>')
def internships(program_type):
    programs_list = read_programs_by_program_type(program_type)
    return render_template("internship.html", program_type=program_type, programs=programs_list)

@app.route('/internships/<int:program_id>')
def program(program_id):
    program = read_program_by_program_id(program_id)
    return render_template("program.html",program=program)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/processed', methods=['POST'])
def processing():
    program_data = {
        "program_type": request.form['program_type'],
        "program_name": request.form['program_name'],
        "salary": request.form['program_salary'],
        "duration": request.form['program_duration'],
        "description": request.form['program_desc'],
        "url": request.form['program_url']
    }
    insert_program(program_data)
    return redirect(url_for('internships', program_type=request.form['program_type']))

@app.route('/modify', methods=['post'])
def modify():
    if request.form["modify"] == "edit":
        program_id = request.form["program_id"]
        program = read_program_by_program_id(program_id)
        return render_template('update.html', program=program)
    elif request.form["modify"] == "delete":
        program_id = request.form["program_id"]
        program = read_program_by_program_id(program_id)
        delete_program(program_id)
        return redirect(url_for("internships", program_type=program["program_type"]))

@app.route('/update', methods=['post'])
def update():
    program_data = {
        "program_id" : request.form["program_id"],
        "program_type": request.form['program_type'],
        "program_name": request.form['program_name'],
        "salary": request.form['program_salary'],
        "duration": request.form['program_duration'],
        "description": request.form['program_desc'],
        "url": request.form['program_url']
    }
    update_program(program_data)
    return redirect(url_for('program',program_id = request.form['program_id']))
    
if __name__ == "__main__":
    app.run(debug=True)