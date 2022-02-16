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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
def task_0(texts, calls):
    incoming_number=texts[0][0]
    answering_number=texts[0][1]
    time=texts[0][2]

    incoming_number_2=calls[-1][0]
    answering_number_2=calls[-1][1]
    time_2=calls[-1][2]
    during_2=calls[-1][3]

    print("First record of texts, {} texts {} at time {}".format(incoming_number, answering_number, time))
    print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(incoming_number_2, answering_number_2, time_2, during_2))

if __name__=='__main__':
    texts,calls=read_csv()
    task_0(texts,calls)
