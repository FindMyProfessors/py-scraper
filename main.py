import json

import confuse

from course import Course
from scrapers.university_of_central_florida import scrape_university_of_central_florida
from scrapers.valencia import scrape_valencia

scrapersDictionary = {'valencia': scrape_valencia,
                      'university-of-central-florida': scrape_university_of_central_florida}


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Course):
            return {'crn': obj.crn, 'course_code': obj.course_code, 'instructor': obj.instructor}
        return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    config = confuse.Configuration('school_scraper', __name__)
    config.set_file('config.yaml', base_for_paths=True)

    for key, value in config["schools"].items():
        print(value["enabled"])
        if value["enabled"].get(bool):
            print(json.dumps(scrapersDictionary[key](), cls=MyEncoder))
