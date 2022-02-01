# Practice with conditionals 

devs_money = int(input("How much money can you spend on smash tournaments atm? "))
dev_can_play_smash = input("Can you play smash? Please answer with yes or no ") 
lroptions = ("YES", "NO")

if dev_can_play_smash.upper == "YES": 
    dev_can_play_smash = True
elif dev_can_play_smash.upper == "NO":
     dev_can_play_smash = False 
else:
    print("Please give either a yes or no answer!") 


if not devs_money > 10 and dev_can_play_smash:
    print("Dev enters a smash tournament!") 
elif devs_money < 10 and dev_can_play_smash: 
    print("Dev is too poor to enter") 
else: 
    print("Dev just can't play smash") 
print("end program")