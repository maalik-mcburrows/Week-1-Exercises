leet_nums = "4361057 "

leet_letters = "AEGIOST"

translation = ""

selected_leet = input("Please enter a sequence of numbers that correspond with each respective letter to for a message.")

for element in range(0, len(selected_leet)):
    if leet_nums[0] == selected_leet[element]: 
        translation += ("A")
    if leet_nums[1] == selected_leet[element]: 
        translation += ("E")
    if leet_nums[2] == selected_leet[element]: 
        translation += ("G")
    if leet_nums[3] == selected_leet[element]: 
        translation += ("I")
    if leet_nums[4] == selected_leet[element]: 
        translation += ("O")
    if leet_nums[5] == selected_leet[element]: 
        translation += ("S")
    if leet_nums[6] == selected_leet[element]: 
        translation += ("T")
    if leet_nums[7] == selected_leet[element]: 
        translation += (" ")
print(translation)    
    
    