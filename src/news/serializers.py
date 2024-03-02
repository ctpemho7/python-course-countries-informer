from rest_framework import serializers


class NewsSerializer(serializers.Serializer):
    """
    Сериализатор для модели данных новости.
    """

    source = serializers.CharField()
    author = serializers.CharField(allow_null=True)
    title = serializers.CharField()
    description = serializers.CharField(allow_null=True)
    url = serializers.CharField(allow_null=True)
    published_at = serializers.DateTimeField()
