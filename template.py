"""
RECORD CHECK  -  my version
===========================

Name  :  Wonshni Reedoy
Lane  :  AI 
Date  :  25th September 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



label = input("Enter dataset name: ")
first = float(input("Enter number of rows loaded: "))
second = float(input("Enter number of rows expected: "))

difference = float(second) - float(first)
percent = (float(first) / float(second) *100)

remaining_percent = (float(difference) / float(second) * 100)
# It indicates the percentage of capacity that is still free.


print ("=" * 34)
print (f" RECORD CHECK - {label}")
print ("=" * 34)
print (f" {'Used': <13}: {float(first) : >10.2f}")
print (f" {'Total': <13}: {float(second) : >10.2f}")
print (f" {'Free': <13}: {float(difference): >+10.2f}")
print (f" {'Percent': <13}: {float(percent): >10.2f} {'%'}")
print (f" {'Percent Free' : <13}: {float(remaining_percent): >10.2f} {'%'}")
print ("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal    #Division by zero error
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
