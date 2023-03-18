from utils.generate_text import generate_text

from .test_data import TEST_DATA


def test_generate_text():
    for test_data in TEST_DATA:
        assert generate_text(test_data['input_text'], test_data['input_digits']) == test_data['generated_text']
