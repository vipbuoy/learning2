#Switch in python
#program that helps you to order customize sandwich
bmenu=['wheat','white','sourdough']
pmenu=['chicken','turkey','ham','tofu']
cmenu=['cheddar','swiss','mozzarella']
import pyinputplus as p
bread=p.inputMenu(bmenu,numbered=True)
protein=p.inputMenu(pmenu,numbered=True)
cheese=p.inputYesNo('Do you want cheese?')
if cheese=='Yes' or cheese=='yes':
    cheese=p.inputMenu(cmenu,numbered=True)
nu=p.inputNum("How many you want?")
print(f'You order of {bread} bread with {protein} protein with {cheese} cheese and quantity {nu} will ready soon!')
