import matplotlib.pyplot as plt


def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_dynamic(n):
    memo = {0: 0, 1: 1}
    
    def fib(n):
        if n not in memo:
            memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    
    return fib(n)


def generate_fibonacci_sequence(n, method='recursive'):
    sequence = []
    for i in range(n):
        if method == 'recursive':
            sequence.append(fibonacci_recursive(i))
        elif method == 'dynamic':
            sequence.append(fibonacci_dynamic(i))
    return sequence


def plot_fibonacci(sequence):
    plt.plot(sequence, marker='o', color='b', linestyle='-', markersize=5)
    plt.title("Числа Фибоначчи")
    plt.xlabel("Индекс")
    plt.ylabel("Значение")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    N = 20 
    fibonacci_seq_recursive = generate_fibonacci_sequence(N, method='recursive')
    fibonacci_seq_dynamic = generate_fibonacci_sequence(N, method='dynamic')

    print("Рекурсивный метод:", fibonacci_seq_recursive)
    print("Динамический метод:", fibonacci_seq_dynamic)
    
   
    plot_fibonacci(fibonacci_seq_dynamic)