h = open("departements_fr.csv", "r", encoding="ISO-8859-1")
data = h.read()

# print(data)

rows = data.split("\n")
# rows_slice = rows[0:5]
# print("\n")
# print(rows[0:5])

#ten_rows = rows[0:10]

final_data = [] # liste vide

for row in rows:
    split_row = row.split(",")
    final_data.append(split_row)

print(final_data[0:5])


first_list = final_data[0]
first_list_first_value = first_list[0]
print(first_list_first_value)

# ou

first_list_first_value = final_data[0][0]
print(first_list_first_value)

second_list_first_value = final_data[1][0]
print(second_list_first_value)

second_list_second_value = final_data[1][1]
print(second_list_second_value)

department_list = []

for row in final_data:
    dpt_list = row[0]
    department_list.append(dpt_list)

print(department_list)





