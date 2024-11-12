import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import create_app, db
from app.models import Tarefa
from datetime import datetime

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Use an in-memory database for tests

    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create tables for the test
        yield client
        with app.app_context():
            db.drop_all()  # Clean up tables after test

def test_criar_tarefa(client):
    response = client.post("/tarefas/create", data={"titulo": "Test Tarefa", "descricao": "Descrição de teste"})
    assert response.status_code == 302  # Redirect after creation
    tarefa = Tarefa.query.filter_by(titulo="Test Tarefa").first()
    assert tarefa is not None
    assert tarefa.descricao == "Descrição de teste"
    assert tarefa.feito is False
    assert tarefa.data_conclusao is None

def test_atualiza_tarefa_marca_completa(client):
    tarefa = Tarefa(titulo="Tarefa incompleta", descricao="Descrição incompleta")
    db.session.add(tarefa)
    db.session.commit()

    # Mark as completed
    response = client.post(f"/tarefas/update/{tarefa.id}", data={"titulo": "Tarefa incompleta", "descricao": "Descrição incompleta", "feito": "on"})
    assert response.status_code == 302  # Redirect after update

    tarefa = Tarefa.query.get(tarefa.id)
    assert tarefa.feito is True
    assert tarefa.data_conclusao is not None
    assert isinstance(tarefa.data_conclusao, datetime)

def test_atualiza_tarefa_desmarca_completa(client):
    tarefa = Tarefa(titulo="Completed Task", descricao="Descrição completa", feito=True, data_conclusao=datetime.utcnow())
    db.session.add(tarefa)
    db.session.commit()

    # Mark as incomplete
    response = client.post(f"/tarefas/update/{tarefa.id}", data={"titulo": "Tarefa completa", "descricao": "Descrição completa"})
    assert response.status_code == 302  # Redirect after update

    tarefa = Tarefa.query.get(tarefa.id)
    assert tarefa.feito is False
    assert tarefa.data_conclusao is None

def test_remover_tarefa(client):
    tarefa = Tarefa(titulo="Tarefa deletada", descricao="Descrição da tarefa")
    db.session.add(tarefa)
    db.session.commit()

    response = client.post(f"/tarefas/delete/{tarefa.id}")
    assert response.status_code == 302  # Redirect after delete

    tarefa = Tarefa.query.get(tarefa.id)
    assert tarefa is None
