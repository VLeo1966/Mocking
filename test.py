import pytest
from main import get_weather
from config import api_key


def test_get_weather_success(mocker):
    mock_get = mocker.patch('main.requests.get')
    # Создаем мок-ответ для успешного запроса
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'weather': [{'description': 'clear sky'}], 'main': {'temp': 273.15}}

    city = 'London'
    weather_data = get_weather(api_key, city)
    assert weather_data == {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    }


def test_get_github_user_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    city = 'London'
    weather_data = get_weather(api_key, city)
    assert weather_data is None

