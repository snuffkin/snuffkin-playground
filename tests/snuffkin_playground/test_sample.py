from snuffkin_playground.sample import sample

def test_sample():
    actual = sample()
    assert actual == "Hello"
    