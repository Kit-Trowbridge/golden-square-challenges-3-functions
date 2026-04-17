from lib.make_snippet import *

# given a string of "Hello", make_snippet returns "Hello"
def test_make_snippet_returns_string_when_given_1_word_string():
    result = make_snippet("Hello")
    assert result == "Hello"

# given a string of five words or less, make_snippet returns the string as it is
def test_make_snippet_returns_string_when_given_5_word_string():
    result = make_snippet("The quick brown fox jumps")
    assert result == "The quick brown fox jumps"

# given a string of more than five words, make_snippet returns the first 5 then "..."
def test_make_snippet_returns_shortened_string():
    result = make_snippet("The quick brown fox jumps over the lazy dog.")
    assert result == "The quick brown fox jumps..."