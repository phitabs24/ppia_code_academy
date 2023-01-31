# PPiAI Code Academy Assignment 2 Term 1 #

## Basic Financial State Calculator ##

<style>
 .container {
  with: 80%;
 }
</style>
Your client wants a program to generate a basic financial report that users can run regularly to understand their current financial state. This program should be able to store in variables:

- the users name
- checking account balance
- savings account balance
- investment account value
- Total utility bills
- total credit card debt
- credit card balance due
- credit card minimum payment due
- annual credit card interest rate
- loan debt
- loan payment due
- annual loan interest rate
- other asset value

When run, this program should generate the following report:

---
<div class="container">

`start of code`

```html
Hello <user’s name>,

The total dollar value of assets you own is $<total value of assets> and the total dollar value of your debt is currently $<total debt>; therefore, your current net worth is: $<total net worth>

Your total bills due are $<total value of bills due>. Once you make these payments, you will have $<value remaining in the checking account after making payments> left in your checking account, and $<total remaining money in bank> in your bank overall. Additionally, your total credit card debt will be down to $<credit card debt remaining after paying balance due> and your loan debt will be $<loan debt after paying amount due and interest is applied on the remaining balance for the month>, including interest applied on the remaining balance after your payment. Therefore, your total debt will then be paid down to $<total debt after making payments> and your net worth will be $<net worth after making payments as specified>.
```

EXTRA CREDIT If you’d like extra credit on your assignment, you can include the following in our output. Successfully including this will give you an extra one quarter worth of assignment credit:

```html
If you instead choose not to pay off your full credit card balance due, $<credit card balance due>, and only pay the minimum payment due, $<credit card minimum payment due>, you will have $<value remaining in the checking account after making minimum payments> left in your checking account, and $<total remaining money in bank> in your bank overall. However, you will accrue $<interest accrued on credit card balance for the month>. Your total credit card debt will then be $<total credit card debt after paying minimum payment and accruing interest on remaining balance due>. In this case, your total debt would instead be $<total debt after making payments as specified> and your net worth will be $<net worth after making payments as specified>.
```

`End of Code`

</div>

---

## Formulae for calculating highlighted values in the code above are ##

- Total value of assets = checking account balance + savings account balance +investment account value + other assets value

- Total Debt = total utility bills + total credit card debt + loan debt

- Total net worth = total value of assets - total debt

- Total Value of Bills Due = total utility bills + credit card balance due + loan payment due

- Value remaining in the checking account after making payments = checking account balance - total value of bills due

- Total remaining money in bank = Value remaining in the checking account after making payments + savings account balance

- Credit Card Debt After paying balance due = total credit card debt - credit card balance due

- Loan debt after paying amount due and interest is applied on the remaining balance for the month = loan debt - loan payment due + ((loan debt - loan payment due) X annual loan interest rate ➗12)

- Total debt after making payments = Loan debt after paying amount due and interest is applied on the remaining balance for the month + Credit Card Debt After paying balance due

- Net worth after making payments specified = total value of assets - total value of bills due - Credit Card Debt After paying balance due - Loan debt after paying amount due and interest is applied on the remaining balance for the month

- Minimum Bills Due = total utility bills + credit card minimum payment due + loan payment due

- Value remaining in checking account after making minimum payments = checking account balance - minimum bills due

- Total remaining money in bank (Paragraph 2) = checking account balance + savings account balance - minimum bills due

- Interest accrued on credit card balance for the month = (credit card balance due - credit card minimum payment due) X (annual credit card interest rate ➗ 12)

- Total credit card debt after paying minimum payment and accruing interest on remaining balance due = total credit card debt - credit card minimum payment due + Interest accrued on credit card balance for the month

- Total debt after making payments as specified (paragraph 2) = Total credit card debt after paying minimum payment and accruing interest on remaining balance due + Loan debt after paying amount due and interest is applied on the remaining balance for the month

- Net worth after making payments as specified (paragraph 2) = total value of assets - total utility bills - loan payment due - credit card minimum payment due - Loan debt after paying amount due and interest is applied on the remaining balance for the month - Total credit card debt after paying minimum payment and accruing interest on remaining balance due
