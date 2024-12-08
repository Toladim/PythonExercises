import os
import shutil

path = '/home/toladim/Pulpit/exercises/python'
os.chdir(path)
el = 0
for element in os.listdir():
    if element != '.git' and not os.path.isdir(element):
        el += 1
        name = os.path.splitext(element)[0] #split extension 
        os.makedirs(name, exist_ok=True)
        shutil.move(element, name + '/')

#print(os.getcwd()) 
print(el)