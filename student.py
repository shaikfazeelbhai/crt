from db import get_connection   
def student_menu(roll_no):
    while True:
        print("""\n student menu:
1.view details
2.view marks
3.view timetable
4.logout""")
    choice=input("enter choice:")
     
    if choice =='1':
        view_details(roll_no)
    elif choice == '2':
        view_marks(roll_no)
    elif choice == '3':
        view_timetable(roll_no)
    elif choice == '4':
        print("logging out...")
        break
    else:
        print("invalid choice..")
def view_details(roll_no):
    con = get_connection()
    cur = con.cursor()
    cur.execute("select * from student WHERE roll_no=%s",(roll))
    print("student details:")
    print(cur.fetchone())
    con.close()

    student_menu()