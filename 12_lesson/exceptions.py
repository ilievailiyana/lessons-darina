# exceptions - za da ne spira programata s greshka, proverqvame za exceptions i gi handle-vame

while True:
    # try clause, trqbva da ima pone 1 except ili finally clause
    try:
        # Code koito moje da dade greshka ili exception
        x = input("Enter a number or 'exit' to stop: ")
        if x == 'exit':
            break
        x = int(x)
        result = 10 / x
        print("Result:", result)
    except ValueError:
        # Handle ValueError exceptions
        print("Handling ValueError exception. To the user: you have to enter a number.")
    except (ZeroDivisionError, TypeError):
        print("Handling two exceptions. I will print the same message for ZeroDivision and for TypeError exceptions")
    except Exception as e:
        print("Exception is not ValueError, so I'm printing - I'm handling all types of exceptions you didn't specify with except clause")
        print("Exception is:", e)