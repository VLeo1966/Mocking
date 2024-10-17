import pytest
from main import get_random_cat_image

api_key = 'live_yTqI1mhOSTsXRf9SAdyDdgMwyHFsmEhznLcknf3B4CTIrzIVtN6solIsZaZkeKrk'

def test_get_random_cat_image_success(mocker):
    mock_get = mocker.patch('main.requests.get')
    # Мок успешного ответа
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{'url': 'https://example.com/cat.jpg'}]

    cat_image_url = get_random_cat_image(api_key)
    assert cat_image_url == 'https://example.com/cat.jpg'


def test_get_random_cat_image_failure(mocker):
    mock_get = mocker.patch('main.requests.get')
    # Мок неуспешного ответа
    mock_get.return_value.status_code = 404

    cat_image_url = get_random_cat_image(api_key)
    assert cat_image_url is None
