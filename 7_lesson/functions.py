# Functions
# v skobi - parameters
# return - optional
def add_numbers(a, b):
    result = a + b
    # return - vrushta rezultata ot funkciqta, tam kydeto e izvikana
    return result

# Ako nqma return i se opitame da printirame ili da vidim rezultata ot funkciqta, shte izleze None
# Parameters can have default values
def subtract_numbers(x, y = 6):
    z = x - y
    print(z)


print("Hello")
# kakto printirame promenlivi, po sushtiq nachin printirame rezultata ot funkcii
func_result = add_numbers(4, 5)
print(func_result)
print(add_numbers(40, 50))

# Vikame funkciqta samo s 1 parameter za x, tui kato imame defolten za y
print(subtract_numbers(10)) # ottuk idva None printiran v console-ata

# Vikame funkciqta s 2 parametera i taka override-vame defolta za y
subtract_numbers(13, 1)