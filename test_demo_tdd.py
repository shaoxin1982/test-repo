from demo_tdd import backwards_allcaps


def test_backwards_allcaps_lower_case():
    assert backwards_allcaps("pycon") == "NOCYP"


def test_backwards_allcaps_camel_case():
    assert backwards_allcaps("Cleveland") == "DNALEVELC"


def test_backwards_allcaps_space_between():
    assert backwards_allcaps("New York City") == "YTICKROYWEN"