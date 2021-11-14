def loose_change(cents):
    keys = ['Quarters','Dimes','Nickels', 'Pennies']
    values = [25, 10, 5, 1]
    change = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    number = 0
    for valor in values:
        if cents >= valor:
            coinsNumber = cents//valor
            cents = cents%valor
            change[keys[number]] = coinsNumber
        number += 1
    return change

loose_change(91)