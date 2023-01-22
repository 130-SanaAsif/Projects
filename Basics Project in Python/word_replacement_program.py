def word_replacement():
    str = "Hello, My name is Sana Asif. I am pursuing Btech in Information Technology."
    word_to_replace = input("Enter the word to replace: ")
    word_replace = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word_replace))

word_replacement()