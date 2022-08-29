# - Write a program that can return factors of a number
def factors(n):
    list_factors = []
    for i in range(1, n+1):
        if n % i == 0:
            list_factors.append(i)
    return(list_factors)


print(factors(100))
