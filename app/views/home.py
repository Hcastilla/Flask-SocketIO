from flask import render_template, request
from flask_socketio import emit, disconnect
from app import app, socketio


@app.route('/')
def index():
    return render_template('home.html')

#Metodos del socket
usuarios = []
points = []

@socketio.on('connect')
def connect():
	print('usuario Conectado')

@socketio.on('createId')
def crateId():
	emit('createId', len(usuarios))

@socketio.on('addUsuario')
def addUsuario(usuario):
	usuarios.append(usuario)
	emit('usuarios', usuarios, broadcast=True)

@socketio.on('updateUsuario')
def updateUsuario(user):
	for i, u in enumerate(usuarios, start=0):
		if u["id"] == user["id"]:
			usuarios[i] = user
			break
	emit('usuarios', usuarios, broadcast=True)

@socketio.on('drawPoint')
def drawPoint(p):
	points.append(p)
	emit('points', points, broadcast=True)

