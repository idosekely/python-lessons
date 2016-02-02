import csv
import pickle
__author__ = 'sekely'

'''
files can be used to save your work between sessions, program runs and even
passing data from one place to another.
files generally opened in read or write mode (or both), and must be closed.
'''

f = open("my_first_file.txt", 'wr')  # opening new file for read and write
lines = ['hello',
         'world!']
f.writelines(lines)

f.write("this is new line\n")  # \n uses to mark new line
f.write("this is the final line\n")
f.close()

# you can save data to file, and use it for later
f = open('save_file.save', 'w')  # we only need to save data to the file, so no need to read
d = {'a': 1, 'b': 2}
pickle.dump(d, f)
f.close()

f = open('save_file.save', 'r')  # now we only need to read from the file
d = pickle.load(f)
print d
f.close()

# another useful file type is csv ("Comma Separated Values")
# it saves data in sort of "table" way, that later can be used by Excel

csv_file = open('my_data.csv', 'w')
writer = csv.writer(csv_file)
headers = ['first_name', 'last_name']
writer.writerow(headers)
writer.writerow(['John', 'Smith'])
writer.writerow(['Bob', 'Lee'])
writer.writerow(['Your', 'Name'])
f.close()

# some advanced stuff

# you can open file as "context". meaning that the file is kept open for that block only
with open("context_file", 'w') as f:
    f.write("you don't need to close the file\n")
    f.write("at the end of the blcok\n")
    f.write("the context will do it for you\n")

# csv has a special writer, to save dicts.
# since dicts are very similar to tables (why?), this is very convenient
with open("new_table.csv", 'w') as f:
    headers = ['first_name', 'last_name']
    writer = csv.DictWriter(f, headers)
    writer.writeheader()
    writer.writerow({'first_name': 'John', 'last_name': 'Smith'})
    writer.writerow({'first_name': 'Bob', 'last_name': 'Lee'})

# and reading back csv:
rows = []
with open("new_table.csv", 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)
print rows
