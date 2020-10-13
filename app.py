from flask import Flask, request, jsonify
import json

app = Flask(__name__)

personas = []

@app.route('/', methods = ['GET'])
def inicio():
    return "Bienvenido"

@app.route('/agregar', methods = ['POST'])
def agregarPersona():
    cuerpo = request.get_json()
    nombre = cuerpo['nombre']
    edad = cuerpo['edad']
    persona = {'nombre':nombre,'edad':edad}
    global personas
    personas.append(persona)
    return jsonify({"mensaje": "Agregado Correctamente"})

@app.route('/obtener', methods = ['GET'])
def obtenerPersonas():
    return jsonify(personas)

@app.route('/modificar', methods = ['POST'])
def modificarPersona():
    cuerpo = request.get_json()
    nombre = cuerpo['nombre']
    new_nombre = cuerpo['new_nombre']
    new_edad = cuerpo['new_edad']
    global personas

    for i in range(len(personas)):
        if personas[i]['nombre'] == nombre:
            personas[i]['nombre'] = new_nombre
            personas[i]['edad'] = new_edad
    return jsonify({"mensaje": "Modificado Correctamente"})

@app.route('/eliminar',methods=['POST'])
def eliminarPersona():
    cuerpo = request.get_json()
    nombre = cuerpo['nombre']
    global personas
    
    for i in range(len(personas)):
        if personas[i]['nombre'] == nombre:
            personas.pop(i)
    return jsonify({"mensaje":"Eliminado correctamente"})

if __name__ == "__main__":
    app.run(port = 4000, host = '0.0.0.0', debug = True)