import re
from collections import Counter
from google.colab import files

# Step 1: Create and save the file

file_name = "sample.txt"
text_content = """Python is fun and versatile.
Learning Python step by step.
Python is simple, yet powerful and simple.
"""

with open(file_name, 'w', encoding='utf-8') as f:
    f.write(text_content)

print(f"File '{file_name}' has been saved in Colab environment!")

# Step 2: Analyze the file
try:
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()

    # Count lines
    num_lines = text.count('\n') + 1  # count lines manually

    # Count words using regex
    words = re.findall(r'\b\w+\b', text.lower())
    num_words = len(words)

    # Count characters
    num_chars = len(text)

    # Word frequency
    word_freq = Counter(words)
    most_common_words = word_freq.most_common(10)

    # Display results
    print("\n----- Text Analysis -----")
    print(f"Lines: {num_lines}")
    print(f"Words: {num_words}")
    print(f"Characters: {num_chars}")
    print("\nMost Common Words:")
    for word, freq in most_common_words:
        print(f"{word}: {freq}")

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")

# Step 3: Download the file (optional)

files.download(file_name)
