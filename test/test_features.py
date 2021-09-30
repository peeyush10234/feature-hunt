from flask_cors import CORS
import requests
from pprint import pprint

def test_feature_1():
    response = requests.get("http://localhost:5000/feature-hunt/features")
    assert b'Create product page' in response.content

def test_feature_2():
    response = requests.get("http://localhost:5000/disentry/features")
    assert b'Enable scheduling/reminders' in response.content