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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
def task_4(texts, calls):
    list_1=[]
    for text in texts:
        list_1.append(text[0])
        list_1.append(text[1])
    for call in calls:
        list_1.append(call[1])
    list_1_unique=set(list_1)
    list_2=[]
    for call in calls:
        list_2.append(call[0])
    list_2_unique=set(list_2)
    result=[]
    for i in list_2_unique:
        if i not in list_1_unique:
            result.append(i)
    result=sorted(result)
    print("These numbers could be telemarketers: ")
    for i in result:
        print(i)

if __name__=='__main__':
    texts,calls=read_csv()
    task_4(texts,calls)
