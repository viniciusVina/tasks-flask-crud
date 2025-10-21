<<<<<<< HEAD
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
    return jsonify({"message": "Nova tarefa criada com sucesso!"}), 201
    
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


@app.route('/task/<int:id>',methods=["PUT"])

def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)
    if task == None:
            return jsonify("Não foi possivel encontrar"),404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']  
    task.completed = data['completed']
    print(task)
    return jsonify("Tarefa atualizda com sucesso"),200



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
=======
# Importa a classe Flask do módulo flask
from flask import Flask

# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# Define uma rota para a URL raiz ("/")
@app.route("/")
def hello_world():
    # Retorna uma resposta simples quando o usuário acessa a página inicial
    return("200")

# Define uma rota para a URL "/about"
@app.route("/about")
def sobre():
    # Retorna uma mensagem quando o usuário acessa a página "Sobre"
    return "Página Sobre Games"

# Verifica se o script está sendo executado localmente (e não importado como módulo)
if __name__ == "__main__":
    # Inicia o servidor em modo de depuração (debug=True)
>>>>>>> 958899be32cfccdf46fa87821ffe245bc9f9a0a5
    app.run(debug=True)
