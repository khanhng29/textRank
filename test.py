import csv
from preprocessing import process_text, process_after
def read_csv_file(file_path):
    summaries = [] 
    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            summary = row[1]
            summaries.append(summary)
    return summaries

file_path = './data/summary_ori.csv'

summary_list = read_csv_file(file_path)
# summary_ori = []
# for _ in summary_list:
#     summary_ori.append(process_after(process_text(_)))
# for _ in summary_ori:
#     print(_)

# ori_length = []  # Initialize an empty list to store word counts
# for paragraph in summary_ori:
#     word_count = len(paragraph.split())  # Count the number of words in the paragraph
#     ori_length.append(word_count)  # Append the word count to the list




# Print or further process the word_counts list
# print(len(word_counts))


