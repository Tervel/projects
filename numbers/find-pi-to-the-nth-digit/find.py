# Spigot algorithm for finding the nth digit of pi
# based off Unbounded Spigot Algorithms for the Digits of Pi
# by Jeremy Gibbons[0]
# [0]www.cs.ox.ac.uk/people/jeremy.gibbons/publications/spigot.pdf

def findPi(length):
    piArray = [2] * length # Array of n length initialised with 2s

    # For each element in piArray
    for i in range(0, length):
        # Multiply all elements by 10
        for j in range(0, length):
            piArray[j] = piArray[j] * 10

        for k in range(length - 1, 0, -1):
            q = piArray[k] / (2 * k + 1)
            piArray[k] %= (2 * k + 1)
            piArray[k - 1] += q * k

        print(piArray[0]/10)
        piArray[0] %= 10

    # for i in piArray:
    #     print(i)

    return


def main():
    pi = findPi(1000)

    # print(3.141592653589793)
    # print (pi)


    return

if __name__ == "__main__":
    main()