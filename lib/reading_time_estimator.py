
def estimate_reading_time_in_minutes(text):
    words = text.split()
    # 50 is 0.25 of 200
    if len(words) % 50 == 0:
        return len(words) / 200
    else:
        # need a way to round up to the nearest 0.25
        pass