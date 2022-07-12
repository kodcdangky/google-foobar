import decimal

D = decimal.Decimal
decimal.getcontext().prec = 102
TWO = D(2)
COMPLEMENTARY = TWO + TWO.sqrt()


def solution(s):
    if s == "0":
        return "0"

    n = int(s)
    largest = int(n * TWO.sqrt())
    complementary_highest_index = int(largest // COMPLEMENTARY)

    return str(
        (largest * (largest + 1)) // 2
        - complementary_highest_index * (complementary_highest_index + 1)
        - int(solution(str(complementary_highest_index)))
    )
