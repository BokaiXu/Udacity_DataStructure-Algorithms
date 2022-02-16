def read_csv():
    """
    Read file into texts and calls.
    It's ok if you don't understand how to read files.
    """
    import csv
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)

    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)

    return texts, calls


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
def task_1(texts, calls):
    list_number=[]
    for i in texts:
        list_number.append(i[0])
        list_number.append(i[1])
    for i in calls:
        list_number.append(i[0])
        list_number.append(i[1])
    unique_number=set(list_number)
    print('There are {} different telephone numbers in the records.'.format(len(unique_number)))

if __name__=='__main__':
    texts,calls=read_csv()
    task_1(texts,calls)
