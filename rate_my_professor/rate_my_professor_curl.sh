curl 'https://www.ratemyprofessors.com/graphql' \
  -H 'Accept-Encoding: gzip, deflate, br' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Connection: keep-alive' \
  -H 'Authorization: Basic dGVzdDp0ZXN0' \
  --data-binary '{"query":"query { newSearch { teachers( query: { text: \"\", schoolID: \"U2Nob29sLTEzNjUx\" } first: 1000 last: 1000) {edges {node {id firstName lastName numRatings avgRatingRounded wouldTakeAgainPercentRounded }} pageInfo {hasNextPage endCursor}}}}","variables":{}}' \
  --compressed