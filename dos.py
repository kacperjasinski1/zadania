try:
    income = float(input("dochod brutto: "))
    if income<=30000:
      tax = 0
    elif income <=120000:
        tax = income * 0.12 - 3600
    else:
        tax = 10800 + (income - 120000) * 0.32
        if income > 1000000:
            tax += (income - 1000000) * 0.04
    print("obliczony podatek: ", round(tax, 2), "zl")
except:
    print("bledne dane")