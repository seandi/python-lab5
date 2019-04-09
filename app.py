from flask import Flask, render_template, redirect, url_for, request
import tododb

app = Flask(__name__)
task_list = []


@app.route('/')
def home():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    task_list.clear()
    for task in tododb.get_tasks():
        task_list.append(task)
    return render_template('index.html', task_list=task_list)


@app.route('/add_task', methods=['POST', 'GET'])
def add_task():
    task = request.form['task_description']
    tododb.add_task(task)
    return redirect(url_for('index'))


@app.route('/delete_task/<id_task>')
def delete_task(id_task):
    tododb.delete_task(id_task)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
