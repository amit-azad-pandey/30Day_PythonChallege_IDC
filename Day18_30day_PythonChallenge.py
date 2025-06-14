class SimpleMeta(type):
    def __new__(cls, name, bases, dct):
        bad_methods = []

        for key, value in dct.items():
            if key.startswith('__'):
                continue
            if not callable(value):
                continue                

            if key != key.lower():
                print(f"{key} : not in lowercase form!")
                bad_methods.append(key)
            else:
                print(f"{key} : all good!")

        if bad_methods:                 
            raise TypeError(f"Bad method names: {bad_methods}\nUse only lowercase for naming the methods!")

        return super().__new__(cls, name, bases, dct)



class greet(metaclass=SimpleMeta):
    intro = "Hey! I am learning Metaclasses today!"

    def Hello(self): #changing the name of method
        print("Hello world!")

    def show(self):
        print("Bye!")