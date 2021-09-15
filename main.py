# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import confuse

from scrapers.valencia import scrape_valencia
scrapersDictionary = {'valencia': scrape_valencia}

if __name__ == '__main__':
    config = confuse.Configuration('school_scraper', __name__)
    config.set_file('config.yaml', base_for_paths=True)

    for key, value in config["schools"].items():
        print(value["enabled"])
        if value["enabled"].get(bool):
            print(scrapersDictionary[key]())