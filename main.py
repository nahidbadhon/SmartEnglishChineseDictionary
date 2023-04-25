import re # to use regular expression
english_words = []# Read words from words.txt
chinese_words = []
with open('words.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # Split the line by tab, space, or other common delimiters
        parts = re.split(r'\t|\s+', line.strip())
        # line.strip() removes leading/trailing whitespaces
        if len(parts) >= 2:
            english_word = parts[0] # Extract the English word from the parts list
            chinese_word = parts[1] # Extract the Chinese word from the parts list
            english_words.append(english_word) # Append English word to the english_words list
            chinese_words.append(chinese_word) # Append Chinese word to the chinese_words list
        else:
            print(f"Skipping line: {line.strip()}") # Print a message if a line does not contain both English and Chinese words

# Create a dictionary mapping English words to Chinese words
dictionary = dict(zip(english_words, chinese_words))

# this method to search for words and return matching words list and match count
def search_words(input_letters):
    matching_words = [] # Initialize an empty list to store matching words
    match_count = 0 # Initialize match count to 0
    for english_word in english_words:
        if input_letters in english_word:
            # Check if the input letters are present in the English word
            matching_words.append(english_word) # Append the matching English word to the list
            match_count += 1 # Increment match count by 1
    return matching_words, match_count

# this method to display the Chinese counterpart of a selected English word
def display_chinese_counterpart(english_word):
    chinese_word = dictionary.get(english_word) # Get the Chinese word corresponding to the English word from the dictionary
    if chinese_word:
        print(f"The Chinese counterpart of '{english_word}' is '{chinese_word}'.")
    else:
        print(f"No Chinese counterpart found for '{english_word}'.")

# Main loop for dictionary tool
while True:
    print("\nSmart English-Chinese Dictionary Tool!")
    input_letters = input("Enter input letters (or 'quit' to exit): ")
    if input_letters == "quit":
        break # Exit the loop if the user enters 'quit'
    matching_words, match_count = search_words(input_letters)
    print(f"\nMatching Words ({match_count}):")
    for i, word in enumerate(matching_words):
        print(f"{i + 1}. {word}")
    if match_count > 0:
        selected_word = input("Select a word (or 'back' to input new letters): ")
        if selected_word == "back":
            continue # Continue to the next iteration of the loop if the user enters 'back'
        elif selected_word in matching_words:
            display_chinese_counterpart(selected_word) # Call the function to display the Chinese counterpart of the selected English word
        else:
            print("Invalid input. Please try again.")
    else:
        print("No matching words found.")

