def common_factors():
    c_f = []
    set_factors = []
    factors = []
    factors_to_get = [64, 128]
    for value in factors_to_get:
        for j in range(1, value + 1):
            if value % j == 0:
                factors.append(j)
    print("The factors between the numbers in", factors_to_get, "are", factors)
    for num in factors:
        if num not in set_factors:
            set_factors.append(num)
    # print(set_factors)

    for num_u in range(len(set_factors)):
        if factors.count(set_factors[num_u]) == len(factors_to_get):
            c_f.append(set_factors[num_u])
    print(c_f, "is the common factor between factors of", factors_to_get)

print(common_factors())


























