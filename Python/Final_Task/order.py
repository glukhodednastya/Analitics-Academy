from pizza import Pizza

from typing import Callable
from functools import wraps
import random


def log(params: str) -> Callable:
    """Параметрический декоратор, в котором параметры -
    название пиццы и время исполнения"""

    def outer_wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner_wrapper(pizza: Pizza) -> str:
            """Функция, которая возвращает шаблон
            с названием пиццы и временем исполнения"""
            result = func(pizza)
            return params.format(pizza.name, result)

        return inner_wrapper

    return outer_wrapper


@log('👨‍🍳 Мы приготовили вашу любимую пиццу {} за {} мин ⏳')
def bake(pizza: Pizza) -> int:
    """Готовит пиццу"""
    if pizza.size == 'XL':
        return random.randint(10, 15)
    else:
        return random.randint(5, 10)


@log('🛵 Мы доставили вашу любимую пиццу {} за {} мин ⏳')
def deliver(pizza: Pizza) -> int:
    """Доставляет пиццу"""
    return random.randint(20, 30)


@log('🚘 Вы забрали вашу любимую пиццу {} за {} мин ⌛')
def pickup(pizza: Pizza) -> int:
    """Самовывоз пиццы"""
    return random.randint(1, 5)
