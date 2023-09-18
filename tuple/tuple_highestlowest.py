
l=(18785,24795,370,4678,566,6,776,8687,968,69674)
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