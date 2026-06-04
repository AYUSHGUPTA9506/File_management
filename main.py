from pathlib import Path#librarywhich i can read the path
import os


def readfileandfolder():    #showcase all the files and folders in the current directory when we call
  path=Path('')          #we can get the path of the file in the directory
  items=list(path.rglob('*'))      #in ehich folder/file i am in , it will read  all the files recursively and provide the list of all the files and folders in the current directory
  for i,item in enumerate(items):     #enumerate is used to get the index of the items in the list
       print(f"{i+1}:{item}")    #it will print the index and the name of the file/folder


def createfile():           #crating a file 
  try:
   readfileandfolder()
   name=input("please tell your file name::-")#after showing the content exists, then tell your file name which you want to create
   p= Path(name)         #we had included the path name
   if not p.exists(): 
    with open(p,"w") as fs:   #we should give a user option to create file by any method he likes
      data=input("what you want to write in the file:-") #we are taking the data from the user which we want to write in the file
      fs.write(data)
    
      print("file created successfully")
   else:
    print("file already exists")
    
  except Exception as err:
      print(f"an error occured as {err}")
      
      
def readfile():
    try:
        
        readfileandfolder()
        name=input(" which file you want to read::-")#after showing the content exists, then tell your file name which you want to read
        p=Path(name)#agar path name exist karta hai yo show hoga warna create hojayega
        if p.exists() and p.is_file():#file honi chahiye directory nahi
            with open(p,'r') as fs:
                data=fs.read()
                print(data)
            
            print("file read successfully")
        else:
            print("file does not exist")
    except Exception as err:
        print(f"an error occured as {err}")
        
        
def updatefile():
  try:
    readfileandfolder()
    name=input(" which file you want to update::-")#after showing the content exists, then tell your file name which you want to update
    p=Path(name)#agar path name exist karta hai yo shoe hoga warna create hoj
    if p.exists() and p.is_file():
        print("press 1 for changing the name of file")
        print("press 2 for overwriting the dat of your file")
        print("press 3 for appending some content in your file")
        res=int(input("tell your response:- "))
        
        if res==1:
            name2=input("tell the new name of your file:-")
            p2=Path(name2)
            p.rename(p2)
            
        if res==2:
            with open(p,'w')as fs:
                data=input("what you want to write in the file:-") #we are taking the data from the user which we want to write in the file
                fs.write(data)   
        
        if res==3:
            with open(p,'a')as fs:
                data=input("what you want to append in the file:-") #we are taking the data from the user which we want to append in the file
                fs.write("" + data)  
                
  except Exception as err:
        print(f"an error occured as {err}")
  
         
def deletefile():  
    try:
        readfileandfolder()
        name=input(" which file you want to delete::-")#after showing the content exists, then tell your file name which you want to delete
        p=Path(name)#agar path name exist karta hai yo shoe hoga warna create hojayega
        
        if p.exists() and p.is_file():
            os.remove(p)#it will delete the file
            print("file removed successfully")
        else:
            print("file does not exist")
    except Exception as err:
            print(f"an error occured as {err}")
 
print("press 1 for creating a file ")
print("press 2 for reading a file ")
print("press 3 for updating a file ")
print("press 4 for deleting a file ")

check= int(input("plzz tell your response:-"))

if check==1:
    createfile()
if check==2:
    readfile()
if check==3:
    updatefile()
if check==4:
    deletefile()





















#we are not changing the file in os but we are altering in file handling system 