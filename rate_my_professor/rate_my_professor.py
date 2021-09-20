import json

import requests

from professor import Professor


def start_scraping(school_id):
    return scrape(school_id, [], '')

def scrape(school_id, professors, cursor):
    url = 'https://www.ratemyprofessors.com/graphql'
    response = requests.post(url,
                             headers={'Authorization': 'Basic dGVzdDp0ZXN0'},
                             json={
                                 'query': "query NewSearch($first: Int!, $last: Int!, $cursor: String!){newSearch{teachers(query:{text:\"\",schoolID:\"U2Nob29sLTEzNjUx\"} first: $first last: $last, after: $cursor) {edges {node {id firstName lastName numRatings avgRatingRounded wouldTakeAgainPercentRounded }} pageInfo {hasNextPage endCursor}}}}",
                                 'variables': {'first': 1000, 'last': 1000, 'cursor': cursor}
                             })
    nextProfessors, endCursor, hasNextPage = parse(response.content)
    professors.extend(nextProfessors)

    print(endCursor)
    print(hasNextPage)
    if hasNextPage:
        return scrape(school_id, professors, endCursor)
    else:
        print(professors)
        return professors


def parse(data):
    professors = []
    decoded = json.loads(data)
    teachers = decoded['data']['newSearch']['teachers']
    for entry in teachers['edges']:
        professorEntry = entry['node']
        professor = Professor('', '', 0.0, 0, 0.0)
        professor.first_name = professorEntry['firstName']
        professor.last_name = professorEntry['lastName']
        professor.average_rating = round(professorEntry['avgRatingRounded'], 0)
        professor.ratings_count = professorEntry['numRatings']
        professor.would_take_again_rate = round(professorEntry['wouldTakeAgainPercentRounded'], 0)
        professors.append(professor)

    return professors, teachers['pageInfo']['endCursor'], teachers['pageInfo']['hasNextPage']
