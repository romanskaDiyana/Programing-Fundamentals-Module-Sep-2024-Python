# Since it is Easter, you have decided to make some loaves of Easter bread and exchange them for eggs.
# Create a program that calculates how many loaves you can make (according to the recipe) with the budget you have.
# recipe:
# eggs = 1 pack
# flour = 1 kg
# milk = 0.250 L
# First, you will receive your budget. Then, you will receive the price for 1 kg flour. The price for
# 1 pack of eggs is 75% of the price for 1 kg flour. The price for 1L milk is 25% more than the price
# for 1 kg flour. Keep in mind that you use only 250ml milk for a bread.
# Start cooking the loaves and keep making them until you have enough budget. Keep in mind that:
#     • For every loaf of bread that you make, you will receive 3 colored eggs.
#     • For every 3rd bread you make, you will lose some of your colored eggs after receiving the usual 3
#     colored eggs for your bread. The count of eggs you will lose is calculated when you subtract 2 from
#     your current count of loaves - ({current_bread_count} - 2)
# In the end, print the loaves of bread you made, the eggs you have collected, and the money you have left,
# formatted to the 2nd decimal place, in the following format:
# "You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left}BGN left."

budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = flour_price + (flour_price * 0.25)
one_bread_price = flour_price + eggs_price + (milk_price / 4)

colored_eggs = 0
bread_count = 0
count_of_eggs_lost = 0

while budget >= one_bread_price:

    colored_eggs += 3
    bread_count += 1

    if bread_count % 3 == 0:
        count_of_eggs_lost = bread_count - 2
        colored_eggs -= count_of_eggs_lost

    budget -= one_bread_price

print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")