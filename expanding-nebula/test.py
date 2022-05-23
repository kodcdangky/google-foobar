def test():
    from main import solution

    input = [[True, False, True], [False, True, False], [True, False, True]]
    output = solution(input)
    print(output)
    assert output == 4

    input = [
        [True, True, False, True, False, True, False, True, True, False],
        [True, True, False, False, False, False, True, True, True, False],
        [True, True, False, False, False, False, False, False, False, True],
        [False, True, False, False, False, False, True, True, False, False],
    ]
    output = solution(input)
    print(output)
    assert output == 11567

    input = [
        [True, False, True, False, False, True, True, True],
        [True, False, True, False, False, False, True, False],
        [True, True, True, False, False, False, True, False],
        [True, False, True, False, False, False, True, False],
        [True, False, True, False, False, True, True, True],
    ]
    output = solution(input)
    print(output)
    assert output == 254

    input = [[False for _ in range(50)] for _ in range(9)]
    print(solution(input))


test()
