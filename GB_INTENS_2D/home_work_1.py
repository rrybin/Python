file = open('salary_ascii.csv')

salary_data = file.readlines()

salary=[]
for _line in salary_data:
    salary.append(_line.split(sep=','))
    
workers = []
for _line in salary:
    workers.append(_line.pop(0))

temp = []
for _idx, _line in enumerate(salary):
    temp.append(sum(list(map(float, _line)))/len(salary[_idx]))

for _idx, _line in enumerate(temp):
    print(f'Средняя зарплата сотрудника {workers[_idx]} = {_line:.2f}')