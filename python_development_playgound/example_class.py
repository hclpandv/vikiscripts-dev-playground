class ExampleClass:
    def __init__(self, name, age, occupation):
        self._name = name
        self._age = age
        self._occupation = occupation
    # In Python, variables that start with an underscore (_) are typically 
    # used to indicate that they are intended to be "private" variables, which 
    # should not be accessed or modified directly from outside the class.
    def greet(self):
        return "Hello, my name is {} and I am {} years old. I work as a {}.".format(self._name,self._age,self._occupation)

    def farewell(self):
        return "Goodbye from {}!".format(self.name)
    
    @property
    def name(self):
        return self._name.title()
