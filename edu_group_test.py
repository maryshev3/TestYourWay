import requests
import unittest

def test_edu_group():
    base_url = "https://yourwayapi.ru/"

    body_request = '''{
    "schools": [
        {
        "name": "школа1"
        }
    ],
    "publics": [
        {
        "name": "группа1"
        }
    ]
    }'''

    res = requests.post(
        url = base_url + "edu/group/",
        data = body_request.encode('utf-8'),
        params = {"http.protocol.content-charset":"UTF-8"}
    )

    print(res.text)

    test = unittest.TestCase()

    test.assertEqual(first = res.status_code, second = 200)

    print(test.longMessage)