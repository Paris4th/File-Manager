action = int(input("""
               What will be doing today ??
               1)  Create
               2)  Open foldeer
               3)  Open File      
"""))

#Create & 1if Statements

if action == 1:
    file_type = float(input("""
                 Select the file type:
                          
                 1.1)  Python File
                 1.2)  Text FIle
          """))
    if file_type == 1.1:
        name = input("Enter File Name:   ")
        with open (f"{name}.py", "x") as file:
            file.write("#Yow ")

    elif file_type == 1.2:
        with open ("text.txt ", "w") as file:
            file.write("print('Hello World!')\n")
        
    else:
        print ("Invalid Option !!!")

# Main If statement 
elif action == 2 :
     import os

# Folder to open

     choice2 =float(input("""
                    Are viuewing completed or incompleted
                    2.1)    Completed
                    2.2)    Incompleted     
                    """))

# Folder paths

     completed_path = r"C:\Users\mtimk\OneDrive\Documents\Python codes\Group Projects\Completed"
     incompleted_path = r"C:\Users\mtimk\OneDrive\Documents\Python codes\Group Projects\Incomplete"

# Choose to Delelete or Edit inside the chosen files

elif action == 3:
    
    choice3 = input("""Do u want to Delete or Edit File?    
                
                       1)     Delete
                       2)     Edit
                       """)
    
    completed_path = r"C:\Users\mtimk\OneDrive\Documents\Python codes\Group Projects\Completed"
    incompleted_path = r"C:\Users\mtimk\OneDrive\Documents\Python codes\Group Projects\Incomplete"
    import os

        # Deleting

    if choice3 =="1":

            file_name = input ("Type the name of the file you wan tto delete...")
            file_format = input ("Enter the file format...")

            # Choosing the file to delete
            folder = input("""From ?
                           1 - completed
                           2 - incompleted 
                           """ )
            
            if folder == "1":
                 o_path = completed_path
            elif folder == "2":
                 o_path = incompleted_path
            else:
                 print("invalid option")
            

            file_path1 = os.path.join(o_path, f"{file_name}.{file_format}")
            if os.path.exists(file_path1):
                os.remove(file_path1)
            else:
                print("File does not Exist!!!...")


        # Editing
    elif choice3 == "2" :

            file_name2 = input ("Type the name of the file you wan tto delete...")
            file_format2 = input ("Enter the file format...")
            adding = input("What do u want to add ?...   ")


            with open (f"{file_name2}.{file_format2}","a") as file:
                file.write(adding)
        
        # If they did't choose anything
    else:
            print("")

# Non Selected

else:
    print("Invalid option!!!")

