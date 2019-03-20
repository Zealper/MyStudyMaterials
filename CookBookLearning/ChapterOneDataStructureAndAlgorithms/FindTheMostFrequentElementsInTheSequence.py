words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not',
    'around', 'the', 'eyes', 'don\'t', 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', 'you\'re', 'under'
]

from collections import Counter


word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

more_words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
word_counts.update(more_words)
for word in more_words:
    word_counts[word] += 1

# Counter不为人知的特性
a = Counter(words)
b = Counter(more_words)
print(a+b)
