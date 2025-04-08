"""
1. Store the course codes, course names, credits, and student enrollment status (enrolled or not enrolled) of 5 courses in a list.
2. Allow users to enroll or unroll from courses.
3. Print the updated course information after each transaction.
4. Prevent users from enrolling in a course if they are already enrolled.
5. Prevent users from unenrolling from a course if they are not enrolled.
6. Keep track of the total credits earned by the student.
7. Allow users to view their enrolled courses and total credits earned.
"""
import random
from core_functions import (is_valid_name)

courses_dict = [
    {"course_code": "CS101", "course_name": "Introduction to Computer Science", "credits": 3, "enrolled": False},
    {"course_code": "CS202", "course_name": "Data Structures", "credits": 4, "enrolled": False},
    {"course_code": "CS303", "course_name": "Algorithms", "credits": 3, "enrolled": False},
    {"course_code": "CS404", "course_name": "Computer Networks", "credits": 4, "enrolled": False},
    {"course_code": "CS505", "course_name": "Database Systems", "credits": 3, "enrolled": False}
]

courses_only = ["CS101", "CS202", "CS303", "CS404", "CS505"]

student_name = ""
student_name_to_course_list_dict = {}


def manage_course_enrollment():
    student_name = input("What is your name: ")
    if is_valid_name(student_name):
        print(f"Hi {student_name}")
        do_again = "y"
        enroll_courses_list = []

        while do_again.lower() == "y":
            print("Manually = 1")
            print("Random = 2")
            method = input("Choose an option: ")

            enroll_course = None
            randomly_selected_str = ""
            if method == "1":
                enroll_course = input("Which course do u want to enroll in: ").upper()
            elif method == "2":
                enroll_course = random.choice(courses_only)
                randomly_selected_str = "randomly selected "
            else:
                print("Please enter a valid number")

            for course in courses_dict:

                if course["course_code"] == enroll_course:
                    if enroll_course not in enroll_courses_list:
                        enroll_courses_list.append(enroll_course)
                        course["enrolled"] = True
                        print(f"You have successfully been enrolled in {randomly_selected_str}{enroll_course} course, which has a total of {course['credits']} credits.")

                    else:
                        print(f"You have already enrolled in {enroll_course}.")

                else:
                    course["enrolled"] = False



            do_again = input("Do you want to enroll into more courses? (y/n): ")

        print(f"{student_name}, you have enrolled in {enroll_courses_list} courses")
        student_name_to_course_list_dict[student_name] = enroll_courses_list

    else:
        print("Please enter a valid name (letters and spaces only).")


def manage_course_unrollment():
    student_names = input("What is your name: ")

    if is_valid_name(student_names):
        print(f"Hi {student_names}")
        do_again = "y"
        print("Manually = 1")
        print("Random = 2")
        method = input("Choose an option: ")
        if student_names not in student_name_to_course_list_dict:
            student_name_to_course_list_dict[student_names] = []

        enroll_courses_list = student_name_to_course_list_dict[student_names]

        while do_again.lower() == "y":
            if method == "1":
                unroll_course = input("Which course do u want to unroll from: ").upper()
            elif method == "2":
                unroll_course = random.choice(courses_only)
            else:
                print("Please enter a valid number")
            for course in courses_dict:
                if course["course_code"] == unroll_course:
                    course["enrolled"] = False
                    print(f"You have successfully been unrolled from {course['course_name']}.")
            if unroll_course in enroll_courses_list:
                enroll_courses_list.remove(unroll_course)

            else:
                print(f"You are not enrolled in {unroll_course}.")


            do_again = input("Do you want to unroll from more courses? (y/n): ")
            student_name_to_course_list_dict[student_names] = enroll_courses_list

            if len(enroll_courses_list) >= 1:
                print(f"{student_names}, you are now enrolled in: {enroll_courses_list}")

            else:
                print(f"{student_names}, you are not enrolled in any courses.")

    else:
        print("Please enter a valid name (letters and spaces only).")



def enroll_unroll_smth_choice():
    print("Unroll from course = 1")
    print("Enroll in course = 2")
    print("Enrolled courses and total credits earned = 3")
    choice = int(input("What do you want to do: "))

    if choice == 1:
        manage_course_unrollment()

    elif choice == 2:
        manage_course_enrollment()

    elif choice == 3:
        student_name = input("What is your name: ")

        if student_name in student_name_to_course_list_dict:

            for course_code in student_name_to_course_list_dict[student_name]:

                for course in courses_dict:

                    if course["course_code"] == course_code:
                        print(f"You are enrolled in {course['course_name']}, which as a total of {course['credits']} credits.")
                        break

        else:
            print("You are not enrolled in any courses.")

    else:
        print("Please enter 1, 2, or 3")


while not is_valid_name(student_name):
    continue_program = input("Do you want to continue (y/n): ")

    if continue_program == "y":
        student_name = ""
        enroll_unroll_smth_choice()

    else:
        print("GoodBye")
        student_name = "Random"

for student in student_name_to_course_list_dict:
    print(f"{student}, is enrolled in:, {student_name_to_course_list_dict[student]}")
