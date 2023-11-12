marvel_characters = [["Thor", "Loki", "Odin"], ["Hawkeye", "Black Widow"], 
                     ["Captain America", 'Bucky']]
for sublist in marvel_characters:
    try:
        index = sublist.index("Captain America")
        sublist[index] = 'Falcon'
    except ValueError:
        pass

print(marvel_characters)