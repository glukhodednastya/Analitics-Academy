from morse import decode
import pytest


@pytest.mark.parametrize('s,exp', [
    ('... --- ...', 'SOS'),
    ('.- ...- .. - ---', 'AVITO'),
    ('----- ----- -----', '000'),
    ('-....- ..--.. -....-', '-?-')
])
def test_decode(s, exp):
    assert decode(s) == exp
