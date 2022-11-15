from one_hot_encoder import fit_transform
import unittest


class TestOneHotEncoder(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(fit_transform([]), [])

    def test_cities_list(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_cities_not_eq(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('Paris', [0, 1, 0]),
            ('Moscow', [0, 1, 0]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertNotEqual(transformed_cities, exp_transformed_cities)

    def test_cities_not_in(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        transformed = fit_transform(cities)
        self.assertNotIn('Paris', transformed)

    def test_empty_input(self):
        self.assertRaises(TypeError, fit_transform)


if __name__ == '__main__':
    unittest.main()