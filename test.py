def prime():
    i = 0
    nr = 2
    while i <= 100:
        test = True
        for j in range(2, nr//2):
            if nr % j == 0:
                break
        if test:
            i += 1
        nr += 1
    return str(nr)

print(prime())