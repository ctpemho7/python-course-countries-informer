"""Сервисный слой для работы с данными о курсах валют."""
from typing import Optional

from geo.clients.currency import CurrencyClient
from geo.clients.shemas import CurrencyRatesDTO


class CurrencyService:
    """
    Сервис для работы с данными о курсах валют.
    """

    def get_currency(self, base: str) -> Optional[CurrencyRatesDTO]:
        """
        Получение списка курсов валют по её коду.

        :param base: Базовая валюта
        :return:
        """

        data = CurrencyClient().get_rates(base)
        if data:
            return CurrencyRatesDTO(
                base=data["base"],
                date=data["date"],
                rates=data["rates"],
            )

        return None
