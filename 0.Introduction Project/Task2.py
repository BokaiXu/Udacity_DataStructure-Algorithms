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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
def task_2(texts, calls):
    from collections import defaultdict
    time=defaultdict(int)
    for call_ in calls:
        time[call_[0]]+=int(call_[3])
        time[call_[1]]+=int(call_[3])
    time_true={k: v for k, v in sorted(time.items(), key=lambda item: item[1], reverse=True)}
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(list(time_true.keys())[0],list(time_true.values())[0]))

if __name__=='__main__':
    texts,calls=read_csv()
    task_2(texts,calls)
