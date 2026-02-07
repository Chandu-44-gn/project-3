def add(a,b):
    c=a+b
    return c
print(add(29,15))

#class
class Person:
    def __init__(self):
        print("Person object created")
        
    def hi(self):
        print("Person says hi")
Person().hi()
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def greet(self):
        print(f"Hello,my name is {self.name} and I am {self.age} years old.")
        
p1=Person("Chandu",20)
p1.greet()
p2=Person("Charu",21)
p2.greet()

#single inheritence
class Animal:
    def sound(self):
        print("Animal makes a sound")
        
class Cat(Animal):
    def sound(self):
        print("Cat meoww")
        
d=Cat()
d.sound()

class Animal:
    def sound(self):
        print("Animal makes a sound")
        
class Cat(Animal):
    pass
d=Cat()
d.sound()

#Multi level inheritence
class Grandparent:
    def greet(self):
        print("Hello from Grandparent")
class Parent(Grandparent):
    def speak(self):
        print("Speaking from Parent")
class child(Parent):
    def play(self):
        print("Playing in child")
c=child()
c.greet()
c.speak()
c.play()

#multiple inheritence
class Flyable:
    def fly(self):
        print("can fly")
class Swimmable:
    def swim(self):
        print("can Swim")
class Duck(Flyable,Swimmable):
    def quack(self):
        print("Quack!")
d=Duck()
d.fly()
d.swim()
d.quack()

#Encapsulation
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("chandu",20)
print(s1.age)
print(s1.name)

#abstraction using abc module
from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("car engine started")
c=car()
c.start()

#file creation
import os
def create_file(filename,content=""):
    filename=filename if filename.endswith(".txt")else (
        filename + ".txt")
    if os.path.exists(filename):
        print(f"[!] File'{filename}'already exists.")
    else:
        with open(filename,'w') as f:
            f.write(content)
        print(f"[+]  File'{filename}'created.")
        
#example usage
create_file("sample","Initial content for the file.\n")
    
#file reading
import os
def read_file(filename):
    filename=filename if filename.endswith(".txt")else(filename +".txt")
    if not os.path.exists(filename):
        print(f"[!]File'{filename}'does not exist.")
        return
    with open(filename,'r') as f:
        print(f"\n---Content of'{filename}'---\n")
        print(f.read())
read_file("sample")

#append file
import os
def append_to_file(filename,content):
    filename=filename if filename.endswith(".txt")else(
        filename + ".txt")
    if not os.path.exists(filename):
        print(f"[!]File'{filename}'does not exist.")
        return
    with open(filename,'a')as f:
        f.write(content)
    print(f"[+]Content appended to'{filename}'.")
append_to_file("sample","this line was appended.\n")
   
#over write file

        
        
        
        
        
       

