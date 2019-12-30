my=open('Mad.txt','w')
my.write('''The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.''')#can be input by user
print('''String before:The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.''')
my.close()
my=open('Mad.txt','r+')
my.seek(0,0)
msg=my.read()
msg=msg.split()
ind=-1
for x in msg:
    ind+=1
    if x=='ADJECTIVE' or x=='ADJECTIVE.':
        msg[ind]=input('Enter an adjective:')
    elif x=='NOUN' or x=='NOUN.':
        msg[ind]=input('Enter a noun:')
    elif x=='VERB' or x=='VERB.':
        msg[ind]=input('Enter a verb:')

msg=' '.join(msg)
my.seek(0,0)
my.write(msg)
my.close()
