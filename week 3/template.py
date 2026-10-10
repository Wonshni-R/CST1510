"""
RECORD CHECK  -  my version
===========================

Name  :  Wonshni Reedoy
Lane  :  AI 
Date  :  07th September 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



def status_of(percent):
    """Returns OVER LIMIT, WARNING, or OK based on the percentage."""
    if percent >= 100:
        return"OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

    
def check(value, limit):
    """Calculates and returns the difference and percentage using value and limit."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Prints the details of the record in a formatted report."""
    print ("=" * 34)
    print (f"RECORD CHECK -  {label}")
    print ("=" * 34)
    print (f"{'Used': <17}: {value:>10.2f}")
    print (f"{'Total': <17}: {limit:>10.2f}")
    print (F"{'Free': <17}: {difference:>+10.2f}")
    print (f"{'Percent': <17}: {percent:>10.2f} {'%'}")
    print (f"{'Status': <17}: {status:>10}")
    print ("=" * 34)


overlimit_count = 0

while True:
    label = input("Enter a name: ")      

    if label == "quit":
        break

    value = float(input("Enter a value: "))   
    limit = float(input("Enter a limit: "))   


    difference, percent = check(value, limit)                                          
    status = status_of(percent)               


    print_report(label, value, limit, difference, percent, status)


    if status == "OVER LIMIT":
        overlimit_count += 1


print (f"{'Over Limit Count':<17}: {overlimit_count:>10}")


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
