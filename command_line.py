def digit_checker(digit):
    # checking if digit entered is a valid digit.
    if digit.isdigit():

        # converting digit to an int
        digit = int(digit)
        # returns the digit and a boolean of true
        return digit, True
    else:
        # informs the user what they entered was incorrect.
        print("Invalid input. Please enter your answer in the form of an integer.")
        # then returning the digit and a false boolean.
        return digit, False


def command_line():
    # loop ensures if an invalid input is entered the user is returned to the question they answered
    # in the wrong format. to prevent the user from having to cycle back through the whole prompt.
    # just because of one mistake. increasing ease of use and user experience.
    while True:
        # receive the amount to be financed from the user.
        loan_amount = input("Enter loan amount: ")

        # checking the amount entered is an int. Valid input will be a boolean of true or false.
        loan_amount, valid_input = digit_checker(loan_amount)

        # if valid_input is true we break out of the loop and move on to the next input.
        if valid_input:
            break

    print("Wow how exciting! Financing an amount of ", loan_amount)

    while True:
        # getting the users annual income.
        annual_income = input("What is your annual income?: ")

        # checking the amount entered is an int. Valid input will be a boolean of true or false.
        annual_income, valid_input = digit_checker(annual_income)

        # if valid_input is true we break out of the loop and move on to the next input.
        if valid_input:
            break

    while True:
        # getting the desired loan term
        loan_term = input("what is the desired term of the loan in months: ")

        # checking the amount entered is an int. Valid input will be a boolean of true or false.
        loan_term, valid_input = digit_checker(loan_term)

        # if valid_input is true we break out of the loop and move on to the next input.
        if valid_input:
            break

    while True:
        # getting the users FICO credit score
        credit_score = input("What is your most recent FICO credit score rating: ")

        # checking the amount entered is an int. Valid input will be a boolean of true or false.
        credit_score, valid_input = digit_checker(credit_score)

        # if valid_input is true we break out of the loop and move on to the next input.
        if valid_input:
            break

    while True:
        # getting residential assets
        residential_assets = input("what is the value of your residential assets?: ")

        # checking the amount entered is an int. Valid input will be a boolean of true or false.
        residential_assets, valid_input = digit_checker(residential_assets)

        # if valid_input is true we break out of the loop and move on to the next input.
        if valid_input:
            break

    while True:
        # getting commercial assets
        commercial_assets = input("What is the value of your commercial assets?: ")

        # checking the amount entered is an int. Valid input will be a boolean of true or false.
        commercial_assets, valid_input = digit_checker(commercial_assets)

        # if valid_input is true we break out of the loop and move on to the next input.
        if valid_input:
            break

    while True:
        # getting luxury assets
        luxury_assets = input("What is the value of your luxury assets?: ")

        # checking the amount entered is an int. Valid input will be a boolean of true or false.
        luxury_assets, valid_input = digit_checker(luxury_assets)

        # if valid_input is true we break out of the loop and move on to the next input.
        if valid_input:
            break

    while True:
        # getting bank assets
        bank_assets = input("What is the value of your bank assets?: ")

        # checking the amount entered is an int. Valid input will be a boolean of true or false.
        bank_assets, valid_input = digit_checker(bank_assets)

        # if valid_input is true we break out of the loop and move on to the next input.
        if valid_input:
            break

    user_data = (annual_income, loan_amount, loan_term, credit_score, residential_assets,
                 commercial_assets, luxury_assets, bank_assets)

    return user_data
