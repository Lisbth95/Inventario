class Supplier:
    def __init__(self, nombre, apellidoP, apellidoM, direccion, celular, nota):
        self.nombre = nombre
        self.apellidoP = apellidoP
        self.apellidoM = apellidoM
        self.direccion = direccion
        self.celular = celular
        self.nota = nota
        
    def toDBCollection(self):
        return{
            'nombre' : self.nombre,
            'apellidoP' : self.apellidoP,
            'apellidoM' : self.apellidoM,
            'direccion': self.direccion,
            'celular' : self.celular,
            'nota' : self.nota,
        }