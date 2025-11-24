import re
def create_inverted_index(files):
    inverted_index = {}
    
    for filename in files:
        try:
            with open(filename, 'r') as f:
                text = f.read().lower()
        except FileNotFoundError:
            print(f"File {filename} not found. Skipping.")
            continue

        words = re.findall(r'\w+', text)

        for pos, word in enumerate(words):
            if word not in inverted_index:
                inverted_index[word] = {}

            if filename not in inverted_index[word]:
                inverted_index[word][filename] = []

            inverted_index[word][filename].append(pos)

    return inverted_index

def search_query(index, word):
    word = word.lower()
    return index.get(word, None)

files=["t1.txt","t2.txt","t3.txt"]
index = create_inverted_index(files)
print("Inverted Index created successfully!")

while True:
    q = input("Enter a word to search (or 'exit'): ")
    if q == "exit":
        break

    result = search_query(index, q)

    if result:
        print(f"\nWord '{q}' found in:")
        for file, positions in result.items():
                print(f"  -> {file} | positions: {positions} | frequency: {len(positions)}")
    else:
        print(f"\nWord '{q}' not found in any file.")
