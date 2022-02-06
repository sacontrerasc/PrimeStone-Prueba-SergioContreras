import db
from Persona import Persona
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
@app.route('/get-prime-numbers',methods=['GET'])
def primos():
  numerosPrimos = 'Los numeros primos son: '
  toNumber = int(request.args.get('toNumber'))
  for n in range(2, toNumber):
    esPrimo = True
    for y in range(2, n):
        if n % y == 0:
            esPrimo = False
    if esPrimo:
        numerosPrimos=numerosPrimos+' '+str(n)
  return numerosPrimos
  
 
@app.route('/convert-heigth',methods=['POST'])
def convertidorTalla():
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
    json = request.json
    alturaPulgadas = float(json['estatura'])
    json['estatura']=alturaPulgadas*0.0254
    return json
  else:
    return 'Content-Type not supported!'
    
    
@app.route('/set-data',methods=['PUT'])
def guardarDatos():
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
    db.Base.metadata.create_all(db.engine)
    json = request.json
    if(len(json['nombre']) ==0):
        return 'Se requiere el nombre de la persona.'
    if(len(json['fechaNacimiento']) ==0):
        return 'Se requiere la fecha de nacimiento de la persona.'
    try:
        fechaNaciemnto = Date(json['fechaNacimiento'])
    except:
        return 'La fecha '+json['fechaNacimiento']+' no tiene un formato valido, debe ser yyyy/mm/dd'
    finally:
        persona = Persona(json['nombre'], json['fechaNacimiento'])
        db.session.add(persona)
        db.session.commit()
        return persona.__str__()
  else:
    return 'Content-Type not supported!'