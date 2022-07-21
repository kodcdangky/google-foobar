import decimal

decimal.getcontext().prec = 102
TWO = decimal.Decimal(2)
ORIGINAL = TWO.sqrt()
COMPLEMENTARY = ORIGINAL / (ORIGINAL - 1)


def solution(s):
    if s == "0":
        return "0"

    n = int(s)
    largest = int(n * ORIGINAL)
    complementary_highest_index = int(largest // COMPLEMENTARY)

    return str(
        (largest * (largest + 1)) // 2
        - complementary_highest_index * (complementary_highest_index + 1)
        - int(solution(str(complementary_highest_index)))
    )
