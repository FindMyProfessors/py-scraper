import json

import confuse

from course import Course
from professor import Professor
from rate_my_professor import rate_my_professor
from schools.university_of_central_florida import scrape_university_of_central_florida
from schools.valencia import scrape_valencia

scrapersDictionary = {'valencia': scrape_valencia,
                      'university-of-central-florida': scrape_university_of_central_florida}


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Course):
            return {'crn': obj.crn, 'course_code': obj.course_code, 'instructor': obj.instructor}
        if isinstance(obj, Professor):
            return {'first_name': obj.first_name,
                    'last_name': obj.last_name,
                    'would_take_again_rate': obj.would_take_again_rate,
                    'average_rating': obj.average_rating,
                    'ratings_count': obj.ratings_count}
        return json.JSONEncoder.default(self, obj)


if __name__ == '__main__':
    config = confuse.Configuration('school_scraper', __name__)
    config.set_file('config.yaml', base_for_paths=True)
    result = {}
    for key, value in config["schools"].items():
        print(value["enabled"])
        if value["enabled"].get(bool):
            data = scrapersDictionary[key]()
            locationDict = {}

            for state in value["locations"].get(dict):
                locationDict[state] = {}
                for location in value["locations"][state].get(dict):
                    locationDict[state][location] = rate_my_professor.start_scraping(value["locations"][state][location])

            result[key] = {'school_data': data, 'rms_data': locationDict}
    with open('output.json', 'w', encoding='utf8') as output_file:
        json.dump(result, output_file, cls=MyEncoder, indent=4, sort_keys=True, ensure_ascii=False)
