from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Liste des tâches
tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task_name = request.form.get("task_name")
    priority = request.form.get("priority")
    tasks.append({"name": task_name, "priority": priority, "done": False})
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("index"))

@app.route("/toggle/<int:task_id>")
def toggle_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = not tasks[task_id]["done"]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)