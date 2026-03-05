a = 10
b = 3

print(a-b)
print(a+b)
print(a*b)
print(a/b)  # Immediately transforms into a float? Data types are not a concern...
print(a//b)
print(a**b)
print(a%b)

professors = ["greg", "kianoosh", "richard", "patricia", "debra"]

print(professors[0])
print(professors[-1])
professors.append("leo")
print(professors)
professors.extend(["heather", "kevin", "jason"])
print(professors)
professors.insert(2, "trevor")
print(professors)
professors[3] = "mark"
print(professors)
print(professors[3:5]) # Goes from 3 to 4, no access to 5.
print(professors[3:]) # Goes from 3 to end of list
print(professors[:6]) # Goes from beginning of list to 5, NOT 6.
print(professors[:]) # It is a copy of the list, not the ACTUAL professors

professors.remove("kianoosh")
print(professors)
print(professors.index("mark"))
x = professors.pop(6) # Removes "leo" and CAPTURES that value into x.
print(x)
print(len(professors))
print(type(professors))
professors.sort()
print(professors)
professors.sort(reverse=True)
print(professors)

for i in professors:
    print(i) # The advanced for-loop from java, where i takes values from list.
    print(i.title()) # Capitalized Names
print("FIU") # NOT repeated, it is not in the same indentation...

water_data = { # This is a DICTIONARY. Very useful for data collection.
    "temperature":[78, 89, 92], # Dictionaries store lists
    "ph":[6.5, 6.7, 6.3],
    "oxygen":[7.2, 5.6, 3.5]
}

print(water_data["oxygen"]) # How to access a list from a dictionary.
print(water_data["oxygen"][2]) # How to access a value from a list in dictionary.
print(water_data["oxygen"][1:])

print(water_data.keys())
print(water_data.values())

import pandas as pd # Can make automatic data tables with dictionaries
                    # VERY useful for data visualization

df = pd.DataFrame(water_data)
print(df)

df