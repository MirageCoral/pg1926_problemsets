class MySchool:
    def __init__(self, employeeNumber, classNumber, teacherNumber, studentCapabity, type):
        self.employeeNumber = employeeNumber
        self.classNumber = classNumber
        self.teacherNumber = teacherNumber
        self.studentCapabity = studentCapabity
        self.type = type


school1 = MySchool(30, 20, 10, 400, "middleschool")
school2 = MySchool(40, 30, 15, 800, "highschool")
school3 = MySchool(80, 50, 25, 1000, "university")
