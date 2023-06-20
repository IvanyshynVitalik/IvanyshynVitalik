class Student():
    name = ""
    mark = 0

def find_total_mark(array):
    total_mark = 0
    for students in array:
        total_mark = total_mark + students.mark
    return total_mark

def collect_data(array):
    valid = False
    while not valid:
        try:
            students = int(input(Back.BLACK + Fore.GREEN + "Enter number of students: "))
            valid = True
        except:
            print("Only numbers please")
    total_mark = 0
    for i in range(students):
        name = input("Enter name of the student: ")
        name = name.capitalize()
        while name == "":
            print("You didn't enter the name")
            name = input("Enter name of the student: ")
        value = float(input("Enter mark as a whole number (Between 1-100%): "))
        while value >= 100 or value <= 1:
            print("Number is not in required range")
            value = int(input("Enter your mark as a whole number (Between 1-100%): "))
        next_student = Student()
        next_student.mark = value
        next_student.name = name
        array.append(next_student)
        total_mark += value
        students = len(array)
        total_mark = find_total_mark(array)
    return array, total_mark, students

def insertion_sort(array):
    UB = len(array)
    LB = 0
    for index in range(LB + 1, UB):
        key = array[index].name
        place = index - 1
        if array[place].name > key:
            while place >= LB and array[place].name > key:
                temp = array[place + 1]
                array[place + 1] = array[place]
                array[place] = temp
                place = place - 1
            array[place + 1].name = key
    return array

def linear_search(sorted_array, n, key):
    for i in range(0, n):
        if sorted_array[i].name == key:
            return sorted_array[i].mark
    return - 1

def searching():
    n = len(sorted_array)
    key = input(Back.BLACK + Fore.GREEN + "Enter name of the searched student: ")
    key = key.capitalize()
    res = linear_search(sorted_array, n, key)
    if res != -1:
        print("Student's mark:", str(res))
    else:
        print("Student is not found")

def colouring():
    if student.mark < 40:
        print(Fore.RED + f"{student.name} - {str(student.mark)}%")
    elif 40 <= student.mark < 65:
        print(Fore.YELLOW + f"{student.name} - {str(student.mark)}%")
    else:
        print(Fore.LIGHTGREEN_EX + f"{student.name} - {str(student.mark)}%")

import pickle
from colorama import Fore, Back, Style
array = []
try:
    file = open("classdata.dat", "rb")
    array, total_mark, students = pickle.load(file)
    file.close()
except:
    array, total_mark, students = collect_data(array)

students: int
sorted_array = insertion_sort(array)
avarage_mark = total_mark / students
for student in sorted_array:
    colouring()

print(Fore.GREEN + "Avarage % mark is:", avarage_mark, "%")

commands = input(Back.LIGHTYELLOW_EX + Fore.BLACK + "Select options: Add more students(add) | Search for a student(search) | Change student's resoult(change) | To stop enter -1: ")
while commands != "-1":
    if commands == "add":
            array, total_mark, students = collect_data(sorted_array)
            sorted_array = insertion_sort(array)
            for student in sorted_array:
                colouring()

    elif commands == "search":
            searching()

    elif commands == "change":
        name_1 = input(Back.LIGHTYELLOW_EX + Fore.BLACK + "Enter student's name:").capitalize()
        new_mark = float(input(Back.LIGHTYELLOW_EX + Fore.BLACK + "Enter new mark:"))
        for i in range(len(sorted_array)):
            if sorted_array[i].name == name_1:
                sorted_array[i].mark = new_mark
    else:
        print("Sorry, but this option does not exist. Try again!")

    commands = input(Back.LIGHTYELLOW_EX + Fore.BLACK + "Select options: Add more students(add) | Search for a student(search) | Change student's resoult(change) | To stop enter -1: ")

file = open("classdata.dat", "wb")
data = [sorted_array, total_mark, students]
pickle.dump(data, file)
file.close()


#p.221 flowchart

# (''') will help to improve command line or "\n" can help as well



