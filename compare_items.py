import csv

items_dict = {}

for i in range(6):
    with open("Item List" + str(i+1) + ".csv", "rt") as item_list:
        reader = csv.reader(item_list)
        for row in reader:
            if row[0] not in items_dict:
                items_dict[row[0]] = {"Item List" + str(i+1):str(row[-1])}
            else:
                items_dict[row[0]]["Item List" + str(i+1)] = str(row[-1])

        item_list.close()

# Print out in seperate csv
outfile = open('Results.csv', 'wt',newline='')
writer = csv.writer(outfile,delimiter=",",quoting=csv.QUOTE_MINIMAL)

for key in items_dict:
    values = items_dict.get(key)
    row_to_write = []
    row_to_write.append(key)
    for i in range(6):
        if "Item List" + str(i+1) in values:
            row_to_write.append(values["Item List" + str(i+1)])
        else:
            row_to_write.append("N/A")
    if row_to_write[1] == row_to_write[2] == row_to_write[3] == row_to_write[4] == row_to_write[5] == row_to_write[6]:
        row_to_write.append("Consistent")
    writer.writerow(row_to_write)

outfile.close()