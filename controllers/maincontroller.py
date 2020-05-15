from orm.core.controller import Controller



class MainController(Controller):
    """docstring for MainController"""
    def __init__(self,view):
        super().__init__()
        self.view = view
        print(self.view)
        self.pr()


    

       
MainController('asd')       
