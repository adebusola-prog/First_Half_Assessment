# Write a program that takes an integer between 0 and 1 million and returns the word equivalent

def number(num):
    f = {0:"zero", 1:"one", 2: "two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine",
        10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14: "fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 
        18:"eighteen", 19: "nineteen", 20:"twenty", 30:"thirty", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy", 80: "eighty",
        90:"ninety"}

    million = 1000000
    thousand = 1000
    
    


    if num in f:
        return (f[num])
    else:
        if num < 100:
            return(f[num//10*10] + " " + f[num%10])
        elif 100 < num < thousand:
            if num % 100 == 0:
                return (f[num//100] + " " + "hundred")
            else:
                return (f[num//100] + " hundred and " + number(num%100))
        elif num < thousand * 1000:
            if num % 100 == 0:
                return number(num//1000) + ' thousand '
            else:
                return number(num//1000) + ' thousand ' + number(num % 1000)
        elif 1000000 <= num < 1000000000: 
            if num % 100 == 0:
                return(number(num//1000000)) + ' million'
            else:
                return (number(num//1000000)) + ' million' + ' ' +  number(num % 1000000)
            
        
              

n = int(input("enter a number"))
print(number(n))