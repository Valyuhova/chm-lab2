def read_row(prompt, n):
    while True:
        try:
            values = list(map(float, input(prompt).split()))
            if len(values) != n:
                raise ValueError(f"Потрібно ввести {n} чисел.")
            return values
        except ValueError:
            print("Помилка вводу! Спробуйте ще раз.")


def check_diagonal_dominance(A):
    n = len(A)
    for i in range(n):
        diag = abs(A[i][i])
        s = sum(abs(A[i][j]) for j in range(n) if j != i)
        if diag <= s:
            print("\nМатриця не задовольняє умову діагональної переваги!")
            exit()


def make_iteration_matrix(A, n):
    B = []
    for i in range(n):
        if A[i][i] == 0:
            print("Діагональний елемент дорівнює нулю — розрахунок неможливий.")
            exit()
        row = []
        for j in range(n):
            if i == j:
                row.append(0)
            else:
                row.append(-A[i][j] / A[i][i])
        B.append(row)
    return B


def find_norm(B):
    norm_val = 0
    for row in B:
        row_sum = sum(abs(x) for x in row)
        norm_val = max(norm_val, row_sum)
    if norm_val >= 1:
        print("Попередження: умова збіжності не виконується.")
        exit()
    return norm_val


def compute_free_vector(A, b):
    return [b[i] / A[i][i] for i in range(len(A))]


def iterate(B, c, x_prev, n, norm, eps, iteration):
    x_new = x_prev[:]
    max_diff = 0
    for i in range(n):
        new_val = c[i] + sum(B[i][j] * x_new[j] for j in range(n) if j != i)
        delta = abs(new_val - x_new[i])
        max_diff = max(max_diff, delta)
        x_new[i] = new_val
    err = max_diff * norm / (1 - norm)
    return x_new, err <= eps, iteration + 1, err


def main():
    while True:
        try:
            n = int(input("Введіть розмірність матриці: "))
            break
        except ValueError:
            print("Помилка. Введіть ціле число.")

    A = []
    print("\nВведіть коефіцієнти матриці:")
    for i in range(n):
        A.append(read_row(f"Рядок {i + 1}: ", n))

    b = read_row(f"\nВведіть вектор вільних членів ({n} чисел): ", n)

    print("\nРозширена матриця:")
    for i in range(n):
        print("[", " ".join(f"{val:7.3f}" for val in A[i]), f"| {b[i]:7.3f} ]")

    check_diagonal_dominance(A)
    B = make_iteration_matrix(A, n)
    c = compute_free_vector(A, b)
    norm_val = find_norm(B)

    while True:
        try:
            eps = float(input("\nВведіть точність ε: "))
            break
        except ValueError:
            print("Помилка: введіть число.")

    x = c[:]
    k = 0

    while True:
        x, ok, k, err = iterate(B, c, x, n, norm_val, eps, k)
        if ok:
            break

    print("\nРезультати:")
    for i, val in enumerate(x):
        print(f"x{i + 1} = {val:9.5f}")
    print(f"Кількість ітерацій: {k}")
    print(f"Оцінка похибки: {err:.6e}")


if __name__ == "__main__":
    main()
