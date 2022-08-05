vacunados_COVID = {
        'covidshiel':[1234567,987654321,42739842],
        'sputnik':[1231,1323,1,123123,312],
        'sinpharm':[2133123]}
                

def agregar(vacunados):
    try:
        vacunas = ['covidshiel', 'sputnik', 'sinpharm']
        dni = int(input('ingresa DNI'))
        vacuna = int(input("""ingresa:
        1:covidshiel
        2:sputnik
        3:sinpharm"""))
        vacunados[vacunas[vacuna-1]].append(dni)
    except(KeyError,IndexError):
        print('ojo!!! se ingreso una vacuna invalida')
    else:
        print('los datos se cargaron correctamente')
        
opcion = input('¿desea ingresar nuevos vacunados?')
while opcion.upper() == 'S':
    try:
        agregar(vacunados_COVID)
    except:
        print('ubo un problema')
    opcion = input('¿desea ingresar nuevos vacunados? s/n')
    
print('listado de los vacunados hasta hoy: ', vacunados_COVID)