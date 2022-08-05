class Vacunas:
    def __init__(self, nom, lab):
        self._nombre = nom
        self._laboratorio = lab
                    
    @property                                                                     
    def nombre(self):
        return self._nombre                       

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor       
                                    
    def informacion (self):
        return (f'Laboratorio de fabricación: {self._laboratorio }')
               
class VacunaCovid(Vacunas):
    def __init__(self, nom, lab, cant, tip):
        super().__init__ (nom, lab)
        self._cantidad = cant
        self._tipo = tip

    @property
    def cantidad (self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cant):
        self._cantidad = cant

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, tip):
        self._tipo = tip
                    
    def informacion (self):
        return (super.informacion())
                              
                              
lista_vacunas = [VacunaCovid('Sputnik', 'xx',100, 'COVID'), VacunaCovid('Moderna', 'zz', 50, 'COVID'), VacunaCovid ('Flucelvax','dd', 1000, 'GRIPE')]

for i  in range(3):
    cant = input (f'Ingrese cantidad de vacuna {lista_vacunas[i].nombre} que llegaron. Si no llegó ninguna ingrese 0: ')
    while not cant.isnumeric():
        cant = input (f'Ingrese cantidad de vacuna {lista_vacunas[i].nombre} que llegaron. Si no llegó ninguna ingrese 0: ')
    lista_vacunas[i].cantidad += int(cant)

for i in range(3):
    if lista_vacunas[i].cantidad < 200:
        print (f'Se deben pedir más vacunas {lista_vacunas[i].nombre} para {lista_vacunas[i].tipo}. {lista_vacunas[i].informacion()}')