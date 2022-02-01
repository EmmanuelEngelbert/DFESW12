# Practice with conditionals 

devs_money = input("How much money can you spend on smash tournaments atm?")
dev_can_play_smash = False 

if not devs_money > 10 and dev_can_play_smash:
    print("Dev enters a smash tournament!") 
elif devs_money < 10 and dev_can_play_smash: 
    print("Dev is too poor to enter") 
else: 
    print("Dev just can't play smash") 
print("end program")