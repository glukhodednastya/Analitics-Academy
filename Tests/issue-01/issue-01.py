from morse import encode
import doctest


def encode_test(message):
    """
    >>> encode_test('SOS')
    '... --- ...'
    >>> encode_test('sos')
    Traceback (most recent call last):
    KeyError: 's'
    >>> encode_test('SO  S') # doctest: +NORMALIZE_WHITESPACE
    '... --- ...'
    >>> encode_test('SSSSSS') # doctest: +ELLIPSIS
    '... ... ...'
    >>> encode_test('SSS  SS') # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    '... ... ...'
    >>> encode_test(000)
    Traceback (most recent call last):
    TypeError: 'int' object is not iterable
    """

    return encode(message)


if __name__ == '__main__':
    doctest.testmod()
