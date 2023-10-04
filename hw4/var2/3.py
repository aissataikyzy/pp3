d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'}, 
   {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'}, 
   {'name':'Princess', 'phone':'555-3141', 'email':''}, 
   {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]
print('A)')
for a in d:
    if a['phone'][-1] == '8':
        print(a['name'])
print('B)')
for a in d:
    if a['email'] == '':
        print(a['name'])  