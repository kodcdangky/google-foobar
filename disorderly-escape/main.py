from copy import deepcopy
from fractions import Fraction


class polynomial(list):
    """
    Represents polynomials as a list of list, supports addition and multiplication
    """

    def __init__(self, expression):
        self = super(polynomial, self).__init__(expression)

    def __add__(self, other):
        poly_sum = deepcopy(self).extend(other)
        polynomial.condense(poly_sum)
        return poly_sum

    def __iadd__(self, other):
        self.extend(other)
        polynomial.condense(self)
        return self

    def __mul__(self, other):
        poly_product = []
        other_copy = deepcopy(other)
        for elem in self:
            for elem_other in other_copy:
                if len(elem) < len(elem_other):
                    elem.extend(0 for _ in range(len(elem_other) - len(elem)))
                elif len(elem_other) < len(elem):
                    elem_other.extend(0 for _ in range(len(elem) - len(elem_other)))

                new_elem = [elem[0] * elem_other[0]]
                for i_elem, i_other in zip(
                    range(1, len(elem)), range(1, len(elem_other))
                ):
                    new_elem.append(elem[i_elem] + elem_other[i_other])
                poly_product.append(new_elem)

        polynomial.condense(self)
        polynomial.condense(poly_product)
        return poly_product

    @classmethod
    def condense(cls, poly):
        """
        Condenses polynomial expression by merging exponent groups, then sort descending by exponents

        Args:
            poly (list): variable groups
        """
        for i, elem_i in zip(reversed(range(len(poly) - 1)), reversed(poly[:-1])):
            if elem_i[0] == 0:
                poly.pop(i)
                continue
            while elem_i[-1] == 0:
                elem_i.pop()
            for j, elem_j in zip(reversed(range(len(poly))), reversed(poly[i + 1 :])):
                if elem_i[1:] == elem_j[1:]:
                    elem_i[0] += elem_j[0]
                    poly.pop(j)
        polynomial.sort(poly)

    @classmethod
    def sort(cls, poly):
        poly = sorted(poly, key=lambda elem: sum(elem[1:]), reverse=True)


def new_gcd_table(n):
    """
    Returns a new greatest common divisor table between integers from 1 to n for constant time look up
    """
    gcd_table = [[None for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(i, n + 1):
            if i == j == 0:
                continue
            if 0 in (i, j):
                gcd_table[i][j] = gcd_table[j][i] = max(i, j)
            elif 0 in (i % j, j % i):
                gcd_table[i][j] = gcd_table[j][i] = min(i, j)
            else:
                gcd_table[i][j] = gcd_table[j][i] = gcd_table[min(i, j)][
                    max(i, j) % min(i, j)
                ]
    return gcd_table


def new_ci_table(n):
    """
    Returns a new cycle index table for symmetric groups from S1 to Sn
    """
    table = [polynomial([[1]])]
    for i in range(1, n + 1):
        new_cycle_index = polynomial([])
        for j in range(1, i + 1):
            sj = [[1]]
            sj[-1].extend(0 for _ in range(j - 1))
            sj[-1].append(1)

            new_cycle_index += polynomial(sj) * table[i - j]
        new_cycle_index *= polynomial([[Fraction(1, i)]])
        table.append(new_cycle_index)
    return table


def solution(w, h, s):
    def weixu(poly1, poly2):
        """
        Returns the unweighted Wei-Xu product of cycle indices as described in this paper, page 182-183
        https://pdf.sciencedirectassets.com/271536/1-s2.0-S0012365X00X02592/1-s2.0-0012365X9390015L/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCO3O%2BqWcPEiHfjEQcx5ReeIJcWSS4bnS62k9cEneVRFQIhALpSjWwgEQ7tNnMMYmkXepagb4RiU2kmeEFS142a%2Fx7YKtsECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQBBoMMDU5MDAzNTQ2ODY1IgyL%2BHF6k171iodd7g4qrwQvkWtme06auCrZ%2FCnIuYvAqSNO6JukcpL0F9AChxV1orWSng2sF5WgWdlrWNDRhNNxGZbrX8iLxLll7usSBgkyMWZgXBBS7vubVL%2BdKkvDWfItAWebHzLVtqbK0ImIum6LWUV1SEqrqSTR6dH01%2Bj20vxQlQC7NPoKl9VG0%2Bxuied8jZiR360Kiwzpka8T4pc%2BBrXpUkRXKumBBAVDeCX81jlefeYhAh5nqiHPInUSH6t3bBC6lSXkgjdLHnAoGPIMQ6%2Fw1bi51s8dppOZpU94ltdrJuu8PcHCgReTuk%2FHQJnTJYbzG63ZtGGe%2Boet1OKe7T9U%2F%2F60qPh2eZs3QVtSc4RpUNWJmQqAP6Vf9L2E12JJ8PhBWeqLMA%2B%2BaHZMqyh3ISO8EzEt%2BMmWifnFHgdiqlbl%2FUwkgmLt2ooVTK10TPkQ17Fs7HAsSkxeLQS%2ByTxyfbz7qJkHap2HCSOe5cQV53HzWN0PDVnPaigyydkUU0dDPUXeBqDF7e0zkTvI3Zh4oMdZb9jXR%2FBq8fGmSPELVbUemig4J4t0BHlJBKbiVC4XBy9A9yuLoIim54SgGrsqIJ64zRWHE2i%2BUw5BepK9Tq%2BNsaIVeIzHdkZpTvRY9d3o2gdqcVemV4EA7CjBHNluN8ImQAE0qDbR08QrNJWfjtb%2BzdzFjhr6KldHD0YtoIu0eq1LaoxYeIOOMwspDcoT%2BssNlvkzgSalASTj7jv0VURF3Gn7nfTMN5mQ3%2BdgMIWkkZQGOqgB4SeGMQfwCJzXQR9xPRB%2FomAS7dHkdad3RoIhZ2K0%2BCqHJdlGh63sKywuuchAazAk0uHbQEn9SAAYdwl4gEmtVsYAFGjpT23aVKzNpmNwng7vV5WnlnCVRXbrLuK0EGeA1htWvK0bNegy%2BmZ0fcMrh9yRhCxNRYet7amU8Hnc0pE1%2B85HZR5lsxCmMwESWi7px53%2Bw1Ih44kW1UFG0%2F%2B7HI03ux9m6Cd1&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220518T025514Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYTVGJFU2H%2F20220518%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=d51a5282e680116916ef98cc65ade02d3bea6cddcca08a5367bf8203325488ac&hash=80ddb80f5f069ff44d7202c573e16d5c1c106edba2e6320c351af4d316e20430&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=0012365X9390015L&tid=spdf-9e7a38fa-0f8b-48f0-ba2a-ab043ad2d018&sid=10d99f334689c947c02a6876ef5aa7dd183egxrqb&type=client&ua=4d54005251505e54510d&rr=70d150117c2a5640#page=1&zoom=auto,-11,763
        """
        prod = []
        for elem1 in poly1:
            for elem2 in poly2:
                prod.append([elem1[0] * elem2[0], 0])
                for i, power1 in enumerate(elem1[1:], start=1):
                    for j, power2 in enumerate(elem2[1:], start=1):
                        prod[-1][1] += gcd_table[i][j] * power1 * power2
        return prod

    gcd_table = new_gcd_table(max(w, h))
    ci_table = new_ci_table(max(w, h))
    ci_prod = weixu(ci_table[w], ci_table[h])
    return str(sum(coeff * (s**power) for coeff, power in ci_prod))
