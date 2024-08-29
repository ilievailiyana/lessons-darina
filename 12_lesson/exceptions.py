# exceptions - za da ne spira programata s greshka, proverqvame za exceptions i gi handle-vame

while True:
    # try clause, trqbva da ima pone 1 except ili 1 finally clause
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
        # this code runs only when the specific except clauses above are not entered (treat as else from the if-elif-else logic)
        print("I'm handling all types of exceptions you didn't specify with except clause")
        print("Exception is:", e)
    else:
        # Code koito se run-va ako nqma exception
        print("No exception occurred, that's why I'm printing!")
    finally:
        # Code koito se run-va bez znachenie dali e imalo exception ili ne
        print("finally block always runs! No matter if there was an exception or not!")