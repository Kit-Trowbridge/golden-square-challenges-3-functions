
def estimate_reading_time(text):
    words = text.split()
    if len(words) % 50 == 0:
        return len(words) / 200