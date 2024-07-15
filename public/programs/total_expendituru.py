from nada_dsl import *

def total_expenditure(xs: list[SecretInteger]) -> SecretInteger:
    total = Integer(0)
    for x in xs:
        total += x
    return total

def nada_main():
    # Create the parties for the participants
    participants = [Party("participant" + str(p)) for p in range(10)]
    official = Party(name="official")
    
    # Gather the inputs (daily expense from each participant)
    daily_expenses = [
        SecretInteger(
            Input(
                name="daily_expense" + str(p),
                party=Party("participant" + str(p))
            )
        )
        for p in range(10)
    ]
    
    # Gather the input for the number of days
    num_days = SecretInteger(Input(name="num_days", party=official))
    
    # Calculate the total expenditure for each participant
    total_expenses = [expense * num_days for expense in daily_expenses]
    total_expenditure_all = total_expenditure(total_expenses)
    
    return [Output(total_expenditure_all, "total_expenditure_all", official)]

# Assuming the appropriate environment setup for nada_dsl is in place, this function can now be used.
