# importvame module za da polzvame funkciq koqto toi ima
import random

my_variable = 10

def sum(a, b):
    return a + b

# tozi block shte se run-ne, ako module-a e run-nat direktno ot run butona, a ne kogato e import-nat
if __name__ == "__main__":
    # za da polzvame funkciq ot module, pishem imeto na module-a . imeto na funkciqta
    print("Print:", random.randint(1, 10))
    sum(10, 20)