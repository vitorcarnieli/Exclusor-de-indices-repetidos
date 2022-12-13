import pandas as pd


def remove_reps(list):
    l = []
    for i in list:
        if i not in l:
            l.append(i)
    l.sort()
    return l

check_name_list = []
popsup_one = []
popsup_two = []
popsup_three = []
popsup_for = []
df = pd.read_excel('listadenomes.xlsx')

for name in df['Nome']:
    if len(check_name_list) == 1:
        popsup_one.append(check_name_list[0])
        check_name_list = []
    if len(check_name_list) == 2:
        popsup_two.append(check_name_list[0])
        check_name_list = []
    if len(check_name_list) == 3:
        popsup_three.append(check_name_list[0])
        check_name_list = []
    if len(check_name_list) == 4:
        popsup_for.append(check_name_list[0])
        check_name_list = []
    for check_name in df['Nome']:
        if check_name == name:
            check_name_list.append(check_name)

print(remove_reps(popsup_for))
print()
print()
print(remove_reps(popsup_three))
print()
print()
print(remove_reps(popsup_two))
print()
print()
print(popsup_one)
print()
print()
