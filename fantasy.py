def addToInventory(inventory, addedItems):
    for k in addedItems:
        inventory.setdefault(k,0)
        inventory[k]+=1
    return inventory
def displayInventory(inventory):
   print('Inventory:')
   total=0
   for k,v in inventory.items():
       print(v,k,sep=' ')
       total+=v
   print('Total no. of items:',total)    

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
