from load import load_words
import vectors as v


def find_word(text, words):
    try:
        return next(w for w in words if text == w.text)
    except StopIteration:
        return None


def most_similar(base_vector, words):
    """Finds n words with smallest cosine similarity to a given word
    returns a List[Tuple[float, Word]]"""
    words_with_distance = [(v.cosine_similarity_normalized(base_vector, w.vector), w) for w in words]
    # We want cosine similarity to be as large as possible (close to 1)
    sorted_by_distance = sorted(words_with_distance, key=lambda t: t[0], reverse=True)
    return sorted_by_distance


def closest_analogies(left2, left1, right2, words):
    """ returns a List[Tuple[float, Word]] """
    word_left1 = find_word(left1, words)
    word_left2 = find_word(left2, words)
    word_right2 = find_word(right2, words)
    if (not word_left1) or (not word_left2) or (not word_right2):
        return []
    vector = v.add(
        v.sub(word_left1.vector, word_left2.vector),
        word_right2.vector)
    closest = most_similar(vector, words)[:10]

    def is_redundant(word: str) -> bool:
        """
        Sometimes the two left vectors are so close the answer is e.g.
        "shirt-clothing is like phone-phones". Skip 'phones' and get the next
        suggestion, which might be more interesting.
        """
        word_lower = word.lower()
        return (
                left1.lower() in word_lower or
                left2.lower() in word_lower or
                right2.lower() in word_lower)

    closest_filtered = [(dist, w) for (dist, w) in closest if not is_redundant(w.text)]
    return closest_filtered


def print_analogy(left2, left1, right2, words):
    analogies = closest_analogies(left2, left1, right2, words)
    if len(analogies) == 0:
        print(f"{left2}-{left1} is like {right2}-?")
    else:
        (dist, w) = analogies[0]
        # alternatives = ', '.join([f"{w.text} ({dist})" for (dist, w) in analogies])
        print(f"{left2}-{left1} is like {right2}-{w.text}")


def analogies_interactive():
    def read_word() -> str:
        return input("Type a word: ")

    while True:
        left2 = input("Type a word: ")
        left1 = input("is to ..")
        right2 = input("Like ..")
        analogies = closest_analogies(left2, left1, right2, words)
        print("is to ", (analogies[0][1] if 0 < len(analogies) else left1))


if __name__ == "__main__":
    words = load_words('vec/vectors50k.vec')
    print_analogy('man', 'him', 'woman', words)
    analogies_interactive()
