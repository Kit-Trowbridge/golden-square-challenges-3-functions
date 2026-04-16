from lib.personal_diary import *

# given a string of "hello", count_words() returns 1

def test_count_words_returns_1_when_string_is_1_word():
    result = count_words("Hello")   
    assert result == 1
