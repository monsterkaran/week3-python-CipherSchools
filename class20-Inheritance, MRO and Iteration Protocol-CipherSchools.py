# Inheritance
class A:
    def __init__(self):
        print("A init exe")
class B(A):
    def __init__(self):
        super().__init__()
        print("B init exe")
abc=B()
print(abc)
class SchoolMember:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("(Initialized SchoolMember: {})".format(self.name))
    def tell(self):
        print("Name: {} Age: {}".format(self.name,self,age),end=" ")
class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
        print("(Initialized Teacher: {})".format(self.name))
    def tell(self):
        super().tell()
        print("Salary: {:d}".format(self.name))
class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks=marks
        print("(Initialized Student: {})".format(self.name))
    def tell(self):
        super().tell(self)
        print("Marks: {:d}".format(self.marks))
t=Teacher("Mr. Ujjwal",40,30000)
s=Student("Nikhil",35,75)
# MRO (Method Resolution Order)
class A:
    pass
class B(A):
    x=5
class C(B):
    pass
class D(A):
    x=10
class E(C,D):
    pass
e=E()
print(e.x)
print(E.mro())
# Iteration Protocol
a=range(5)
it=a.__iter__()
print(it)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
a=range(5)
it=iter(a)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
class myrange:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        return myrange_iterator(self)
class myrange_iterator:
    def __init__(self,myrange):
        self.myrange=myrange
        self.i=0
    def __next__(self):
        ret=self.i
        self.i+=1
        if ret>=self.myrange.n:
            raise StopIteration
        return ret
a=myrange(5)
it=iter(a)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
