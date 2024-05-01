import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data


#################
file_path = "./data/final.csv"
data = read_csv_file(file_path)

# for _ in data:
#     print(_['id'])
# data = data[:2]
# print(data['text'])
# arr = []
# for _ in range(len(data)):
#     data[_]['text']
# texts = [item['text'] for item in data]
# print(texts)
# for _ in texts:
#     print(len(_))