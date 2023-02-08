class BasePokemon:
    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category

    def __str__(self):
        return f'{self.name}/{self.category}'


class EmojiMixin:
    emojies = {
        'grass': '🌿',
        'fire': '🔥',
        'water': '🌊',
        'electric': '⚡'
    }

    def __str__(self):
        text: str = super().__str__()
        for category, emoji in self.emojies.items():
            replaced = text.replace(category, emoji)
            if replaced != text:
                return replaced
        return text


class Pokemon(EmojiMixin, BasePokemon):
    pass


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur', category='grass')
    print(bulbasaur)
    pikachu = Pokemon(name='Pikachu', category='electric')
    print(pikachu)

