def is_perfect(n):
    dzielnik = [1]
    suma = 0
    for i in range(1, n):
        if (n % i) == 0:
            dzielnik.append(i)
            suma += i
    if suma == n:
        return True
    else:
        return False


def get_perfect_numbers(n):
    result = []
    x = 1
    while len(result) != n:
        if is_perfect(x):
            result.append(x)
        x += 1
    return result
