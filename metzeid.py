def input_matrix(n):
    A = []
    print("Введіть елементи матриці A (по рядках, через пробіл):")
    for i in range(n):
        row = list(map(float, input(f"Рядок {i + 1}: ").split()))
        A.append(row)
    return A

def input_vector(n, name="B"):
    vec = list(map(float, input(f"Введіть елементи матриці {name} ({n} чисел через пробіл): ").split()))
    return vec

def check_convergence(A):
    n = len(A)
    for i in range(n):
        diag = abs(A[i][i])
        sum_row = sum(abs(A[i][j]) for j in range(n) if j != i)
        if diag <= sum_row:
            print(f"Рядок {i+1}: |A[{i+1},{i+1}]| ≤ сума інших елементів ({diag:.3f} ≤ {sum_row:.3f})")
            return False
    return True

def gauss_seidel(A, B, eps=1e-4, max_iter=1000):
    n = len(A)
    x = [0.0] * n
    print("\nІтерації:")

    for k in range(1, max_iter + 1):
        x_old = x.copy()

        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(i))
            s2 = sum(A[i][j] * x_old[j] for j in range(i + 1, n))
            x[i] = (B[i] - s1 - s2) / A[i][i]

        diff = max(abs(x[i] - x_old[i]) for i in range(n))
        print(f"Ітерація {k}: {['%.6f' % xi for xi in x]}   Δ={diff:.6e}")

        if diff < eps:
            print("\nМетод збігся!")
            return x, k

    print("\nМетод не збігся за максимальну кількість ітерацій.")
    return x, max_iter

if __name__ == "__main__":
    n = int(input("Введіть розмірність системи (n): "))

    A = input_matrix(n)
    B = input_vector(n, "B")

    print("\nПеревірка умови збіжності:")
    if check_convergence(A):
        print("Виконується умова строгої діагональної переваги — метод повинен збігатись.")
    else:
        print("Строга діагональна перевага не виконується — метод може не збігтись!")

    eps = float(input("\nВведіть точність: "))

    x, iters = gauss_seidel(A, B, eps)

    print("\nРозв’язок системи:")
    for i, val in enumerate(x, start=1):
        print(f"x{i} = {val:.6f}")
    print(f"Кількість ітерацій: {iters}")
