import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def teste_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
    }
    
    response = requests.post(f"{BASE_URL}/task",json=new_task_data)
    assert response.status_code == 200
    
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    
    tasks.append(response_json['id'])


def teste_get_task():
    response = requests.get(f"{BASE_URL}/task")
    assert response.status_code == 200
    response_json = response.json()
    
    assert "tasks" in response_json         
    assert "total_task" in response_json
    
    if response_json["tasks"]:
        tasks.append(response_json["tasks"][0]["id"])

def test_get_task():
    
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/task/{task_id}")
        assert response.status_code == 200
        
def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "completed": True,
            "description": "Nova Descrição",
            "title": "Título atualização"
        }
        
        response = requests.put(f"{BASE_URL}/task/{task_id}", json=payload)
        assert response.status_code == 200
        
        response_json = response.json()
        assert "message" in response_json    
        
        
        response = requests.put(f"{BASE_URL}/task/{task_id}", json=payload)
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['title'] == payload['title']  
        assert response_json['description'] == payload['description']
        assert response_json['completed'] == payload['completed']
        
        
def test_delete_task():

    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/task/{task_id}")
        assert response.status_code == 200
        
        response = requests.delete(f"{BASE_URL}/task/{task_id}")
        assert response.status_code == 404