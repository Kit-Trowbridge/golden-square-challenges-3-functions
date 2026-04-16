from lib.personal_diary import *

# given a string of "hello", count_words() returns 1

def test_count_words_returns_1_when_string_is_1_word():
    result = count_words("Hello")   
    assert result == 1

# given a string of "hello", count_words() returns 1

def test_count_words_returns_2_when_string_is_2_words():
    result = count_words("Hello there")   
    assert result == 2

# given a string of "Hello", make_snippet returns "Hello"
def test_make_snippet_returns_string_when_given_1_word_string():
    result = make_snippet("Hello")
    assert result == "Hello"

def test_make_snippet_returns_string_when_given_5_word_string():
    result = make_snippet("The quick brown fox jumps")
    assert result == "The quick brown fox jumps"
