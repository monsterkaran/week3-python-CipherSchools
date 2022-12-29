# object
a=5
print(isinstance(a,object))
print(type(int))
print(isinstance(a,int))
def func():
    pass
print(type(func))
print(isinstance(func, object))
class a:
    name="shubham"
    marks=50
print(type(a))
a=5
print(type(a))
class A:
    def __call__(self):
        print("You called me")
a=A()
a() # a=A.__call__()
print(type(a))
a={"name":"shubham"}
print(a["name"])
print(a.__getitem__("name"))
class Exponent:
    def __init__(self,n):
        self.n=n
    def __getitem__(self, x):
        return x**self.n
e=Exponent(2)
print(e[6])
class A:
    name="shubham"
    def __init__(self,n):
        self.n=n
a=A(2)
print(a.name)
print(a.n)
class Dog:
    tricks=[]
    def __init__(self,name):
        self.name=name
    def add_tricks(self,trick):
        self.tricks.append(trick)
d1=Dog("Maxx")
d1.add_tricks("fetch")
d1.add_tricks("talk")
print(d1.tricks)
d2=Dog("Bella")
print(d2.tricks)