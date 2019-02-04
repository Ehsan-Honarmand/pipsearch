import os
print('hi,enter the name of module for pip search & save data with format txt in your directory')
print('search over --> type end ')

l,L=[],[]
while l != 'end':
    l = input('search for module ? ')
    l = str(l)
    L.append(l)

for i in range(len(L)-1):
    os.system(f'py -m pip search {L[i]} > {L[i]}.txt')
