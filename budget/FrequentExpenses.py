from . import Expense

expenses = Expense.Expenses()

expenses.read_expenses('data/spending_date.csv')