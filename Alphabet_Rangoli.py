def print_rangoli(size):
    width = 4 * size - 3
    lines = []
    for i in range(size - 1, -size, -1):
        k = abs(i)
        left = [chr(97 + j) for j in range(size - 1, k - 1, -1)]
        right = left[-2::-1]
        lines.append("-".join(left + right).center(width, "-"))
    print("\n".join(lines))
