from flask import Flask, render_template, request, redirect, jsonify
import json
import os

app = Flask(__name__)

# carregar tarefas do arquivo JSON
def load_tasks():
    if not os.path.exists('tasks.json'):
        return[]
    with open('tasks.json', 'r') as file:
        return json.load(file)
    
    # salvar tarefa no arquivo JSON
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methos=['POST'])
def add_task():
    tasks = request.form['task']
    if task:
        tasks = load_tasks()
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id <len(tasks):
       tasks.pop(task_id)
       save_tasks(tasks)
    return redirect('/')

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = not tasks[task_id]['done']
        save_tasks(tasks)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)