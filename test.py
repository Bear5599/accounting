import os

file_path = os.path.expanduser("~/Documents/accounting_files/")
user_input = str(input("Enter a search word for the file: "))
def test_program(folder, search):
    results = []
    with open(folder, "r") as file:
        for lines in file:
            if search.lower() in lines.lower():
                results.append(lines)
    print(f"There are {len(results)} occurances in this file")
    for items in results:
        print(items)
test_program(file_path, user_input)




