#~  Tax Calculator ~#
#~ c. Indya Dodson ~#

print("I hope you had a grat dinner!")
print("Now it's time to calculate the tip.")
#print("Tell me, how much was the bill? $", end="") #stays on the same line
bill = float(input("Tell me, how much was the bill? $"))

if bill > 50:
    print("-------------------")
    print("¯\_(⊙︿⊙)_/¯")
    print("Wow that's an expensive dinner! ")
    print("At leaset for me, that is :,(")
else:
    print("-------------------") #for formatting purposes

# Tip calcualtion
tip_10p = round(bill + (0.10 * bill),2)
tip_15p = round(bill + (0.15 * bill),2)
tip_20p = round(bill + (0.20 * bill),2)

print(f"If you pay 10%, the total will be ${tip_10p}")
print(f"If you pay 15%, the total will be ${tip_15p}")
tip_20p_text = "If you pay 20%, the total will be ${}"
print(tip_20p_text.format(tip_20p)) #Use format for print (same output as printf)
