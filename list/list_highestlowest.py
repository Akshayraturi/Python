

l=[185,245,30,4,5,6,7,8,9,694]
highest=0
lowest=l[0]
for item in l:
    if item>highest:
        highest+=item
        highest=item
    elif item<lowest:
        lowest+=item
        lowest=item
print("lowest",lowest)
print("highest",highest)