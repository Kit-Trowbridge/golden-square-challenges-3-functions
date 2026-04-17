from lib.reading_time_estimator import *

"""
Test 1
Given an empty string
It returns 0

"""
def test_estimate_reading_time_returns_0_for_empty_string():
    result = estimate_reading_time("")
    assert result == 0

"""
Test 2
Given a string of exactly 200 pure words
It returns 1
"""

def test_estimate_reading_time_returns_1_for_200_pure_words():
    result = estimate_reading_time(two_hundred_word_text_pure)
    assert result == 1

"""
Test 3
Given a string of exactly 50 pure words
It returns 0.25.
"""
def test_estimate_reading_time_returns_one_quarter_for_50_words():
    result = estimate_reading_time(fifty_word_text)
    assert result == 0.25

"""
Test 4
Given a string of exactly 100 words containing hyphenated words,
It returns 0.5
"""
def test_estimate_reading_time_returns_one_half_for_100_words_including_hyphens():
    result = estimate_reading_time(hundred_word_text_with_hyphens)
    assert result == 0.5

# Text variables:

# Test 2
two_hundred_word_text_pure = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way. In short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only. There were a king with a large jaw and a queen with a plain face, on the throne of England; there were a king with a large jaw and a queen with a fair face, on the throne of France. In both countries it was clearer than crystal to the lords of the State preserves of loaves and fishes, that things in general were settled for ever. It was the year of Our Lord one thousand seven hundred and seventy five."

# Test 3
fifty_word_text = "He was a man of about sixty, handsomely dressed, haughty in manner, and with a face like a fine mask. A face of a transparent paleness; every feature in it clearly defined; one set expression on it. The nose, beautifully formed otherwise, was very slightly pinched at the top of"

# Test 4
hundred_word_text_with_hyphens = "The passenger booked by this history, was on the coach-step, getting in; the two other passengers were close behind him, and about to follow. He remained on the step, half in the coach and half out of; they re-mained in the road below him. They all looked from the coachman to the guard, and from the guard to the coachman, and listened. The coachman looked back and the guard looked back, and even the emphatic leader pricked up his ears and looked back, without contradicting. The stillness consequent on the cessation of the rumbling and and labouring of the coach,"

# Test 6
two_hundred_word_text_em_dash = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way--in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only. There were a king with a large jaw and a queen with a plain face, on the throne of England; there were a king with a large jaw and a queen with a fair face, on the throne of France. In both countries it was clearer than crystal to the lords of the State preserves of loaves and fishes, that things in general were settled for ever. It was the year of Our Lord one thousand seven hundred and seventy-five. Spiritual"