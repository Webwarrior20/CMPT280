from collections import Counter

def word_count(text):
    return Counter(text.lower().split())

if __name__ == "__main__":
    print(word_count("Hello world hello world world"))
