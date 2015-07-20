"""
Find e to the Nth Digit
Based off nayuki.io/page/approximating-eulers-number-correctly
"""
def find_e(length):
    """
    Finds the value of E
    """
    precision = 7

    while True:
        result = find_e_precise(length, precision)
        precision += 2

        if result is not None:
            return result

    return

def find_e_precise(length, precision):
    """
    Finds the value of E after iterating for extra precision
    """
    full_scaler = 10 ** (length + precision)
    extra_scaler = 10 ** precision
    sum_low = 0
    sum_high = 0
    term_low = full_scaler
    term_high = full_scaler
    index = 0

    while term_low > 0:
        sum_low += term_low
        sum_high += term_high

        if index >= 1 and term_high < extra_scaler:
            sum_upper_bound = sum_high + term_high
            temp = divide_and_round(sum_low, extra_scaler)
            # if the divided and rounded sum low is equal to sum high, return as result
            if divide_and_round(sum_upper_bound, extra_scaler) == temp:
                string = str(temp)
                return string[ : len(string) - length] + "." + string[len(string) - length : ]

        index += 1
        term_low = term_low  // index
        term_high = term_high // index + 1

    return

def divide_and_round(num, div):
    """
    divide and round the number
    """
    quot = num // div
    rem = num % div

    if rem * 2 > div or (rem * 2 == div and quot & 1 == 1):
        quot += 1

    return quot

def main():
    """
    main function
    """
    print("Enter number of digits of e: ")
    length = input(" >>  ")

    print(find_e(int(length)))

    return

if __name__ == "__main__":
    main()
