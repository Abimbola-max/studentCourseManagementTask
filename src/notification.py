class Notification:

    def __init__(self, message, course_code, student_name):
        self.__message = message
        self.course_code = course_code
        self.__student_name = student_name

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value

    @property
    def student_name(self):
        return self.__student_name


    def __repr__(self):
        return f"Notification: {self.message} for {self.student_name} in {self.course_code}"