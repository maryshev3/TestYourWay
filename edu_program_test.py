import requests
import unittest

def test_edu_program():
    base_url = "https://yourwayapi.ru/"

    body_request = '''
    [
    {
        "question": "Хотели бы вы писать программы?",
        "edu_program": "09.03.01 Информатика и вычислительная техника",
        "answer": 5
    }
    ]
    '''

    res = requests.post(
        url = base_url + "edu/program/",
        data = body_request.encode('utf-8'),
        params = {"http.protocol.content-charset":"UTF-8"}
    )

    print(res.text)

    test = unittest.TestCase()

    test.assertEqual(first = res.status_code, second = 200)

    print(test.longMessage)