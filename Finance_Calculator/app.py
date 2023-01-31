from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html')
  elif request.method == 'POST':
    user_name = request.form.get('one')
    checking_account_balance = float(request.form.get('two'))
    saving_account_balance = float(request.form.get('three'))
    invest_account_value = float(request.form.get('four'))
    total_utility_bills = float(request.form.get('five'))
    total_credit_card_debt = float(request.form.get('six'))
    credit_card_balance_due = float(request.form.get('seven'))
    credit_card_minimum_payment_due = float(request.form.get('eight'))
    annual_credit_card_interest_rate = float(request.form.get('nine')) * 0.01
    loan_debt = float(request.form.get('ten'))
    loan_payment_due = float(request.form.get('eleven'))
    annual_loan_interest_rate = float(request.form.get('twelve')) * 0.01
    other_asset_value = float(request.form.get('thirteen'))

    total_value_of_assets = checking_account_balance + saving_account_balance + invest_account_value + other_asset_value

    total_debt = total_utility_bills + total_credit_card_debt + loan_debt

    total_net_worth = total_value_of_assets - total_debt

    total_value_of_bills_due = total_utility_bills + credit_card_balance_due + loan_payment_due

    checking_balance_after_payment = checking_account_balance - total_value_of_bills_due

    total_balance_in_bank = checking_balance_after_payment + saving_account_balance

    credit_card_debt_after_paying_balance_due = total_credit_card_debt - credit_card_balance_due

    loan_debt_after_paying_amount = loan_debt - loan_payment_due + (
      (loan_debt - loan_payment_due) * annual_loan_interest_rate / 12)

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

    networth_after_payments_specified = total_value_of_assets - total_utility_bills - loan_payment_due - credit_card_minimum_payment_due - loan_debt_after_paying_amount - total_credit_debt_after_min_payment

#    statement = f'''Hello {user_name},

#        \nThe total dollar value of assets you own is ${total_value_of_assets} and the total dollar value
#        of your debt is currently ${total_debt}; therefore, your current net worth is: ${total_net_worth}.\n

#        \nYour total bills due are ${total_value_of_assets}. Once you make these payments, you will have ${checking_balance_after_payment} left in your checking account, and ${total_remaining_money} in your bank accounts overall. Additionally, your total credit card debt will be down to ${credit_card_debt_after_paying_balance_due} and your loan debt will be down to ${loan_debt_after_paying_amount} (including interest applied on the remaining balance after your payment). Therefore, your total debt will then be paid down to ${total_debt_after_payments} and your net worth will be ${networth_after_payments}.\n

#        \nIf you instead choose not to pay off your full credit card balance due (${credit_card_balance_due}) and only pay the minimum payment due , (${credit_card_minimum_payment_due}) you will have ${value_remaining_checking_after} left in your checking account, and ${total_remaining_money} in your bank accounts overall. However, you will accrue ${interest_accrued_on_credit_card} in interest. Your total credit card debt will then be ${total_credit_debt_after_min_payment}. In this case, your total debt would instead be ${total_debt_after_payments} and your net worth will be ${networth_after_payments_specified}.\n'''

    #result = eval(statement)
    #return render_template('statement.html', statement=statement, statement1=statement)
    return render_template(
      'statement.html',
      user_name=user_name,
      total_value_of_assets=total_value_of_assets,
      total_debt=total_debt,
      total_net_worth=total_net_worth,
      total_value_of_bills_due=total_value_of_bills_due,
      checking_balance_after_payment=checking_balance_after_payment,
      total_balance_in_bank=total_balance_in_bank,
      credit_card_debt_after_paying_balance_due=
      credit_card_debt_after_paying_balance_due,
      loan_debt_after_paying_amount=loan_debt_after_paying_amount,
      total_loan_debt_after_payments=total_loan_debt_after_payments,
      networth_after_payments=networth_after_payments,
      minimum_bills_due=minimum_bills_due,
      value_remaining_checking_after=value_remaining_checking_after,
      total_remaining_money=total_remaining_money,
      interest_accrued_on_credit_card=interest_accrued_on_credit_card,
      total_credit_debt_after_min_payment=total_credit_debt_after_min_payment,
      total_debt_after_payments=total_debt_after_payments,
      networth_after_payments_specified=networth_after_payments_specified,
      credit_card_minimum_payment_due=credit_card_minimum_payment_due,
      credit_card_balance_due=credit_card_balance_due)


if __name__ == '__main__':
  app.run()


@app.errorhandler(500)
def page_not_found(e):
  return render_template(
    'templates/statement.html',
    result=
    "Please Check your input values. Ensure that all values entered are numbers"
  )
