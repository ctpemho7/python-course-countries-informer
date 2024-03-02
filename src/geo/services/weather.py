"""Сервисный слой для работы с данными о погоде."""
from typing import Optional

from geo.clients.shemas import WeatherInfoDTO
from geo.clients.weather import WeatherClient


class WeatherService:
    """
    Сервис для работы с данными о погоде.
    """

    def get_weather(self, alpha2code: str, city: str) -> Optional[WeatherInfoDTO]:
        """
        Получение списка стран по названию.

        :param alpha2code: ISO Alpha2 код страны
        :param city: Город
        :return:
        """

        data = WeatherClient().get_weather(f"{city},{alpha2code}")
        if data:
            return WeatherInfoDTO(
                temp=data["main"]["temp"],
                pressure=data["main"]["pressure"],
                humidity=data["main"]["humidity"],
                visibility=data["visibility"],
                wind_speed=data["wind"]["speed"],
                description=data["weather"][0]["description"],
            )

        return None
