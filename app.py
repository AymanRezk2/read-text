import nltk
from nltk.corpus import stopwords
from collections import Counter

# Read the contents of the file
with open("/app/paragraphs.txt") as file:
    text = file.read()

# Tokenize the text
words = nltk.word_tokenize(text)

# Remove stop words
stop_words = set(stopwords.words("english"))
filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

# Count word frequency
word_freq = Counter(filtered_words)

# Display word frequency count
for word, freq in word_freq.items():
    print(f"{word}: {freq}")

# Example of using inspect.signature (optional)
if __name__ == "__main__":
    import inspect

    def my_function(text, stop_words):
        words = nltk.word_tokenize(text)
        # ... rest of the code ...

    signature = inspect.signature(my_function)
    print(f"Function signature: {signature}")
