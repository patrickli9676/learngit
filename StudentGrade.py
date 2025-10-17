class StudentGrade:
    def __init__(self, student_name='', student_number='', chinese=0, math=0, english=0):
        self.name = student_name
        self.number = student_number
        self.chinese = chinese
        self.math = math
        self.english = english

    def print(self):
        print(f"姓名：{self.name}\n学号:{self.number}")
        print(f"语文成绩：{self.chinese}\n数学成绩:{self.math}\n英语成绩:{self.english}")

    def set(self):
        self.name = input("请输入该生姓名>>")
        self.number = input("请输入该生学号>>")
        self.chinese = float(input("请输入该生语文成绩>>"))
        self.math = float(input("请输入该生数学成绩>>"))
        self.english = float(input("请输入该生英语成绩>>"))

student1 = StudentGrade()
student1.set()
student1.print()

