def ictGrade(hScore,aScore,eScore): 
    return 100*(hScore/25 + aScore/50 + eScore/100)

studentName = input("What is your name? ") 
homeworkScore = input("What was your homework score ") 
assesmentScore = input("What was your assesment grade? ")
examScore = input("What was your exam score? ")

var1 = ictGrade(homeworkScore,assesmentScore,examScore) 
print(studentName)
