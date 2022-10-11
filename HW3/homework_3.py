from typing import List

class CountVectorizer():
    def __init__(self):
        self.feature_names = list()

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        feature_names = [word.lower() for sent in corpus for word in sent.split()]
        self.feature_names = list(feature_names)
        return self.count_matrix(corpus)

    def count_matrix(self, corpus: List[str]) -> List[List[int]]:
        matrix = list()
        for sent in corpus:
            matrix.append([])
            for word in self.feature_names:
                sent_words = [word.lower() for word in sent.split()]
                matrix[-1].append(sent_words.count(word))
        return matrix

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

