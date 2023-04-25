# SmartEnglishChineseDictionary
Software design ideas and key algorithms analysis:

This python project is a smart English-Chinese dictionary which consists of a ‘Dictionary’ class that has various methods for loading data, word searching, displaying Chinese counterparts and running the main loop for the dictionary tool.

Here is an overview of the software design idea and key algorithms used in this project.

Data loading: The ‘load_data’ method/function read a file from the specfied file path and extracts English and Chinese words from each line from word.txt file.It uses regular expression to split the line into parts based on tab(‘\t’) or whitespace(‘\s+’) characters, and stores the English words, Chinese words and their corresponding position in the dictionary.

Word Search: The ‘search_words’ method searches for English words that contain the input letters provided by the user. It iterates through the list of English words stored in the ‘english_words’ attribute and checks if the input letters are present in each word using the ‘in’ operator. Matching words are appended to a list along with a count of the total number of matches.

Display Chinese Counterpart: The ‘display_chinese_counterpart’ method takes an English word as input and retrieves its corresponding Chinese word from the dictionary mapping stored in the ‘dictionary’ attribute. It uses the ‘get’ method of the dictionary to retrieve the value associated with the given key, and prints the English and Chinese words as output.

Main Loop: The ‘run_dictionary_tool’ method implements the main loop of the dictionary tool. It displays a prompt for the user to enter input letters, and then calls the ‘search_words’ method to get matching words. It then displays the matching words along with their count. If there are matching words, it prompts the user to select a word and calls the ‘display_chinese_counterpart’ method to display the corresponding Chinese counterpart. The loop continues until the user enters "quit" to exit.

After all, the code is about a simple design where English and Chinese words are loaded from a file, stored in lists and a dictionary, and then searched and displayed based on user input. The key algorithms used are regular expression splitting for data loading, string matching for word search, and dictionary mapping for retrieving Chinese counterparts.
