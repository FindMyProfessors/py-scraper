class Course:
    def __init__(self, crn, course_code, instructor):
        self.crn = crn
        self.course_code = course_code
        self.instructor = instructor

    def __repr__(self):
        return "Course{crn: %s, course_code: %s, instructor: %s}" % (self.crn, self.course_code, self.instructor)
