from typing import List
from collections import Counter
from math import log


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

    def corpus_matrix(self) -> List[List[int]]:
        matrix = []
        for index, _ in enumerate(self.corpus):
            vector = []
            for feature in self.feature_names:
                vector.append(self.frequency[index][feature])
            matrix.append(vector)
        return matrix

    def fit_transform(self, text_corpus: List[str]) -> List[List[int]]:
        self.fit(text_corpus)
        return self.corpus_matrix()

    def get_feature_names(self) -> List[str]:
        return self.feature_names


class TfidfTransformer:
    def __init__(self):
        self.tf_matrix = []
        self.idf_matrix = []
        self.tfidf_matrix = []

    def tf_transform(self, count_matrix: List[int]) -> List[List[int]]:
        if len(count_matrix) > 0:
            for row in count_matrix:
                row_sum = sum(row)
                tf_row = [round(el / row_sum, 3) for el in row]
                self.tf_matrix.append(tf_row)
        return self.tf_matrix

    def idf_transform(self, count_matrix: List[int]) -> List[List[int]]:
        if len(count_matrix) > 0:
            total = len(count_matrix) + 1
            transposed_matrix = list(map(list, zip(*count_matrix)))
            self.idf_matrix = [1 + round(log(total / (sum(map(bool, doc)) + 1)), 1) for doc in transposed_matrix]
        return self.idf_matrix

    def fit_transform(self, count_matrix: List[int]) -> List[List[int]]:
        for vector in self.tf_transform(count_matrix):
            res = [round(tf * idf, 3) for tf, idf in zip(vector, self.idf_transform(count_matrix))]
            self.tfidf_matrix.append(res)
        return self.tfidf_matrix


class TfidfVectorizer(CountVectorizer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tfidf_transformer = TfidfTransformer()

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        matrix = super().fit_transform(corpus)
        return self.tfidf_transformer.fit_transform(matrix)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    print('Задание #1: count vectorizer')
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix, '\n')

    print('Задание #2: term frequency')
    transformer = TfidfTransformer()
    tf_matrix = transformer.tf_transform(count_matrix)
    print(tf_matrix, '\n')

    print('Задание #3: inverse document-frequency')
    transformer = TfidfTransformer()
    idf_matrix = transformer.idf_transform(count_matrix)
    print(idf_matrix, '\n')

    print('Задание #4: tf-idf transformer')
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    print(tfidf_matrix, '\n')

    print('Задание #5: tf-idf vectorizer')
    vectorizer = TfidfVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
