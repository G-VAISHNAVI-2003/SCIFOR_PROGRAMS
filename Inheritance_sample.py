class A:
    def __init__(self, name):
        self.name = name

    def view(self):
        print(self.name, "It's a nice view!..")

class B(A):
    def show(self):
        print(self.name, "The contents are shown here")

obj1 = A("Sri")
obj2 = B("Paul")
obj1.view()
obj2.view() 
obj2.show() 
