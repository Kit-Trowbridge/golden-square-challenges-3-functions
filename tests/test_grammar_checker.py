from lib.grammar_checker import *
"""
Given a blank text
It returns False
"""
def test_check_grammar_returns_false_for_empty_string():
    result = check_grammar("")
    assert result == False