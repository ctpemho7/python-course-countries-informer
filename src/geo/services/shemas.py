"""
Описание моделей данных (DTO).
"""

from pydantic import Field
from typing import List, Optional

from base.clients.shemas import HashableBaseModel


class CountryCityDTO(HashableBaseModel):
    """
    Модель данных для идентификации города.
    Содержит ISO Alpha2-код страны и название города.

    .. code-block::

        CountryCityDTO(
            city="Mariehamn",
            alpha2code="AX",
        )
    """

    city: str
    alpha2code: str = Field(min_length=2, max_length=2)


class CoordinatesDTO(HashableBaseModel):
    """
    Модель данных для координат.
    Содержит долготу (lon) и широту (lat).

    Пример использования:
    ```
    Coordinates(
        lon=37.6156,
        lat=55.7522,
    )
    ```

    Аргументы:
        lon (float): Долгота.
        lat (float): Широта.
    """
    lon: float
    lat: float


class WeatherDescriptionDTO(HashableBaseModel):
    """
    Модель данных для описания погоды.
    Содержит идентификатор (id), основное описание (main), описание (description) и иконку (icon).

    Пример использования:
    ```
    WeatherDescription(
        id=804,
        main="Clouds",
        description="overcast clouds",
        icon="04d",
    )
    ```

    Аргументы:
        id (int): Идентификатор.
        main (str): Основное описание.
        description (str): Описание.
        icon (str): Иконка.
    """
    id: int
    main: str
    description: str
    icon: str


class MainWeatherDTO(HashableBaseModel):
    """
    Модель данных для основных показателей погоды.
    Содержит температуру (temp), ощущаемую температуру (feels_like), минимальную температуру (temp_min),
    максимальную температуру (temp_max), давление (pressure), влажность (humidity), уровень моря (sea_level)
    и уровень земли (grnd_level).

    Пример использования:
    ```
    MainWeather(
        temp=3.8,
        feels_like=0.89,
        temp_min=1.42,
        temp_max=5.29,
        pressure=1025,
        humidity=99,
        sea_level=1025,
        grnd_level=1006,
    )
    ```

    Аргументы:
        temp (float): Температура.
        feels_like (float): Ощущаемая температура.
        temp_min (float): Минимальная температура.
        temp_max (float): Максимальная температура.
        pressure (int): Давление.
        humidity (int): Влажность.
        sea_level (int): Уровень моря.
        grnd_level (int): Уровень земли.
    """
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int


class WindDTO(HashableBaseModel):
    """
    Модель данных для погоды ветра.
    Содержит скорость (speed), направление (deg) и порывы (gust).

    Пример использования:
    ```
    Wind(
        speed=3.24,
        deg=201,
        gust=8.72,
    )
    ```

    Аргументы:
        speed (float): Скорость ветра.
        deg (int): Направление.
        gust (float): Порывы ветра.
    """
    speed: float
    deg: int
    gust: float


class CloudsDTO(HashableBaseModel):
    """
    Модель данных для погодных облаков.
    Содержит процент облачности (all).

    Пример использования:
    ```
    Clouds(
        all=100,
    )
    ```

    Аргументы:
        all (int): Процент облачности.
    """
    all: int


class SysDTO(HashableBaseModel):
    """
    Модель данных для системных данных о погоде.
    Содержит тип (type), идентификатор (id), страну (country), время восхода (sunrise) и заката (sunset).

    Пример использования:
    ```
    Sys(
        type=1,
        id=9027,
        country="RU",
        sunrise=1709180568,
        sunset=1709218897,
    )
    ```

    Аргументы:
        type (int): Тип.
        id (int): Идентификатор.
        country (str): Страна.
        sunrise (int): Время восхода.
        sunset (int): Время заката.
    """
    type: Optional[int]
    id: Optional[int]
    country: str
    sunrise: int
    sunset: int


class WeatherDTO(HashableBaseModel):
    """
    Модель данных для погоды.
    Содержит координаты (coord), описание погоды (weather), базу (base), основные показатели погоды (main),
    видимость (visibility), ветер (wind), облака (clouds), время (dt), системные данные (sys), часовой пояс (timezone),
    идентификатор (id), название (name) и код (cod).

    Пример использования:
    ```
    WeatherData(
        coord=Coordinates(lon=37.6156, lat=55.7522),
        weather=[
            WeatherDescription(id=804, main="Clouds", description="overcast clouds", icon="04d"),
        ],
        base="stations",
        main=MainWeather(temp=3.8, feels_like=0.89, temp_min=1.42, temp_max=5.29, pressure=1025, humidity=99, sea_level=1025, grnd_level=1006),
        visibility=10000,
        wind=Wind(speed=3.24, deg=201, gust=8.72),
        clouds=Clouds(all=100),
        dt=1709214035,
        sys=Sys(type=1, id=9027, country="RU", sunrise=1709180568, sunset=1709218897),
        timezone=10800,
        id=524901,
        name="Moscow",
        cod=200,
    )
    ```

    Аргументы:
        coord (Coordinates): Координаты.
        weather (List[WeatherDescription]): Описание погоды.
        base (str): База.
        main (MainWeather): Основные показатели погоды.
        visibility (int): Видимость.
        wind (Wind): Ветер.
        clouds (Clouds): Облака.
        dt (int): Время.
        sys (Sys): Системные данные.
        timezone (int): Часовой пояс.
        id (int): Идентификатор.
        name (str): Название.
        cod (int): Код.
    """
    coord: CoordinatesDTO
    weather: List[WeatherDescriptionDTO]
    base: str
    main: MainWeatherDTO
    visibility: int
    wind: WindDTO
    clouds: CloudsDTO
    dt: int
    sys: SysDTO
    timezone: int
    id: int
    name: str
    cod: int

