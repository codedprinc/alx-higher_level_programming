#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lt = sorted(dir(hidden_4).copy())
    for y in lt:
        if "__" != y[:2]:
            print(y)
