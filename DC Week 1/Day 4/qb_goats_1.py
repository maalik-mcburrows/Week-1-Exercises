qb_goats = ["Joe", "Tom", "Aaron", "Mike", "Steve"]

who_to_remove = input("Who would you like to remove? ")

if who_to_remove in qb_goats: 
    qb_goats.remove(who_to_remove)
    print(qb_goats)
else:
    print("%s isn't a part of the group" % (who_to_remove))