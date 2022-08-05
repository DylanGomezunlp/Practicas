import json
import os
dicc_nombres = {'Pyroclastic shield': 'Escudo piroclastico', 'Mud volcano': 'Volcan de lodo', 
    'Subglacial volcano': 'Volcan subglacial', 'Crater rows': 'Filas de crateres',
    'Submarine volcanoes' : 'Volcanes submarinos', 'Pyroclastic cone' : 'Cono piroclastico', 'Lava dome' : 'Domo de lava', 
    'Caldera' : 'Caldera', 'Lava cone' :'Cono de lava' , 'Volcanic field' : 'campo volcanico', 'Stratovolcano' : 'Estratovolcan', 'Shield volcano' : 'Volcan en escudo', 
    'Tuff cone' : 'Cono de toba', 'Compound volcano' : 'Volcan compuesto', 'Maar' : 'Maar', 'Submarine volcano' : 'Volcan submarino', 'Complex volcano' : 'Volcan complejo', 
    'Cinder cone' : 'Cono de ceniza', 'Pumice cone' : 'Cono de piedra pómez', 'Fissure vent' : 'Respiradero de fisura'}

ruta = os.path.join(os.getcwd(), 'dicc_nombres.json')  
a_file = open(ruta, "w")
json.dump(dicc_nombres, a_file)
a_file.close()