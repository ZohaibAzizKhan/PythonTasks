# serialization 
# simple convertion of complex objects into such kind of format that can easyly be transmitted and stored
# liberaries
import functools
import pickle
class Student:
  def __init__(self,name,age):
    self.name=name
    self.age=age

s=Student('zohaib',24)
with open('/home/zohaib-aziz/projects/QT  Projects/PyTasks/PythonTasks/Pyhton_intermediate3/data.pickle','wb') as file:
  pickle.dump(s,file)

with open('/home/zohaib-aziz/projects/QT  Projects/PyTasks/PythonTasks/Pyhton_intermediate3/data.pickle','rb') as file:
  load=pickle.load(file)

print(load.name)
print(load.age)

# using json
import json

data={
  'name':'zohaib',
  'age':24
}
with open('/home/zohaib-aziz/projects/QT  Projects/PyTasks/PythonTasks/Pyhton_intermediate3/data.pickle','w') as file:
  json.dump(data,file)

with open('/home/zohaib-aziz/projects/QT  Projects/PyTasks/PythonTasks/Pyhton_intermediate3/data.pickle','r') as file:
  load=json.load(file)
print(load)


from functools import partial,wraps
# partial function 
def func(a,b,c):
  return a+b+c


part=partial(func,b=4,c=15)
print(part(100))


# closure 
def outer(name):
  def inner():
    print('i have access to outer function parameter',name)
  return inner

out=outer('zohaib')
out()
# decorator
def decorator_function(func):
   @wraps(func)
   def wrapper():
     print('code started executing')
     func(4,7)
     print('code stoped executing')
   return wr

@decorator_function
def add(a=0,b=0):
  print('function started executing',a+b)

add()