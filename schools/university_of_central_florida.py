import json

import requests

from course import Course


def scrape_university_of_central_florida():
    courses = []
    # https://cdl.ucf.edu/support/student/modalities/
    for mode in {"W", "V", "M", "RS", "P"}:
        if len(courses) == 0:
            courses = scrape_endpoint(mode)
        else:
            courses[0:0] = scrape_endpoint(mode)
    return courses


def scrape_endpoint(mode):
    return parse(requests.get(
        'https://cdl.ucf.edu/wp-content/themes/cdl/lib/course-search-ajax.php?call=classes&term=1710&prefix=&catalog=&title=&instructor=&career=&college=&department=&mode={}&_=1631687421296'.format(
            mode)).content)


def parse(data):
    courses = []
    decoded = json.loads(data)
    for entry in decoded['classes']:
        course = Course('', '', '')
        course.crn = entry['registration_number']
        course.course_code = '{}{}'.format(entry['prefix'], entry['catalog_number'])
        course.instructor = '{} {}'.format(entry['name_first'], entry['name_last'])
        courses.append(course)
    return courses
