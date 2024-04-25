class A:
    def shout(self):
        pass

class B(A):
    def shout(self):
        print("Haha")

class C(A):
    def shout(self):
        print("wooh")

def make_sound(human):
    human.shout()

obj1 = B()
obj2 = C()

make_sound(obj1)  
make_sound(obj2)  
