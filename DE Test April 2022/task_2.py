import requests as req
import csv
from os.path import exists
from collections.abc import Iterator

# A team of analysts wish to discover how far people are travelling to their nearest
# desired court. We have provided you with a small test dataset so you can find out if
# it is possible to give the analysts the data they need to do this. The data is in
# `people.csv` and contains the following columns:
# - person_name
# - home_postcode
# - looking_for_court_type

# The courts and tribunals finder API returns a list of the 10 nearest courts to a
# given postcode. The output is an array of objects in JSON format. The API is
# accessed by including the postcode of interest in a URL. For example, accessing
# https://courttribunalfinder.service.gov.uk/search/results.json?postcode=E144PU gives
# the 10 nearest courts to the postcode E14 4PU. Visit the link to see an example of
# the output.

# Below is the first element of the JSON array from the above API call. We only want the
# following keys from the json:
# - name
# - dx_number
# - distance
# dx_number is not always returned and the "types" field can be empty.

"""
[
    {
        "name": "Central London Employment Tribunal",
        "lat": 51.5158158439741,
        "lon": -0.118745425821452,
        "number": null,
        "cci_code": null,
        "magistrate_code": null,
        "slug": "central-london-employment-tribunal",
        "types": [
            "Tribunal"
        ],
        "address": {
            "address_lines": [
                "Victory House",
                "30-34 Kingsway"
            ],
            "postcode": "WC2B 6EX",
            "town": "London",
            "type": "Visiting"
        },
        "areas_of_law": [
            {
                "name": "Employment",
                "external_link": "https%3A//www.gov.uk/courts-tribunals/employment-tribunal",
                "display_url": "<bound method AreaOfLaw.display_url of <AreaOfLaw: Employment>>",
                "external_link_desc": "Information about the Employment Tribunal"
            }
        ],
        "displayed": true,
        "hide_aols": false,
        "dx_number": "141420 Bloomsbury 7",
        "distance": 1.29
    },
    etc
]
"""

# Use this API and the data in people.csv to determine how far each person's nearest
# desired court is. Generate an output (of whatever format you feel is appropriate)
# showing, for each person:
# - name
# - type of court desired
# - home postcode
# - nearest court of the right type
# - the dx_number (if available) of the nearest court of the right type
# - the distance to the nearest court of the right type

class CourtTypeError(Exception):
    pass

class APIError(Exception):
    pass

PEOPLE_CSV_FILE_PATH = './people.csv'

def read_csv(file_path: str) -> Iterator[dict]:
    """Generator function that reads and yields
    each line of a csv as a dict."""
    with open(file_path) as csv_file:
        lines = csv.DictReader(csv_file)
        for line in lines:
            yield line

def get_nearest_courts(postcode: str) -> list[dict]:
    """Takes UK postcode and returns a list of the
    10 nearest courts."""
    url = f"https://courttribunalfinder.service.gov.uk/search/results.json?postcode={postcode}"
    res = req.get(url)

    if 400 <= res.status_code < 500:
        raise APIError(f'CLIENT ERROR {res.status_code}: check postcode is valid UK postcode.')
    elif 500 <= res.status_code < 600:
        raise APIError(f'SERVER ERROR: {res.status_code}')

    return res.json()

def extract_valid_court(courts: list[dict], type_needed: str) -> dict:
    """Takes a list of courts and the type of court needed. Returns
    the first court that matches required type."""
    for court in courts:
        if type_needed in court['types']:
            result =  {'court_name': court['name'], 'distance': court['distance']}
            if court['dx_number']:
                result['dx_number'] = court['dx_number']
                return result
            return result
    
    raise CourtTypeError(f"No courts of type '{type_needed}' found.")

if __name__ == "__main__":
    # [TODO]: write your answer here
    for person in read_csv(PEOPLE_CSV_FILE_PATH):
        
        try:
            nearest_courts = get_nearest_courts(person['home_postcode'])
        except APIError as err:
            print(err.args[0])
            continue

        try:
            valid_court = extract_valid_court(nearest_courts,
                                            person['looking_for_court_type'])
        except CourtTypeError as err:
            print(err.args[0])
            continue

        data = dict(person, **valid_court)
        print(data)
