from Calculator import Calculator

print("\n**Binary Calculator**")
calculator_open = Calculator()
while calculator_open.open == True:

    print(f"\n{'-' * 50}\n"
          "(B)inary to Decimal Conversion\n"
          "(D)ecimal to Binary Conversion\n"
          "(A)dd two binary numbers\n"
          "(S)ubtract two binary numbers\n"
          "(M)ultiply two binary numbers\n"
          "D(i)vide two binary numbers\n"
          "(Q)uit")
    user_input = input('')

    if user_input.upper() == 'B':
        calculator_open.binary()

    if user_input.upper() == 'D':
        calculator_open.decimal()

    if user_input.upper() == 'A':
        binary1 = input("Enter the first binary number: ")
        binary2 = input("Enter the second binary number: ")
        calculator = Calculator(binary1, binary2)
        print(f"\n{binary1} + {binary2} = {calculator.add()}\n")

    if user_input.upper() == 'S':
        binary1 = input("Enter the first binary number: ")
        binary2 = input("Enter the second binary number: ")
        calculator = Calculator(binary1, binary2)
        print(f"\n{binary1} - {binary2} = {calculator.subtract()}\n")

    if user_input.upper() == 'M':
        binary1 = input("Enter the first binary number: ")
        binary2 = input("Enter the second binary number: ")
        calculator = Calculator(binary1, binary2)
        print(f"\n{binary1} * {binary2} = {calculator.multiply()}\n")

    if user_input.lower() == 'i':
        binary1 = input("Enter the first binary number: ")
        binary2 = input("Enter the second binary number: ")
        calculator = Calculator(binary1, binary2)
        print(f"\n{binary1} / {binary2} = {calculator.divide()}\n")

    if user_input.upper() == 'Q':
        calculator_open.quit()

    if user_input.upper() != 'Q':
        print("\n**Not a valid input.**\n")
        cont = input("Press <enter> to continue, or 'Q' to quit. ")
        if cont == '':
            continue
        if cont.upper() == 'Q':
            calculator_open.quit()
