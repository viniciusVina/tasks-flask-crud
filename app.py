from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []  # lista de tarefas

task_id_control = 1

@app.route('/task', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    print(data)
    new_task = Task(id=task_id_control,title=data['title'],description=data.get("description"))
    task_id_control += 1
    tasks.append(new_task)
    return jsonify({"message": "Nova tarefa criada com sucesso!","id":new_task.id}), 200
    
    return 'Test'



@app.route('/task',methods=['GET'])
def get_tasks():
    
    task_list = [task.to_dict() for task in tasks]
    
    output ={
        "tasks": task_list,
        "total_task": len(task_list)
    }
    return jsonify(output)


@app.route('/task/<int:id>',methods=['GET'])

def read_tasks(id):
    
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    
    return jsonify("Não foi possivel encontrar"),404
    

##rota com conversão de tipo
@app.route('/user/<int:user_id>')
def show_user(user_id):
    print(user_id)
    print(type(user_id))
    return "%s" %user_id


@app.route('/task/<int:id>', methods=["PUT"])
def update_task(id):
    task = next((t for t in tasks if t.id == id), None)

    if task is None:
        return jsonify({"message": "Tarefa não encontrada"}), 404

    data = request.get_json()

    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.completed = data.get('completed', task.completed)

    # Retorna objeto atualizado no padrão esperado pelo teste
    return jsonify({
        "message": "Tarefa atualizada com sucesso",
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }), 200



@app.route('/task/<int:id>',methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            print(t)
            break
    if task == None:
            return jsonify("Não foi possivel encontrar"),404
    
    tasks.remove(task)
    return jsonify("Tarefa deletada com sucesso"),200



if __name__ == "__main__":
    app.run(debug=True)
