entry = input()

unencryptedEntry = []

for ele in range(len(entry)):
    if ele == "’" or ele == "‘":
        unencryptedEntry.append("'")
    elif ele == "“" or ele == "”":
        unencryptedEntry.append("\"")
    else:
        unencryptedEntry.append(entry[ele])
print(unencryptedEntry)