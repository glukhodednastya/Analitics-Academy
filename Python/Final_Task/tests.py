from pizza import Margherita, Pepperoni, Hawaiian
from order import bake, deliver, pickup
from cli import menu, order

# для замены реального обращения к randint()
from unittest.mock import patch
# для тестирования click
from click.testing import CliRunner
import random


def test_dict():
    """Тестирует метод dict"""
    assert Hawaiian(size='L').dict() == {
        'tomato sauce': 200,
        'mozzarella': 150,
        'chicken': 75,
        'pineapples': 50,
    }
    assert Pepperoni(size='XL').dict() == {
        'tomato sauce': 400,
        'mozzarella': 300,
        'pepperoni': 140,
    }
    assert 'tomatoes' in Margherita().dict()


def test_eq():
    """Тестирует метод eq"""
    assert Margherita(size='XL') == Margherita(size='XL')
    assert Margherita(size='L') != Margherita(size='XL')
    assert Margherita(size='XL') != Hawaiian(size='XL')
    assert Margherita(size='XL') != Pepperoni(size='L')


def test_bake():
    """Тестирует функцию bake до применения декоратора"""
    assert bake.__wrapped__(Margherita(size='XL')) in range(10, 16)
    assert bake.__wrapped__(Margherita(size='L')) in range(5, 11)


def test_deliver():
    """Тестирует функцию deliver до применения декоратора"""
    assert deliver.__wrapped__(Margherita(size='XL')) in range(20, 31)


def test_pickup():
    """Тестирует функцию pickup до применения декоратора"""
    assert pickup.__wrapped__(Pepperoni()) in range(1, 6)


def test_bake_with_decorator():
    """Тестирует функцию bake с декоратором"""
    my_randint = 11
    with patch.object(random, 'randint', return_value=my_randint):
        assert (
                bake(Margherita()) == '👨‍🍳 Мы приготовили вашу любимую' +
                ' пиццу Margherita 🧀 за 11 мин ⏳'
        )


def test_deliver_with_decorator():
    """Тестирует функцию deliver с декоратором"""
    my_randint = 21
    with patch.object(random, 'randint', return_value=my_randint):
        assert (
                deliver(Pepperoni()) == '🛵 Мы доставили вашу любимую' +
                ' пиццу Pepperoni 🍕 за 21 мин ⏳'
        )


def test_pickup_with_decorator():
    """Тестирует функцию pickup с декоратором"""
    my_randint = 18
    with patch.object(random, 'randint', return_value=my_randint):
        assert (
                pickup(Hawaiian()) == '🚘 Вы забрали вашу любимую' +
                ' пиццу Hawaiian 🍍 за 18 мин ⌛'
        )


def test_order_with_delivery():
    """Тестирует заказ в пиццерии"""
    my_randint_deliver = 17
    with patch.object(random, 'randint', return_value=my_randint_deliver):
        runner = CliRunner()
        result = runner.invoke(order, ['Margherita', '--delivery', '--size=L'])
        assert (
                '👨‍🍳 Мы приготовили вашу любимую пиццу' +
                ' Margherita 🧀 за 17 мин ⏳\n' +
                '🛵 Мы доставили вашу любимую пиццу' +
                ' Margherita 🧀 за 17 мин ⏳\n'
                in result.output
        )


def test_order_without_delivery():
    """Тестирует заказ в пиццерии"""
    my_randint_pickup = 9
    with patch.object(random, 'randint', return_value=my_randint_pickup):
        runner = CliRunner()
        result = runner.invoke(order, ['Pepperoni', '--size=L'])
        assert (
                '👨‍🍳 Мы приготовили вашу любимую пиццу' +
                ' Pepperoni 🍕 за 9 мин ⏳\n' +
                '🚘 Вы забрали вашу любимую пиццу' +
                ' Pepperoni 🍕 за 9 мин ⌛\n'
                in result.output
        )


def test_menu():
    """Тестирует вывод меню пиццерии"""
    runner = CliRunner()
    result = runner.invoke(menu)
    assert (
            result.output ==
            '- Margherita 🧀: tomato sauce, mozzarella, tomatoes\n' +
            '- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni\n' +
            '- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples\n'
    )
