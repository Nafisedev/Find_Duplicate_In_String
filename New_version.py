import pandas as pd

dataset = pd.read_excel(
    'C:/Users/Zahra Mirzaei/Desktop/project-1/test_data.xlsx')
dataset.head()

dataset['Name'] = dataset['Name'].str.lower()
dataset = dataset.groupby('objcode').agg(list).reset_index()

temp = {}
for index, current_row in enumerate(dataset['Name']):
    temp[index] = []
    if len(current_row) < 2:
        temp[index].extend(current_row)
        continue
    for value in current_row:
        container = pd.Series(data=current_row).str.contains(
            value).map(int).to_list()
        if sum(container) > 1:
            for i, v in enumerate(container):
                if v == 0 and current_row[i] not in temp[index]:
                    temp[index].append(current_row[i])

dataset['Name'] = pd.Series(data=temp.values())
print(dataset)
