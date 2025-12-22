def count_words(text):
    word_count = len(text.split())
    return word_count

def count_chars(text):
    count = sum(1 for c in text if not c.isspace())
    return count
