My_dictionary = {
    "name": "Genius",
    "Math": "A",
    "Physics": "B",
    "Philosophy": "F"
    }
My_Keys = ["name", "Philosophy"]
required_dictionary = {k: My_dictionary[k] for k in My_dictionary.keys() if k in My_Keys}
print(required_dictionary)
