import pytest
import requests
from src.data.alt_text import *
from src.data.tour_info import tour_1000

BASE_URL = "https://api.artic.edu/api/v1"

"""
Get all apis and check status code is correct
"""


def test_get_all_info():
    response = requests.get(f'{BASE_URL}/artworks')
    assert response.status_code == 200

    resp = response.json()
    assert "data" in resp


"""
Confirm that the required information is correct 
"""


def test_focus_data():
    response = requests.get(f'{BASE_URL}/artworks/search')
    resp = response.json()
    assert "data" in resp, "Response JSON does not contain 'data' key"  # Ensure 'data' key exists

    score_count = sum(1 for item in resp["data"] if "_score" in item)
    assert score_count == 10

    samples = [SAMPLE_1, SAMPLE_2, SAMPLE_3, SAMPLE_4, SAMPLE_5, SAMPLE_6, SAMPLE_7, SAMPLE_8, SAMPLE_9, SAMPLE_10]
    for i in range(score_count):
        assert (resp['data'][i]['thumbnail']['alt_text']) == samples[i]


"""
Assuming there is a travel information number 1000, I want to compare all its data to verify if it's correct.
"""


def test_confirm_tour_info():
    test_tour_num = 1000
    response = requests.get(f'{BASE_URL}/tours/{test_tour_num}')
    resp = response.json()
    assert resp == tour_1000
