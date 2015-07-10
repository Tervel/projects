# Spigot algorithm for finding the nth digit of pi
# based off Unbounded Spigot Algorithms for the Digits of Pi
# by Jeremy Gibbons[0] and digits of py by John Zelle[1]
# 
# [0] www.cs.ox.ac.uk/people/jeremy.gibbons/publications/spigot.pdf
# [1] mail.python.org/pipermail/edu-sig/2006-July/006810.html 

def findPi(length):
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    piArray = []

    while True:
        if 4*q+r-t < n*t:
            piArray.append(str(n)) # alternative to yield
            q, r, t, k, n, l = (10*q, 10*(r-n*t), t, k, (10*(3*q+r))//t-10*n, l)
        else:
            q, r, t, k, n, l = (q*k, (2*q+r)*l, t*l, k+1, (q*(7*k+2)+r*l)//(t*l), l+2)

        if len(piArray) == length:
            return piArray

def main():
    print("Enter number of digits of pi: ")
    length = input(" >>  ")

    piArray = findPi(int(length))
    piArray = piArray[:1] + ['.'] + piArray[1:]

    print ("".join(piArray))

    return

if __name__ == "__main__":
    main()