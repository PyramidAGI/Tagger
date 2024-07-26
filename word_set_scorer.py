import csv
from collections import Counter

def load_word_sets(file_path):
    word_sets = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)  # Skip header
        for row in reader:
            tag = row[0]
            words = set(word.lower() for word in row[1:] if word)
            word_sets[tag] = words
    return word_sets

def score_sentence(sentence, word_sets):
    words = sentence.lower().split()
    word_counts = Counter(words)
    
    scores = {}
    for tag, word_set in word_sets.items():
        score = sum(word_counts[word] for word in word_set if word in word_counts)
        scores[tag] = score
    
    return scores

def main():
    word_sets = load_word_sets('tags.csv')
    
    while True:
        sentence = input("Enter a sentence (or 'quit' to exit): ")
        if sentence.lower() == 'quit':
            break
        
        scores = score_sentence(sentence, word_sets)
        if scores:
            highest_scoring_tag = max(scores, key=scores.get)
            print(f"Highest scoring tag: {highest_scoring_tag}")
        else:
            print("No matching tags found.")

if __name__ == "__main__":
    main()