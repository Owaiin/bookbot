with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    split_words = file_contents.split()
    total_words = len(split_words)
    
    
    def letter_count(content):
        counted_letters = {}
        lowered_content = content.lower()
        for letter in lowered_content:
            if letter in counted_letters:
                counted_letters[letter] += 1
            else:
                counted_letters[letter] = 1
        return counted_letters
    
    total_letters = letter_count(file_contents)
    letters_list = list(total_letters.items())
    letters_list.sort(key=lambda x: x[1], reverse=True)
    
    
    print(f"---Beginning Report of books/frankenstein.txt---")
    print(f"{total_words} words were found in the document")
    for key, value in letters_list:
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")
    print("---End Report---")