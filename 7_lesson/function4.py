# Moje da imame i funkcii bez parametri
x = 10
y = 15

# funkciite imat dostup do vsichki promenlivi definirani vuv faila
# kakto dosega - promenlivi sa dostupni v sushtata kolona i nadqsno v kolonite
def sum_numbers():
    x = int(input("Enter a number: "))
    return x + y

# kogato vikame funkciqta, parametrite narichame argumenti
print(sum_numbers())