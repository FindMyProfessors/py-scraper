class Course:
    def __init__(self, course_code, instructor):
        self.course_code = course_code
        self.instructor = instructor

    def __repr__(self):
        return "Course{course_code: %s, instructor: %s}" % (self.course_code, self.instructor)
