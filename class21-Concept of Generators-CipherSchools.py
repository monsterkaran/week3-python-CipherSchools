# Generators
# Eager Loading
def generate_squares(n):
    return [i**2 for i in range(1,n)]
for x in generate_squares(100):
    print(x)
# Lazy Loading
def generate_squares(n):
    for i in range(1,n):
        yield i**2
for i in generate_squares(100):
    print(i)
# from time import sleep
# def func():
#     print("started")
#     yield
#     sleep(5)
#     print("ended")
# print("hello")
# it=iter(func())
# print(next(it))
# print("world")
# print(next(it))
a=(i**2 for i in range(10))
print(iter(a))
