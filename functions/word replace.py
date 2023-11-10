def replace_word():

    str = "hi guys, I am Utibe, and hi hi hi hi"
    print(str)
    word_to_replace = input("Enter the word to be replaced:\n")
    word_replacement = input("Enter the word replacement:\n")
    print(str.replace(word_to_replace, word_replacement))

replace_word()