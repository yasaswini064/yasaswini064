#mini project
#dictionary of words

dictionary_words = {}
while True:
    print("\nDictionary Management System:")
    print("1. Add a word")
    print("2. Search for a meaning")
    print("3. Display all words")
    print("4. Update meaning")
    print("5. Delete a word")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        word = input("Enter the word: ").strip()
        meaning = input("Enter the meaning: ").strip()
        dictionary_words[word] = meaning
        print("Word added successfully.")

    elif choice == "2":
        word = input("Enter the word to search: ").strip().lower()
        if word in dictionary_words :
            print("Meaning:" , dictionary_words[word])
        else:
            print("Meaning not found.")

    elif choice == "3":
        if dictionary_words:
            print("All words and their meanings:")
            for word, meaning in dictionary_words.items():
                print(f"{word}: {meaning}")
        else:
            print("The dictionary is empty.")

    elif choice == "4":
        word = input("Enter the word to update: ").strip()
        if word in dictionary_words:
            meaning = input("Enter the new meaning: ").strip()
            dictionary_words[word] = meaning
            print("Meaning updated successfully.")
        else:
            print("Word not found.")

    elif choice == "5":
        word = input("Enter the word to delete: ").strip()
        if word in dictionary_words:
            del dictionary_words[word]
            print("Word deleted successfully.")
        else:
            print("Word not found.")

    elif choice == "6":
        print("exit")
        break

    else:
        print("Invalid choice. Please try again.")


