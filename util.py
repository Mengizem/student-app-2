import json
import tabulate

class Util:
    @staticmethod
    def list_students():
        f = open("students.json")
        student_list = json.loads(f.read())
        f.close()

        for student in student_list["students"]:
            print(student)

    @staticmethod
    def add_student():
        print("Enter new student recorde")
        print("Enter student name")
        name = input()

        print("Enter student age")
        age = int(input())

        f = open("students.json")
        student_list = json.loads(f.read())
        f.close()

        students = student_list["students"]
        students.append({'name':name, 'age':age})
        student_list["students"] = students
        js =json.dumps(student_list)

        f = open("students.json", 'w')
        f.write(js)
        f.close()

        for student in students:
            print(student)
    @staticmethod
    def display_list():
        try:
            f = open("students.json")
            student_list = json.loads(f.read())
            f.close()

            for student in student_list["students"]:
                data = [['name', student["name"]], ['age', student["age"]]]
                print(tabulate.tabulate(data))
        except:
            print("exception while fetching student")

    @staticmethod
    def average_age():
        f = open("students.json")
        student_list = json.loads(f.read())
        f.close()

        totalsum = 0
        count = 0
        for student in student_list["students"]:
            totalsum += student["age"]
            count += 1
        average = totalsum/count
        print("Average student age: " + str(average))

