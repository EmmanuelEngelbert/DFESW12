def ictGrade(hScore,aScore,eScore):  
    if hScore > 25 or aScore > 50 or eScore > 100: 
        print("Error: invalid score/s provided")  
        return 0
    else:
        return round((100/3)*(hScore/25 + aScore/50 + eScore/100))

def gradeFunction(grade):
    if grade > 69: 
        return "A"
    elif grade > 59: 
        return "B"
    elif grade > 49:
        return "C"
    elif grade > 39:
        return "D" 
    elif grade > 29: 
        return "FAIL"

studentName = input("What is your name? ") 
homeworkScore = int(input("What was your homework score "))
assesmentScore = int(input("What was your assesment grade? "))
examScore = int(input("What was your exam score? "))

var1 = ictGrade(homeworkScore,assesmentScore,examScore)  
var2 = gradeFunction(var1)

if homeworkScore > 25 or assesmentScore > 50 or examScore >100:
    print(studentName, "your","%", "score could not be determined") 
else:
    print(studentName, "your score was", var1,"%", "Grade =", var2)
