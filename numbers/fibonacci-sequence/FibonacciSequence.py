"""
Finds the fibonacci sequence to the nth number
"""
# def recursive_fibonacci(n):
#     """
#     finds the nth fibonacci number recursively
#     """
#     if n < 2:
#         return n
#     else:
#         return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def iterative_fibonacci(length):
    """
    iterative algorithm
    n = n-1 + n-2
    """
    i = 1
    j = 0

    for index in range(1, length + 1):
        temp = i + j
        i = j
        j = temp

    return j

def main():
    """
    main function
    """
    print("Enter the nth digit of the fibonacci sequence to find: ")
    length = input(" >>  ")

    print(iterative_fibonacci(int(length)))

    return

if __name__ == "__main__":
    main()
