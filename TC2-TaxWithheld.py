# Tax Withheld Calculator

# Write a console program that calculates the total amount of tax withheld from an employee’s weekly salary.
# The total withheld tax amount is calculated by combining the amount of provincial tax withheld and the amount of 
# federal tax withheld, minus a per-dependent deduction from the total tax withheld. The user will enter their pre-tax 
# weekly salary amount and the number of dependents they wish to claim. 
# 
# The program will calculate and output the amount of provincial tax withheld, amount of federal tax withheld, the 
# dependent tax deduction, and the user’s final take-home amount.
# Provincial withholding tax is calculated at 6.0%. Federal withholding tax is calculated at 25.0%. 
# The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Provincial withholding tax is calculated at 6.0%. 
    provInp = float(input("Please enter the full amount of your weekly salary: "))
    prov = provInp * 0.06

    #Federal withholding tax is calculated at 25.0%. 
    fed = float(provInp * 0.25)

    #The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.
    depInp = float(input("How many dependents do you have?: "))
    dep = (provInp * 0.02) * depInp

    #Total withheld
    withheld = (prov + fed) - dep

    #Total take-home pay
    pay = provInp - withheld

    #Results
    print("Provincial Tax Withheld: {0:.2f}".format(prov))
    print("Federal Tax Withheld: {0:.2f}".format(fed))
    print("Dependent Deduction for",int(depInp),"dependents: {0:.2f}".format(dep))
    print("Total Withheld: {0:.2f}".format(withheld))
    print("Total Take-Home Pay: {0:.2f}".format(pay))

    # YOUR CODE ENDS HERE

main()
