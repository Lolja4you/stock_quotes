import aiohttp
import asyncio
from urllib import parse
import pandas as pd
# from src.utils.logger import logger as log

# Настройка pandas
# pd.set_option("display.max_columns", 15)

async def query(method: str, **kwargs):
    """
    Асинхронно отправляю запрос к ISS MOEX
    :param method: Метод API
    :param kwargs: Параметры запроса
    :return: JSON-ответ или None в случае ошибки
    """
    try:
        url = f"https://iss.moex.com/iss/{method}.json"
        if kwargs:
            url += "?" + parse.urlencode(kwargs)
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                if r.status == 200:
                    return await r.json()
                else:
                    log.error(f'Request Error: {r.status}')
                    return None
    except Exception as e:
        log.error(f"query error: {e}")
        return None

def flatten(j: dict, blockname: str):
    """
    Преобразую JSON-ответ в список словарей
    :param j: JSON-ответ
    :param blockname: Название блока данных
    :return: Список словарей
    """
    # Создаем пустой список для хранения результата
    result = []

    # Получаем названия столбцов
    columns = j[blockname]['columns']
    # Проходим по каждой строке данных
    return (dict(zip(columns, row)) for row in j[blockname]['data'])

async def main():
    """
    Основная асинхронная функция
    """
    moex_query = await query('securities')
    # log.info(moex_query)
    if moex_query:
        f = pd.DataFrame(flatten(moex_query, 'securities'))
        log.info(f'\n{f}')
    else:
        log.error("Failed to fetch data from MOEX")

# Запуск асинхронного кода
if __name__ == '__main__':
    asyncio.run(main())