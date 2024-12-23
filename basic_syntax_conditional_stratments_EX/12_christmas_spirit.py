# It is time to get in a Christmas mood. You need to decorate the house in time for the big event, but you
# have limited days to do so.
# Write a program that calculates how much money you will need to spend on Christmas decorations and how much your
# Christmas spirit will improve.
# On the first line, you will receive the quantity of decorations you should buy each time you go shopping.
# On the second line, you will receive the days left until Christmas.
# There are 4 types of decorations, and each piece costs a certain price. Also, each time you go shopping for a
# concrete type of decoration, your Christmas spirit is improved by some points:
# Until Christmas, you go shopping for a certain decoration as follows:
#     • Every second day you buy Ornament Sets.
#     • Every third day you buy Tree Skirts and Tree Garlands.
#     • Every fifth day you buy Tree Lights.
#         ◦ If you have bought Tree Lights and Tree Garlands on the same day, you additionally
#         increase your spirit by 30.
# Hint: A day happens to be the third one as well as the fifth one at the same time (for example the 15th day).
# That's not all! You have a cat at home that really likes to mess around with the decorations:
#     • Every tenth day your cat ruins all tree decorations, and you lose 20 points of the spirit:
#         ◦ Because of that, you go shopping (for a second time during the day) to buy one piece of tree skirt,
#         garlands, and lights, but you do NOT earn additional spirit points for them.
#     • Also, because of the cat - at the beginning of every eleventh day, you are forced to increase the quantity
#     of decorations needed to be bought each time you go shopping by adding 2.
#     • If the last day is the tenth day, the cat demolishes even more and ruins the Christmas turkey, and you
#     lose an additional 30 points of spirit.
# In the end, you must print the total cost and the gained spirit.
# Input / Constraints
# The input will consist of exactly 2 lines:
#     • quantity - integer in the range [1…100]
#     • days - integer in the range [1…100]
# Output
# In the end, print the total cost and the total gained spirit in the following format:
#     • "Total cost: {budget}"
#     • "Total spirit: {totalSpirit}"

quantity = int(input())
days = int(input())

total_cost = 0
total_spirit = 0

ornament_sets_price = 2
tree_skirts_price = 5
tree_garlands_price = 3
tree_lights_price = 15

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_cost += quantity * ornament_sets_price
        total_spirit += 5
    if day % 3 == 0:
        total_cost += (quantity * tree_skirts_price) + (quantity * tree_garlands_price)
        total_spirit += 13
    if day % 5 == 0:
        total_cost += quantity * tree_lights_price
        total_spirit += 17
        if day % 5 == 0 and day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirts_price + tree_lights_price + tree_garlands_price

if days % 10 == 0:
    total_spirit = total_spirit - 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
