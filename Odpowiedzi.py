import decimal

# Zadanie 1.
def postcode_gen(postcode_1 = "79-900", postcode_2 = "80-155"):
    
    list_of_postcodes = []

    # Convert a postcode into an integer e.g. "80-004" -> 80004.
    postcode_1 = int(postcode_1[:2] + postcode_1[3:])
    postcode_2 = int(postcode_2[:2] + postcode_2[3:])
    
    # Finding the range of the list:
    smaller_postcode = min(postcode_1, postcode_2)
    greater_postcode = max(postcode_1, postcode_2)
    
    # Create appropriate postcodes and add them to the list:
    while smaller_postcode + 1 < greater_postcode:
        smaller_postcode += 1
        list_of_postcodes.append(str(smaller_postcode)[:2] + '-' + str(smaller_postcode)[2:])
        
    return list_of_postcodes

# Zadanie 2.
def list_checker(a_list, n):
    return [(number + 1) for number in range(n) if (number + 1) not in a_list]

# Zadanie 3.
def number_generator(n = 2,m = 5.5):
    list_of_numbers = []
    while (n <= m):
        list_of_numbers.append(decimal.Decimal(n))
        n += 0.5
    return list_of_numbers