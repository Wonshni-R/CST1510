"""
RECORD CHECK  -  my version
===========================

Name  :  Wonshni Reedoy
Lane  :  AI
Date  :  30th September 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

"""Process records by comparing values against limits, calculating difference and percentage, assigning status, and tracking over-limits,"""

overlimit_count = 0
while True:
    label = input("Enter dataset name: ")
    
    if label == "quit":   # Stop the program when the user enters "quit".
        break

    value = float(input("Enter a value:"))
    limit = float(input("Enter a limit: "))
    
    
    difference = float(limit) - float(value)  
    percent = (float(value) / float(limit)) * 100 

    # Determine the status based on the percentage used.
    if percent >=100: 
        status = "OVER LIMIT"
        overlimit_count +=1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    print ("=" * 34)
    print (f" RECORD CHECK - {label}")
    print ("=" * 34)
    print (f" {'Used': <17}: {float(value): >10.2f}")
    print (f" {'Total': <17}: {float(limit): >10.2f}")
    print (f" {'Free': <17}: {float(difference): >+10.2f}")
    print (f" {'Percent': <17}: {float(percent): >10.2f} {'%'}" )
    print (f" {'Status': <17}: {status: >10}")
    print ("=" * 34)

print(f" {'Over Limit Count': <17}: {overlimit_count: >10}")


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)    #Division by zero error
#    [ ] Check every variable name says what it holds
