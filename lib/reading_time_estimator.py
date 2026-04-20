
def estimate_reading_time_in_minutes(text):
    words = text.split()
    # 50 is 0.25 of 200
    number_of_words = len(words)
    if number_of_words % 50 == 0:
        return number_of_words / 200
    else:
        import math
        # rounds up to the nearest 0.25 minutes
        return math.ceil(number_of_words / 200 * 4) / 4