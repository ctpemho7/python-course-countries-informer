from rest_framework import serializers

from geo.models import Country, City


class CountrySerializer(serializers.ModelSerializer):
    """
    Сериализатор для данных о стране.
    """

    class Meta:
        model = Country
        fields = [
            "id",
            "name",
            "alpha2code",
            "alpha3code",
            "capital",
            "region",
            "subregion",
            "population",
            "latitude",
            "longitude",
            "demonym",
            "area",
            "numeric_code",
            "flag",
            "currencies",
            "languages",
        ]


class CitySerializer(serializers.ModelSerializer):
    """
    Сериализатор для данных о городе.
    """

    country = CountrySerializer(read_only=True)

    class Meta:
        model = City
        fields = [
            "id",
            "name",
            "region",
            "latitude",
            "longitude",
            "country",
        ]


# сериализаторы данных о погоде
class CoordinatesSerializer(serializers.Serializer):
    lon = serializers.FloatField()
    lat = serializers.FloatField()

    def create(self, validated_data):
        return validated_data


class WeatherDescriptionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    main = serializers.CharField()
    description = serializers.CharField()
    icon = serializers.CharField()

    def create(self, validated_data):
        return validated_data


class MainWeatherSerializer(serializers.Serializer):
    temp = serializers.FloatField()
    feels_like = serializers.FloatField()
    temp_min = serializers.FloatField()
    temp_max = serializers.FloatField()
    pressure = serializers.IntegerField()
    humidity = serializers.IntegerField()
    sea_level = serializers.IntegerField()
    grnd_level = serializers.IntegerField()

    def create(self, validated_data):
        return validated_data


class WindSerializer(serializers.Serializer):
    speed = serializers.FloatField()
    deg = serializers.IntegerField()
    gust = serializers.FloatField()

    def create(self, validated_data):
        return validated_data


class CloudsSerializer(serializers.Serializer):
    all = serializers.IntegerField()

    def create(self, validated_data):
        return validated_data


class SysSerializer(serializers.Serializer):
    type = serializers.IntegerField()
    id = serializers.IntegerField()
    country = serializers.CharField()
    sunrise = serializers.IntegerField()
    sunset = serializers.IntegerField()

    def create(self, validated_data):
        return validated_data


class WeatherSerializer(serializers.Serializer):
    coord = CoordinatesSerializer()
    weather = WeatherDescriptionSerializer(many=True)
    base = serializers.CharField()
    main = MainWeatherSerializer()
    visibility = serializers.IntegerField()
    wind = WindSerializer()
    clouds = CloudsSerializer()
    dt = serializers.IntegerField()
    sys = SysSerializer()
    timezone = serializers.IntegerField()
    id = serializers.IntegerField()
    name = serializers.CharField()
    cod = serializers.IntegerField()

    def create(self, validated_data):
        return validated_data


class CurrencySerializer(serializers.Serializer):
    """
    Cериализатор данных о валюте.
    """

    base = serializers.CharField()
    date = serializers.DateField()
    rates = serializers.DictField()
