from util import Util

def main():
    print("Welcome to student console IT566 app")
    while 1:
        print("Enter '1' to list all of the students")
        print("Enter '2' to add new students")
        print("Enter '3' to display all the student data")
        print("Enter '4' to calculate the average age")
        print("Enter '5' to exit the app")


        n = int(input())
        if n == 1:
            Util.list_students()
        elif n == 2:
            Util.add_student()
        elif n == 3:
            Util.display_list()
        elif n == 4:
            Util.average_age()
        elif n == 5:
            break
        else:
            print("Invalid choice")


main()