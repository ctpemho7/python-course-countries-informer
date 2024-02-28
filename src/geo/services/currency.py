from typing import Optional

from geo.clients.currency import CurrencyClient


class CurrencyService:
    """
    Сервис для работы с данными о курсах валют.
    """

    def get_currency(self, base: str) -> Optional[dict]:
        """
        Получение списка курсов валют по её коду.

        :param base: Базовая валюта
        :return:
        """

        if data := CurrencyClient().get_rates(base):
            return data

        return None
