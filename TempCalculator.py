# Basic Temperature Calculator

def user_celcius():
    Celcius = int(input("please give me an amount in Celsius:\t"))# query user for input temp in F
    Farenheit = (Celcius-32)/(9/5)#  convert input temp to C
    result = round(Farenheit,2) #  round converted temp to places
    print(result)  #print convertion
    return() #return to make function be valid
user_celcius() #call function