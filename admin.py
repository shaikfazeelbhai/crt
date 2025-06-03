'''
admin features:
1.add student
2.delete student
3.update student
4.timetable
5.marks

'''
from db import connection
def admin():
    conn=connection()
    cursor=conn.cursor()
    print("""\nadmin menu:
    1.add student
    2.update student details
    3.reset student password
    4.timetable
    5.view all students
    6.update timetable
    7.logout""")
    ch=int(input("enter your choice"))
    if ch==1:
        add_student()
    elif ch==2:
        update_student()
    elif ch==3:
        reset_student_password()
    elif ch==4:
        update_marks()
    elif ch==5:
        view_all_students()
    elif ch==6:
        update_timetable()
    elif ch==7:
        logout()
    else:
        print("invalid choice. please try again")
def add_student():
    conn=connection()
    roll_no = input("enter roll no:")
    name  =input("enter name:")
    class_name=input("enter class:")
    section = input("enter section:")
    password = "password@123"
    email = input("enter email:")
    query="insert into student(roll_no,name,class_name,section,password,email) values(%s,%s,%s,%s,%s,%s)"
    values = (roll_no,name,class_name,section,password,email)
    conn.commit()
    print("student added successfully.")
def update_student():
    conn=connection()
    cursor=conn.cursor()
    roll_no = input("enter roll no of student to update:")
    name  =input("enter new name:")
    class_name=input("enter new class:")
    section = input("enter new section:")
    email = input("enter new email:")
    query="update students SET name=%s, class=%s, section=%s, email=%s,where roll_no=%s"
    values =(name,class_name,section,email,roll_no)
    cursor.execute(query,values)
    conn.commit()
    print("Student details updated successfully.")
def reset_student_password():
    pass
def update_marks():
    
    cursor=conn.cursor()
    roll_no=input("enter roll no of student")
    subject=input("enter subject:")
    marks=input("enter marks:")
    query="update marks set marks=%s where roll_no=%s"
    values=(marks,roll_no,subject)
    cursor.execute(query,values)
def view_all_students():
    conn=connection()
    cursor=conn.cursor()
    query="select * from students"
    cursor.execute(query)
    result=cursor.fetchall()
    for row in result:
        print(row)
def update_timetable():
    pass
def logout():
    print("logging out...")

    return

if __name__=="__main__":
    admin()


