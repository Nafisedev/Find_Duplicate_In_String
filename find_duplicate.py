import pandas as pd


dataset = pd.read_csv('C:/Users/Zahra Mirzaei/Desktop/project-1/dataset.csv')
dataset.head()
type(dataset)

for index, row in dataset.iterrows():
    current_row = pd.Series(
        data=row["fruit"].strip("[").strip("]").split(", "))
    temp = []
    for index, value in enumerate(current_row.values):
        container = current_row.str.contains(value).map(int).to_list()
        if sum(container) > 1:
            for i, v in enumerate(container):
                if v == 0 and current_row[i] not in temp:
                    temp.append(current_row[i])

        if len(temp) == 0 and index == len(current_row) - 1:
            temp.extend(current_row.to_list())
