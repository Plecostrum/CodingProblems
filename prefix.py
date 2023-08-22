def autoComplete(query,dictionary):

    result = []
    for word in dictionary:
        if word.startswith(query):
            result.append(word)
    return result
    

    
    
if __name__ == "__main__":
    query = "da"
    dictionary = ["Daily",
"Daddy",
"Daisy",
"Dazed",
"Dairy",
"Debut",
"Doubt",
"Daffy",
"Death",
"Delve",
"Dealt",
"Daunt",
"Delay"]
    print(autoComplete(query.capitalize(),dictionary))