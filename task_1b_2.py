def remove_common_letters(name1, name2):
    for char in name1[:]:
        if char in name2:
            name1 = name1.replace(char, '', 1)
            name2 = name2.replace(char, '', 1)
    return name1, name2

def flames_game(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()
    
    # Remove common letters
    name1, name2 = remove_common_letters(name1, name2)
    
    # Count remaining letters
    count = len(name1) + len(name2)
    
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]
    
    result = {
        'F': 'Friends',
        'L': 'Lovers',
        'A': 'Affectionate',
        'M': 'Married',
        'E': 'Enemies',
        'S': 'Siblings'
    }
    
    return result[flames[0]]

# Get names from user
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Calculate and print the FLAMES result
result = flames_game(name1, name2)
print(f"The relationship between {name1} and {name2} is: {result}")
