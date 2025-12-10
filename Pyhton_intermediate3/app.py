# what is serialization 
# ans: serialization is the process of converting complex object into format that can easily be transmitted,stored and retrived from file
# why to use because as we know objects are very complex can have reference to other object 
# so serialization help us to store those objects into file that we then can use later
# three ways to serizalize objects
# example using pickle library serialize data into binary format
import pickle

data={'name':'zohaib','age':23}
class Student:
  def __init__(self,name,age):
    self.name=name
    self.age=age

# pickle is used to store complex objects like data object user defined objects,functions etc
with open('/home/zohaib-aziz/projects/QT  Projects/PyTasks/PythonTasks/Pyhton_intermediate3/data.pickle','wb') as file:
  pickle.dump(data,file)

with open('/home/zohaib-aziz/projects/QT  Projects/PyTasks/PythonTasks/Pyhton_intermediate3/data.pickle','rb') as file:
  serialized_data=file.read()
  file.seek(0)
  loaded_data=pickle.load(file)
  print(serialized_data)
  print(loaded_data)

# using json note this only used to serialized built in objects like list,dctionary
# string,boolean,None not complex one
import json

with open('/home/zohaib-aziz/projects/QT  Projects/PyTasks/PythonTasks/Pyhton_intermediate3/data.json','w') as file:
  json.dump(data,file)

with open('/home/zohaib-aziz/projects/QT  Projects/PyTasks/PythonTasks/Pyhton_intermediate3/data.json','r') as file:
  json_data_from_file=file.read()
  file.seek(0)
  json_data=json.load(file)

print(json_data_from_file)
print(json_data)


# # using yaml it is superset of json


# with open('/home/zohaib-aziz/projects/QT  Projects/PyTasks/PythonTasks/Pyhton_intermediate3/data.yaml','w') as file:
#   yaml.dump(data,file)
# with open('/home/zohaib-aziz/projects/QT  Projects/PyTasks/PythonTasks/Pyhton_intermediate3/data.yaml','r') as file:
#   data_from_yaml=file.read()
#   file.seek(0)
#   data_yaml=yaml.safe_load(file)

# print(data_from_yaml)
# print(data_yaml)

from functools import partial
# partial function function python is a specail kind of function which allows us to adjust the argument of function to generate new one like
def f(a,b,c):
  return a+b+c

add_15=partial(f,b=5,c=10)
print(add_15(100))