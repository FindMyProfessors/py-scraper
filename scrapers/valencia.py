import requests
from bs4 import BeautifulSoup
from course import Course

def scrape_valencia():
    response = requests.get(
        'https://valenciacollege.edu/academics/schedule-search/search.php?term=202210&INSM%5B%5D=N&INSM%5B%5D=M&INSM%5B%5D=X&INSM%5B%5D=S&Campus=&course_desc=&crn=',
        headers={
            'Connection': 'keep-alive',
            # 'Pragma': 'no-cache',
            'Cache-Control': 'max-age=100000000000',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'https://valenciacollege.edu',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/93.0.4577.63 Safari/537.36',
            'Accept': 'text/htmlapplication/xhtml+xmlapplication/xml;q=0.9image/avifimage/webpimage/apng*/*;q=0.8application/signed-exchange;v=b3;q=0.9',
            'Sec-GPC': '1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://valenciacollege.edu/academics/schedule-search/',
            'Accept-Language': 'en-USen;q=0.9'
        })
    # print(response.content)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('tbody')
    row_cursor = 0
    courses = []

    for row in table.find_all('tr', recursive=False):
        if row_cursor % 3 == 0:
            course = Course("", "")
            cell_cursor = 0
            for cell in row.find_all('td', recursive=False):
                if cell_cursor == 0:
                    course.course_code = cell.find('strong').string
                elif cell_cursor == 3:
                    course.instructor = cell.string
                cell_cursor += 1
            courses.append(course)
        row_cursor += 1

    return courses