import os
import shutil
path= input ("enter the name of your directory to be sorted")
list = os.listdir(path)

for file in list:
    name.ext=os.path.splittext(file)

ext=ext[1:]

if ext== '':
    continue 

if os.path.exists(path+'/'+ext):
    shutil.move(path+'/'+file,path+'/'+ext+'/'+file)

else:
    os.makedirs(path+'/'+ext)
    shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
