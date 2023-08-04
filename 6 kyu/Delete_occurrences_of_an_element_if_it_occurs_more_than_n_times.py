"""
https://www.codewars.com/kata/554ca54ffa7d91b236000023
"""


def delete_nth(order, max_e):
    occurrences = {}
    result = []
    for num in order:
        if num not in occurrences:
            occurrences[num] = 1
            result.append(num)
        elif occurrences[num] < max_e:
            occurrences[num] += 1
            result.append(num)
    return result
