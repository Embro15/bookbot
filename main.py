def count_letters(file):
    letters = {}
    for i in file:
        count = 0
        if i in letters.keys():
            pass
        else:
            for j in file:
                if j == i:
                    count += 1
            letters[i] = count
    return letters
        
    

def count_words(file):
    words = file.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def sort_list(dict):
    sorted_letters = []
    for i in dict:
        sorted_letters.append({"letter" : i, "num" : dict[i]})
    sorted_letters.sort(reverse = True, key = sort_on)
    return sorted_letters


def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
    
    count = count_words(file_contents)

    print(f"--- Begin report of {file_path} --- ")
    print(f"{count} words found in the document")

    letters = {}
    letters = count_letters(str.lower(file_contents))
    sorted = sort_list(letters)

    for i in sorted:
        if not i["letter"].isalpha():
            continue
        print(f"The {i['letter']} character was found  {i['num']} times")
    print ("----- End Report ----")


main()