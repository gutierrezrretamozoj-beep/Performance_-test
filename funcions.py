students_list = []
runnig = True
def menu():
   
    while True:
     print("\n=====WELCOME, PLEASE SELECT AN OPTION.=====")
     print("1.Register new students.")
     print("2. View the student list.")
     print("3. Search student")
     print("4. Update a student's information.")
     print("5. Delete students.")
     print("6. exit")
     
     opcion = input("Enter an option between (1-6): ")
     while not opcion.isdigit() or int(opcion) <1 or int(opcion)>6 or opcion == "": 
         print("Error: The option cannot be empty, contain letters, or be out of range.")
         opcion = input("Enter an option between (1-6): ")
menu()     
     
    
def register_new_students(students_list, ID, name, age, course_program, status, opcion):
    
    
    if opcion == "1":
     advance = "yes"
     while advance.lower() == "si":
        
      ID = input("Enter student ID: ").strip()
     while ID == "" or not ID.isdigit():
         print("Error: The name cannot be empty or consist of letters. ")
         ID = input("Enter student ID: ").strip()
         continue 
     
     name = input("Enter the student's name: ")
     while name == "" or name.isdigit():
         print("Error, the name cannot be empty or a number. ")
         name = input("Enter the student's name: ")
         continue
     
     age = input("Enter the student's age: ")
     while not age.isdigit() or int(age) <= 0 or age == "":
         print("Error: The age cannot be empty, less than 0, or be letters. ")
         age = input("Enter the student's age: ")  
         age = int(age) 
         continue
     
     course_program = input("Enter the program name: ")
     while course_program == "" or course_program.isdigit():
         print("error the program cannot be empty or be a number")
         course_program = input("Enter the program name: ")
         continue
     
     status = input("(1.active/2.inactive): ")
     while not status.isdigit() or int(status) < 1 >2 or status == "":
        print("Error: The status cannot be empty or contain letters.")
        status = input("(1.active/2.inactive): ")
        status = int(status)
        break
    
    registered_students = {
        "id": ID,
        "name": name,
        "age": age,
        "course_program": course_program,
        "status": status 
    }
    students_list.append(registered_students)
    print("added student")
    advance = input("Do you want to add another student (yes/no): ")
    
    
def Check_the_student_list(students_list, opcion):
    if opcion == "2":
        if not students_list:
         print("There are no registered students yet: ")
         
        else: 
         print("His students are:")
         for registered_students in students_list:
            print("ID:", registered_students ["ID"])
            print("NAME:", registered_students ["name"])
            print("AGE:", registered_students ["age"])
            print("courese_program:", registered_students ["course_program"])
            print("STATUS:", registered_students ["status"])
            

def Search_student(student_list, opcion):
    if opcion == "3":
     Search_student_id = input("Enter the student ID: ")
     while not Search_student_id.isdigit or Search_student_id == "":
         print("Error: The ID cannot be empty or contain letters.")
         Search_student_id = input("Enter the student ID: ")
         Search_student_id = int(Search_student_id)
         continue 
     for registerd_students in student_list:
         print("ID:", registerd_students["id"], registerd_students["name"])
 
 
def Update_a_students_information(student_list, opcion, registered_students):
   if opcion =="4":
     search = input("Enter the name of the student you want to change: ")
     while search == "" or search.isdigit():
        print("Error: The name cannot be empty or a number.")
        search = input("Enter the name of the student you want to change: ")  
        continue    
     for search in student_list:
        new = input("enter new name: ")
        index = student_list.index(search)
        student_list[index] = new 
     else: 
        print("the name does not exist.")
        
def  Delete_students(students_list, opcion, name, registered_students):
    if opcion == "5":
        
     delete = input("Enter the name of the student you want to delete: ")
    print("student successfully removed")
    if delete in registered_students:
        value_removed = registered_students.pop(name)
        print(f"student removed: {name}, {value_removed}")
    else: 
        print("the name does not exist")

    print("final students:", registered_students)    
    
def exit(opcion):
    if opcion == "6":
        print("leaving the program")
        
        
    