import sys

from exceptions.exception import InvalidNameLengthException, InvalidNameException, NullException
from src.student import Student
from src.teacher import Teacher
from src.teachers import Teachers


class Main:

    def __init__(self):
        pass

    def main_menu(self):
        self.welcome()
        print("""
                   1 --> Register
                   2 --> Login
                   3 --> Exit
        """)

        print("Kindly enter any choice from the above:")
        choice = input("still waiting: ")

        match choice:
            case "1":
                self.register_menu()
            case "2":
                self.login_menu()
            case "3":
                self.exit_app()
            case _:
                self.main_menu()

    def register_menu(self):
        print("""
                        1 --> Register as a teacher
                        2 --> Register as a student
                        3 --> Exit
                    """)
        choice = input("Kindly enter any choice from the above: ")
        if choice == "1":
            self.register_teacher()
        elif choice == "2":
            self.register_student()
        elif choice == "3":
            self.exit_app()
        else:
            self.main_menu()


    @staticmethod
    def exit_app():
        print("Exiting App.")
        print(">>>>>>>>>>>>>>>>>>>>.")
        sys.exit(0)

    @staticmethod
    def welcome() -> None:
        print("Welcome\n")
        print("The next page Displays And Help You With Your Choice ?\n")

    def register_teacher(self):
        try:
            name = input("Enter your name(First and Last name): ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            teacher = Teacher(name, email, password)
            teacher.register(name, email, password)
            print(f"Dear {name}, You have successfully registered")
        except InvalidNameLengthException as e:
            print(f"Error {e}")
        except InvalidNameException as e:
            print(f"Error {e}")
        except NullException as e:
            print(f"Error {e}")
        finally:
            self.main_menu()

    def register_student(self):
        try:
            name = input("Enter your name(First and Last name): ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            student = Student(name, email, password)
            student.register(name, email, password)
            print(f"Dear {name}, You have successfully registered")
        except InvalidNameLengthException as e:
            print(f"Error {e}")
        except InvalidNameException as e:
            print(f"Error {e}")
        except NullException as e:
            print(f"Error {e}")
        finally:
            self.main_menu()

    def login_menu(self):
        print("""
                                1 --> Login as a teacher
                                2 --> Login as a student
                                3 --> Exit
                            """)
        choice = input("Kindly enter any choice from the above: ")
        if choice == "1":
            self.login_teacher()
        elif choice == "2":
            self.login_student()
        elif choice == "3":
            self.exit_app()
        else:
            self.main_menu()

    def login_teacher(self):
        try:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            student = Student(email, password)
            teacher.find_teacher(email)
            teacher.login(email, password)
            print("You have successfully logged in.")
        except InvalidNameLengthException as e:
            print(f"Error {e}")
        except InvalidNameException as e:
            print(f"Error {e}")
        except NullException as e:
            print(f"Error {e}")
        finally:
            self.main_menu()

    def login_student(self):
        try:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            student = Student(email, password)
            teacher.find_teacher(email)
            check = teacher.login(email, password)
            if check:
            print("You have successfully logged in.")
            print("""
                1. View Courses
                2. Enroll Course(s)
                3. Check Notification
                4. Back to Main Menu
                """)
            choice = input("Kindly enter any choice from the above: ")

            if choice == "1":
                student.view_courses()
            elif choice == "2":
                student.view_enrolled_courses()
            elif choice == "3":
                student.check_notification()
            elif choice == "4 ":
                self.main_menu()
            else:
                self.main_menu()

        except InvalidNameLengthException as e:
            print(f"Error {e}")
        except InvalidNameException as e:
            print(f"Error {e}")
        except NullException as e:
            print(f"Error {e}")
        finally:
            self.main_menu()


if __name__ == "__main__":
    app = Main()
    app.main_menu()


