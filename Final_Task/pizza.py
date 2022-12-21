class Pizza:
    """Класс для всех пицц"""
    def __init__(self, add_ingredients: dict,
                 size: str = 'L', name: str = None):
        self.name = name
        self.size = size
        self.ingredients = {'tomato sauce': 200, 'mozzarella': 150}
        self.ingredients.update(add_ingredients)
        if self.size == 'XL':
            self.ingredients = \
                {k: 2 * ingred for k, ingred in self.ingredients.items()}

    def dict(self) -> dict:
        """Функция, возвращающая рецепт пиццы в виде словаря"""
        return self.ingredients

    def __eq__(self, other) -> bool:
        """Функция для сравнения двух пицц"""
        return self.ingredients == other.ingredients and \
            self.size == other.size


class Margherita(Pizza):
    """Класс для пиццы Маргариты"""
    def __init__(self, size: str = 'L'):
        self.name = 'Margherita 🧀'
        self.add_ingredients = {'tomatoes': 75}
        super().__init__(self.add_ingredients, size, self.name)


class Pepperoni(Pizza):
    """Класс для пиццы Пепперони"""
    def __init__(self, size: str = 'L'):
        self.name = 'Pepperoni 🍕'
        self.add_ingredients = {'pepperoni': 70}
        super().__init__(self.add_ingredients, size, self.name)


class Hawaiian(Pizza):
    """Класс для Гавайской пиццы"""
    def __init__(self, size: str = 'L'):
        self.name = 'Hawaiian 🍍'
        self.add_ingredients = {'chicken': 75, 'pineapples': 50}
        super().__init__(self.add_ingredients, size, self.name)
