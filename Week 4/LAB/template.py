"""
RECORD CHECK  -  my version
===========================

Name  :  Wonshni Reedoy
Lane  :  AI
Date  :  15th October 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent):
    """Returns status based on the percentage."""

    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
    

def check_record (value, limit):
    """Calculates and returns the difference, percentage using value and limit"""

    difference = value - limit
    percent = (value / limit) * 100
    status = status_of(percent)

    return difference, percent, status


def print_report (label, value, limit, difference, percent, status):
    """Prints the details of a record in a formatted report."""
    print ("=" * 34)
    print (f"RECORD CHECK - {label}")
    print ("=" * 34)
    print (f"{'Used': <17}: {value: >10.2f}")
    print (f"{'Total': <17}: {limit: >10.2f}")
    print (f"{'Free': <17}: {difference: >+10.2f}")
    print (f"{'Percent': <17}: {percent: >10.2f} {'%'}")
    print (f"{'Status': <17}: {status: >10}")
    print ("=" * 34)


def load_records(path):
    """Reads records from a file and returns a list of dictionaries."""
    records = []
    with open(path, "r") as f:   # Open the input file in read mode.
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({
                "label": label.strip(), 
                "value": float(value),
                "limit": float(limit)
            })
            
    return records 


records = load_records("./records.txt")  # Load records from the input file.

overlimit_count = 0    # Initialise the counter for records exceeding their limits.

with open("./checked_W04.txt", "w") as f:  # Open the ouput file in write mode.
    for record in records:
        label = record["label"]
        value = record["value"] 
        limit = record["limit"]

        difference, percent, status = check_record(value, limit)

        print_report(label, value, limit, difference, percent, status)


        if status == "OVER LIMIT":
            overlimit_count +=1    # Count records that exceed their limits.


        f.write(f"{label}, {status}\n")  

print (f"{'Over Limit Count': <17}: {overlimit_count: >10}")  





# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down                              # It raises a FileNotFoundError.
#    [ ] Check every function still does one job
