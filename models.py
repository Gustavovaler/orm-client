from orm.core import model

class User(model.Model):
    def __init__(self, nombre, *args,**kwargs):
        super().__init__(nombre,*args, **kwargs)


User('gustavo', prueba='prueba')