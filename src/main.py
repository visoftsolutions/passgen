from secrets import choice, randbelow

BASE58 = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
DIGITS = "123456789"
SPECIAL = "!@#$%^&*"


def random_permutation(l: list):
    l_len = len(l)
    for i in range(l_len):
        j = i + randbelow(l_len - i)
        t = l[j]
        l[j] = l[i]
        l[i] = t
    return l


def main():
    p = random_permutation([i for i in range(16)])
    result = [None for _ in range(len(p))]
    for i in range(0, 1):
        result[p[i]] = choice(SPECIAL)
    for i in range(1, 2):
        result[p[i]] = choice(DIGITS)
    for i in range(2, len(p)):
        result[p[i]] = choice(BASE58 + DIGITS + SPECIAL)
    print("".join(result))


if __name__ == "__main__":
    main()
