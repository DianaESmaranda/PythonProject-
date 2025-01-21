def unique_pair_sum(numbers, target):
    # Folosim un set pentru a stoca perechile unice
    pairs = set()
    seen = set()

    for num in numbers:
        complement = target - num
        if complement in seen:
            # Asigurăm ordinea (a <= b) în perechi
            pair = (min(num, complement), max(num, complement))
            pairs.add(pair)
        seen.add(num)

    return pairs
