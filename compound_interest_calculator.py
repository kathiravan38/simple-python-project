def  compound_interest_calculator():
    #input
    principle=float(input("enter the principle amount: "))
    if principle == 0:
        print(f"final amount:${round(principle,2)}")
        return
    elif principle < 0:
        print("principle amount should not be a negative amount")
        return
    
    rate=float(input("enter the annual interest rate(%): "))
    time=float(input("enter the time (in years): "))
    
    #compound interest list
    print("\nselect compound frequency:\n1.annually(1 time/year)\n2.half yearly(2 time/year)\n3.quarterly(4 time/year)\n4.monthly(12 time/year)\n5.daily(365 time/year)")
    choice=input("enter the choice(1-5): ")
    if choice == '1':
        n=1
        s="annually(1 times/year)"
    elif choice == '2':
        n=2
        s="half yearly(2 times/year)"
    elif choice == '3':
        n=4
        s="quarterly(4 times/year)"
    elif choice == '4':
        n=12
        s="monthly(12 times/year)"    
    elif choice == '5':
        n=365
        s="daily(365 times/year)"
    else:
        print("invalid choice")
        return
    
    #calculate compound interest
    rate=rate/100
    total=principle * (1 +rate/n)**(n*time)
    compound_interest=total-principle
    #output
    print(f"the final amount:${round(total,2)}")
    print(f"the compound interest ({s}):${round(compound_interest,2)}")

compound_interest_calculator()
    
    
