owner_name = input("What is your name? ")

savings_balance = float(input("How much money is in your bank to start? $"))

target_goal = input("What dream toy or game are you saving for? ")

target_cost = float(input("How much does it cost? $"))

print("\n--- Welcome to " + owner_name + "'s Piggy Bank Tracker! ---")

chores_done = int(input("\nHow many chores did you finish this week? "))
reward_per_chore = 2.50  

chore_earnings = chores_done * reward_per_chore
savings_balance = savings_balance + chore_earnings
print("Awesome! You earned $" + str(chore_earnings) + " from chores.")

snack_price = float(input("\nYou bought a snack! How much did it cost? $"))
savings_balance = savings_balance - snack_price

has_enough_money = savings_balance >= target_cost

is_bank_empty = savings_balance <= 0.0

print("\n================================")
print("Piggy Bank Owner: " + owner_name)
print("Chores Finished: " + str(chores_done))
print("Current Balance: $" + str(round(savings_balance, 2)))
print("Can you buy the " + target_goal + " today? " + str(has_enough_money))
print("Is your piggy bank completely empty? " + str(is_bank_empty))
print("================================")

if has_enough_money:
    print("Woohoo! Time to go shopping for your " + target_goal + "!")
else:
    money_needed = target_cost - savings_balance
    print("Keep saving! You only need $" + str(round(money_needed, 2)) + " more.")
