from datetime import datetime

from flask import Blueprint, request, render_template, redirect, url_for, flash
from .models import Tarefa, db

tasks_bp = Blueprint("tarefas", __name__)

@tasks_bp.route("/")
def index():
    return redirect(url_for("tarefas.ver_tarefas"))

@tasks_bp.route("/tarefas", methods=["GET"])
def ver_tarefas():
    tarefas = Tarefa.query.all()
    return render_template("tarefas.html", tarefas=tarefas)

@tasks_bp.route("/tarefas/create", methods=["POST"])
def criar_tarefa():
    titulo = request.form.get("titulo")
    descricao = request.form.get("descricao")
    nova_tarefa = Tarefa(titulo=titulo, descricao=descricao)
    db.session.add(nova_tarefa)
    db.session.commit()
    flash("Tarefa criada com sucesso!")
    return redirect(url_for("tarefas.ver_tarefas"))

@tasks_bp.route("/tarefas/update/<int:id>", methods=["POST"])
def atualiza_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    tarefa.titulo = request.form.get("titulo")
    tarefa.descricao = request.form.get("descricao")
    feito = request.form.get("feito") == "on"
    if feito and not tarefa.feito:  # Only update if it's being marked as done now
        tarefa.data_conclusao = datetime.utcnow()
    elif not feito:
        tarefa.data_conclusao = None

    tarefa.feito = feito
    db.session.commit()
    flash("Tarefa atualizada com sucesso!")
    return redirect(url_for("tarefas.ver_tarefas"))

@tasks_bp.route("/tarefas/delete/<int:id>", methods=["POST"])
def remover_tarefa(id):
    task = Tarefa.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    flash("Tarefa removida com sucesso!")
    return redirect(url_for("tarefas.ver_tarefas"))

@tasks_bp.errorhandler(404)
def page_not_found(e):
    return redirect(url_for("tarefas.ver_tarefas"))
