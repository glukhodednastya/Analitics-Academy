from one_hot_encoder import fit_transform
import pytest


def test_empty_list():
    assert fit_transform([]) == []


def test_cities_list():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert fit_transform(cities) == exp_transformed_cities


def test_cities_not_eq():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('Paris', [0, 1, 0]),
        ('Moscow', [0, 1, 0]),
        ('London', [1, 0, 0]),
    ]
    assert fit_transform(cities) != exp_transformed_cities


def test_cities_not_in():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    assert 'Paris' not in fit_transform(cities)


def test_empty_input():
    with pytest.raises(TypeError):
        assert fit_transform()
