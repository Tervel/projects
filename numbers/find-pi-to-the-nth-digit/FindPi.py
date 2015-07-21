"""
Spigot algorithm for finding the nth digit of pi
based off Unbounded Spigot Algorithms for the Digits of Pi
by Jeremy Gibbons[0] and Digits of Pi by John Zelle[1]

[0] www.cs.ox.ac.uk/people/jeremy.gibbons/publications/spigot.pdf
[1] mail.python.org/pipermail/edu-sig/2006-July/006810.html
"""

def find_pi(length):
    """
    Spitgot algorithm to find pi
    """
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    pi_array = []

    while True:
        if 4*q+r-t < n*t:
            pi_array.append(str(n)) # alternative to yield
            q, r, t, k, n, l = (10*q, 10*(r-n*t), t, k, (10*(3*q+r))//t-10*n, l)
        else:
            q, r, t, k, n, l = (q*k, (2*q+r)*l, t*l, k+1, (q*(7*k+2)+r*l)//(t*l), l+2)

        if len(pi_array) == length:
            return pi_array

def main():
    """
    Get user input and append find_pi output onto output string
    """
    print("Enter number of digits of pi: ")
    length = input(" >>  ")

    pi_array = find_pi(int(length))
    pi_array = pi_array[:1] + ['.'] + pi_array[1:]
    print("".join(pi_array))

    return

if __name__ == "__main__":
    main()
