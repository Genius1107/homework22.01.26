#10

def min_flips(states):
    """
    states — итерируемый объект с состояниями монет:
    0 для решки, 1 для герба (или любые два символа, но тогда нужно считать один из них)
    Функция возвращает минимальное число переворотов.
    """
    ones = sum(1 for s in states if s == 1)
    zeros = sum(1 for s in states if s == 0)
    return min(ones, zeros)

# Пример использования из ввода
if __name__ == "__main__":
    n = int(input().strip())
    # допустим, следующие n чисел — 0 или 1, разделённые пробелами
    coins = list(map(int, input().split()))
    print(min_flips(coins))
#11

# Читаем S и P из ввода (в одной строке или в двух)
S, P = map(int, input().split())

def find_pair(S, P):
    # Ограничения натуральные числа: X, Y >= 1 и <= 1000
    for X in range(1, min(1000, S-1) + 1):
        Y = S - X
        if 1 <= Y <= 1000 and X * Y == P:
            return X, Y
    return None

res = find_pair(S, P)
if res:
    print(res[0], res[1])
else:
    print("Решений нет")
#14

N = int(input())

val = 1
while val <= N:
    print(val, end=' ')
    val *= 2
print()
