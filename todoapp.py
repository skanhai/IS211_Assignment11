from flask import Flask, render_template, redirect, url_for, request
import os
import pickle

app = Flask(__name__)


template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
app = Flask(__name__, template_folder=template_dir)


file_path = 'todo_list.pkl'



def save_list(todo_list):
    with open(file_path, 'wb') as file:
        pickle.dump(todo_list, file)



def load_list():
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    else:
        return []



todo_list = load_list()



@app.route('/')
def index():
    return render_template('todo_list.html', todo_list=todo_list)



@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']


    todo_list.append({'task': task, 'email': email, 'priority': priority})
    save_list(todo_list)
    return redirect(url_for('index'))



@app.route('/clear')
def clear():
    global todo_list
    todo_list = []
    save_list(todo_list)
    return redirect(url_for('index'))



@app.route('/save_list', methods=['POST'])
def save_list_route():
    save_list(todo_list)
    return redirect(url_for('index'))



@app.route('/delete/<int:index>', methods=['POST'])
def delete_item(index):
    if index < len(todo_list):
        del todo_list[index]
        save_list(todo_list)
    return redirect(url_for('index'))


if __name__ == '__main__':

    app.run(debug=True)
