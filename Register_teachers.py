from main import Teacher

try:
    teacher_name = input("Enter name\n")
    teacher_email = input("Enter email\n")
    teacher_password = input("Enter password\n")

    Teacher.create(tr_name=teacher_name,tr_email=teacher_email, tr_pwd=teacher_password)
    print("Teacher created successfully")

except:
    print("Failed to create teachers")