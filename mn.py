import requests

def my_function():
    pass

print(__name__)
print(requests.__name__)
print(requests.__build__)
print(requests.__cake__)
print(my_function.__name__)

for item in dir():
    print(item)

word = "hello"

print(hasattr(word, "upper"))
print(hasattr(word, "uppercase"))
print(word.upper())

print(callable(my_function))
print(callable(word))

class A:
    pass

class B(A):
    pass

print(issubclass(B,A))
print(issubclass(A,B))

if isinstance(word, int):
    print("wt xbckj")
elif isinstance(word,str):
    print("wt cnhsxrf")


import inspect

print(
    inspect.ismodule(requests),
    inspect.isfunction(my_function),
    inspect.isclass(B)
)


import sys

print(sys.version)
print(sys.platform)
print(sys.executable)
print(sys.argv)

for module_name, module_path in sys.modules.items():
    print(module_name, module_path)
print("======================================")

for item in dir(__builtins__):
    print(item)