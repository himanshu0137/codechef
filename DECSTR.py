result = 'zyxwvutsrqponmlkjihgfedcba'
for i in range(input()):
    n = input()
    final = result * (n/25)
    if n % 25 != 0:
        final = result[25-(n%25):] + final
    print final