from typing import List
from collections import Counter


class CountVectorizer():
    def __init__(self):
        self.feature_names = []
        self.frequency = []
        self.corpus = []

    def fit(self, text_corpus: List[str]) -> None:
        features = []
        for index, text in enumerate(text_corpus):
            words_list = text.lower().split()
            self.frequency.append(Counter(words_list))
            self.corpus.append(words_list)
            for word in words_list:
                if word not in features:
                    features.append(word)
            self.feature_names = features

    def count_matrix(self) -> List[List[int]]:
        matrix = []
        for index, _ in enumerate(self.corpus):
            vector = []
            for feature in self.feature_names:
                vector.append(self.frequency[index][feature])
            matrix.append(vector)
        return matrix

    def fit_transform(self, text_corpus: List[str]) -> List[List[int]]:
        self.fit(text_corpus)
        return self.count_matrix()

    def get_feature_names(self) -> List[str]:
        return self.feature_names


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
