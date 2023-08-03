from ML_model import predict_loan_approval
from command_line import command_line

print("Welcome to the Western Governors Bank loan tool. \nPlease answer the following questions "
      "and we will determine whether or not you will get pre-approved for a loan with 97% accuracy.")
print("Please enter the amount you wish to finance with us.")

while True:
    result = command_line()

    # Unpack the user data tuple and pass individual arguments to predict_loan_approval function
    annual_income, loan_amount, loan_term, credit_score, residential_assets, commercial_assets, luxury_assets, bank_assets = result
    loan_status = predict_loan_approval(annual_income, loan_amount, loan_term, credit_score, residential_assets,
                                        commercial_assets, luxury_assets, bank_assets)

    print("Loan Status:", loan_status)

    desire = input("If you would like to perform another query press 1: "
                   "\nIf you would like to exit press 2: ")

    if desire == "2":
        print("We look forward to your buiness! \nExiting the program. Goodbye!")
        break
    elif desire != "1":
        print("Invalid input. Please enter either '1' to perform another query or '2' to exit.")
