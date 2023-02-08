from keyword import iskeyword
import json


class JSONtoObject:
    def __init__(self, data):
        for key, value in data.items():
            if iskeyword(key):
                key += '_'
            if isinstance(value, dict):
                self.__dict__[key] = JSONtoObject(value)
            else:
                self.__dict__[key] = value


class ColorizeMixin:
    def __init__(self):
        self.style = 1
        self.text_color = 33
        self.background_color = '40m'

    def __str__(self):
        text = self.__repr__()
        return f"\033[{self.style};{self.text_color};{self.background_color} {text} \033[m"


class Advert(ColorizeMixin):
    def __init__(self, df):
        super().__init__()
        self.__dict__.update(JSONtoObject(df).__dict__)

    @property
    def price(self):
        if 'price' in self.__dict__ and self.__dict__['price'] > 0:
            return self.__dict__['price']
        elif 'price' in self.__dict__ and self.__dict__['price'] < 0:
            raise ValueError('must be >= 0')
        return 0

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('must be >= 0')
        self.price = value

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == "__main__":
    test1 = """{
        "title": "iPhone X",
        "price": 100,
        "location": {
        "address": "город Самара, улица Мориса Тореза, 50",
        "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }"""
    advert_test1 = Advert(json.loads(test1))
    print(advert_test1.title)
    print(advert_test1.price)
    print(advert_test1.location.address)
    print(advert_test1)

    test2 = """{
           "title": "Вельш-корги",
           "price": 1000,
           "class": "dogs",
           "location": {
           "address": "Москва, 25"
           }
       }"""
    advert_test2 = Advert(json.loads(test2))
    print(advert_test2.class_)
    print(advert_test2)

    test3 = """{
            "title": "python", 
            "price": -1
        }"""
    advert_test3 = Advert(json.loads(test3))
    print(advert_test3)
