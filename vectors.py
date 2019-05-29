import math


def l2_len(v):
    return math.sqrt(sum([x * x for x in v]))


def dot(v1, v2):
    assert len(v1) == len(v2)
    return sum([x * y for (x, y) in zip(v1, v2)])


def add(v1, v2):
    assert len(v1) == len(v2)
    return [x + y for (x, y) in zip(v1, v2)]


def sub(v1, v2):
    assert len(v1) == len(v2)
    return [x - y for (x, y) in zip(v1, v2)]


def normalize(v):
    l2 = l2_len(v)
    return [x / l2 for x in v]


def cosine_similarity_normalized(v1, v2) -> float:
    """
    Returns the cosine of the angle between the two vectors.
    Each of the vectors must have length (L2-norm) equal to 1.
    Results range from -1 (very different) to 1 (very similar).
    """
    return dot(v1, v2)
