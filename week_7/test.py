newphrase = "rainstorm"
           # 012345678
           # 123456789 --> college board version
#create a new variable called shortphrase
# and assign it a value by slicing
# the newphrase variable by removing
# the first 3 characters
# and the last 3 characters
# the first three characters are "rai"
# the last three characters are "orm"
#substring(string, start, end)

shortphrase  = newphrase[3:len(newphrase)-3]

#college board version --> [4:len(newphrase(-6))]
print(shortphrase)
#explain len(newphase)-3 = 9-3 = 6
#why does it end with 6?
#because the last index is not included
