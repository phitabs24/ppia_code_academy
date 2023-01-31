print("""Welcome to The Basic Financial State Calculator


Please provide the following information as accurately as possible""")

user_name = input("Please Enter Your Full Names: ")

checking_account_balance = float(input("Checking account Balance: $"))
saving_account_balance = float(input("Saving's account Balance: $"))
invest_account_value = float(input("Investment account Value: $"))
total_utility_bills = float(input("Total utility Bills: $"))
total_credit_card_debt = float(input("Total credit card debt: $"))
credit_card_balance_due = float(input("Credit card balance due: $"))
credit_card_minimum_payment_due = float(
  input("Credit card minimum payment due: $"))
annual_credit_card_interest_rate = float(
  input("Annual credit card interest rate: %")) * 0.01
loan_debt = float(input("Loan debt: $"))
loan_payment_due = float(input("Loan payment due: $"))
annual_loan_interest_rate = float(input("Annual loan interest rate: %")) * 0.01
other_asset_value = float(input("Other asset value: $"))

total_value_of_assets = checking_account_balance + saving_account_balance + invest_account_value + other_asset_value

total_debt = total_utility_bills + total_credit_card_debt + loan_debt

total_net_worth = total_value_of_assets - total_debt

total_value_of_bills_due = total_utility_bills + credit_card_balance_due + loan_payment_due

checking_balance_after_payment = checking_account_balance - total_value_of_bills_due

total_balance_in_bank = checking_balance_after_payment + saving_account_balance

credit_card_debt_after_paying_balance_due = total_credit_card_debt - credit_card_balance_due

loan_debt_after_paying_amount = loan_debt - loan_payment_due + ((loan_debt - loan_payment_due) * annual_loan_interest_rate / 12)

total_loan_debt_after_payments = loan_debt_after_paying_amount + credit_card_debt_after_paying_balance_due

networth_after_payments = total_value_of_assets - total_value_of_bills_due - credit_card_debt_after_paying_balance_due + loan_debt_after_paying_amount

minimum_bills_due = total_utility_bills + credit_card_minimum_payment_due + loan_payment_due

value_remaining_checking_after = checking_account_balance - minimum_bills_due

total_remaining_money = checking_account_balance + saving_account_balance - minimum_bills_due

interest_accrued_on_credit_card = (credit_card_balance_due -
                                   credit_card_minimum_payment_due) * (
                                     annual_credit_card_interest_rate / 12)

total_credit_debt_after_min_payment = total_credit_card_debt - credit_card_minimum_payment_due + interest_accrued_on_credit_card

total_debt_after_payments = total_credit_debt_after_min_payment + loan_debt_after_paying_amount

networth_after_payments_specified = total_value_of_assets - total_utility_bills - loan_payment_due -         credit_card_minimum_payment_due - loan_debt_after_paying_amount - total_credit_debt_after_min_payment

print(f'''Hello {user_name},

The total dollar value of assets you own is ${total_value_of_assets} and the total dollar value of your debt is currently ${total_debt}; therefore, your current net worth is: ${total_net_worth}.

Your total bills due are ${total_value_of_assets}. Once you make these payments, you will have ${checking_balance_after_payment} left in your checking account, and ${total_remaining_money} in your bank accounts overall. Additionally, your total credit card debt will be down to ${credit_card_debt_after_paying_balance_due} and your loan debt will be down to ${loan_debt_after_paying_amount} (including interest applied on the remaining balance after your payment). Therefore, your total debt will then be paid down to ${total_debt_after_payments} and your net worth will be ${networth_after_payments}.

If you instead choose not to pay off your full credit card balance due (${credit_card_balance_due}) and only pay the minimum payment due , (${credit_card_minimum_payment_due}) you will have ${value_remaining_checking_after} left in your checking account, and ${total_remaining_money} in your bank accounts overall. However, you will accrue ${interest_accrued_on_credit_card} in interest. Your total credit card debt will then be ${total_credit_debt_after_min_payment}. In this case, your total debt would instead be ${total_debt_after_payments} and your net worth will be ${networth_after_payments_specified}.'''
      )
