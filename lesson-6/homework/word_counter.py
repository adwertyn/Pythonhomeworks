def report(total_number_words, top_5_words):  # Save report to file
    with open("word_count_report.txt", 'a') as file:
        file.write(f"Total words: {total_number_words}\n")
        file.write("Top 5 most common words:\n")
        file.write(top_5_words)

def word_count():  # Count and display words
    with open('sample.txt', 'r') as file:
        text = file.read()
    # Remove punctuation and split into words
    text = text.replace('.', ' ').replace('\n',' ').replace(',', ' ').split()
    set_text = set(text)
    total_number_words = len(text)
    num_words_list = []

    for i in set_text:
        num_word = text.count(i)
        num_words_list.append([i, num_word])
    
    # Sort by frequency (descending)
    num_words_list.sort(key=lambda x: x[1], reverse=True)

    print(f"Total words: {total_number_words}")
    print("Top 5 most common words: ")

    top_5_words = ''
    i = 0
    for word, count in num_words_list:
        top_5_words += f'{word} - {count}\n'
        i += 1
        if i == 5:
            break

    print(top_5_words)
    report(total_number_words, top_5_words)  # Save report

def user_sample():  # Get text input from user
    text = input("Please enter text: ")
    with open('sample.txt', 'w') as file:
        file.write(text)
    word_count()

# Clear old report
with open('word_count_report.txt', 'w') as f:
    f.write('')
# Clear sample if exists
with open('sample.txt', 'w') as file:
    pass

# Check if sample.txt is empty
with open('sample.txt', 'r') as file:
    text = file.read()
    if len(text) == 0:
        user_sample()
    else:
        word_count()
