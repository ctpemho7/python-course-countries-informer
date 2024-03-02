"""Представления Django для новостей"""
from django.core.cache import caches
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.settings import api_settings

from app.settings import CACHE_NEWS
from news.serializers import NewsSerializer
from news.services.news import NewsService

paginator = api_settings.DEFAULT_PAGINATION_CLASS()
paginator.page_size = 5


@api_view(["GET"])
def get_news(request: Request, alpha2code: str) -> JsonResponse:
    """
    Получение информации о новостях страны.
    :param Request request: Объект запроса
    :param str alpha2code: ISO Alpha2 код страны
    :return:
    """
    cache_key = f"news_{alpha2code}"

    data = caches[CACHE_NEWS].get(cache_key)
    if not data:
        if data := NewsService().get_news(alpha2code):
            caches[CACHE_NEWS].set(cache_key, data)

    if data:
        result_page = paginator.paginate_queryset(data, request)
        serializer = NewsSerializer(result_page, many=True)

        return JsonResponse(serializer.data, safe=False)

    return JsonResponse([], safe=False)
