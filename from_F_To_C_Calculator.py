# Convert Fahrenheit to Celsius (2.2.2)

def user_celcius():
    Celcius = int(input("please give me an amount in Celsius:\t"))# TODO query user for input temp in F
    Farenheit = (Celcius-32)/(9/5)# TODO convert input temp to C
    result = round(Farenheit,2) # TODO: round converted temp to places
    # TODO: print output

# TODO: execute function by calling it
    return(result)
    print(result)