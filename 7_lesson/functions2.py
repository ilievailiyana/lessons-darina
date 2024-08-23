def add_numbers(a, b):
    result = a + b
    # return e optional
    # samo edin return na funkciq, sled nego nishto ne se izpulnqva, kakto break na loops
    return result

def sum_product(a, b, c):
    result = a + b + c
    result2 = a * b * c
    print("Sum:", result)
    print("Product:", result2)
    
func_result = sum_product(5, 10, 20)
print("Printirane na towa koeto return-va funkciqta:", func_result)

