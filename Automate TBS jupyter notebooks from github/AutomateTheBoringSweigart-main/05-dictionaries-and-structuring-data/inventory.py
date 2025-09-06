# The data structure to model the player’s inventory will be a 
## dictionary where the keys are string values describing the item in 
## the inventory and the value is an integer value detailing how many of that item the player has. 
# For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
## means the player has 1 rope, 6 torches, 42 gold coins, and so on.
# Write a function named displayInventory() that would take any possible “inventory” 

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v # This line will add each value to the item total 
        print(k,v) # This line will display the key and value of each key in the inventory dictionary
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

# Write a function named addToInventory(inventory, addedItems), 
## where the inventory parameter is a dictionary representing the player’s inventory 
## (like in the previous project) and the addedItems parameter is a list like dragonLoot. 
# The addToInventory() function should return a dictionary that represents the updated inventory. 
# Note that the addedItems list can contain multiples of the same item. 

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i not in inventory.keys(): # This will check if an added item is new 
            inventory.setdefault(i, 1) # This will add the new item to the inventory dictionary
        else: 
            inventory[i] += 1 # If the item is not new, this will increase the associated value by 1
    return inventory # The inventory dictionary needs to be returned 
        
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
