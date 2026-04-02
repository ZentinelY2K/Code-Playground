student_name = ""
test_score = ""
def teacherUI():
    global student_name,test_score
    student_name = input("Please provide a username: \n")
    if student_name == '' or student_name.isdigit():
        raise TypeError("Name can't be empty nor can it be a number please try again:\n")
    else:
        pass #do nothing
    try:
       test_score = int(input("Provide test score:\n"))
       if not(test_score > 0 and test_score < 100):
           raise TypeError("Must be a digit in between 0-100 and not a String")
    except ValueError as vl:
        if vl:
            print("You must Type a number, not a String")
    finally:
        return()
    
def grades():
    global student_name,test_score
    print(f"The grade for {student_name}:")
    if test_score >= 90:
        print("A")
    elif test_score  >= 80  and test_score < 90:
        print("B")
    elif test_score >= 70 and test_score < 80:
        print("C")
    elif test_score >60 and test_score < 70:
        print("D")
    else:
        print("F")

    return()

teacherUI()  
grades()
