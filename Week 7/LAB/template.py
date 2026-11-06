"""
RECORD CHECK  -  my version
===========================

Name  :  Wonshni Reedoy
Lane  :  AI 
Date  :  04th November 2026

Run it:   python template.py
"""


"""This program reads messy records, cleans and parses them into dictionaries, 
classifies their ratings, and reports the total number of flagged reports."""


def parse_line(raw_line):
    """Clean and convert one raw survey line into a dictionary."""

    parts = raw_line.strip().split(",")  # Remove unnecessay spaces and separate the fields at commas.

    record = {"survey": parts[0].strip().lower()}  # Standardise the survey name to lowercase.


    for part in parts[1:]:

        # Separate the field name from its value at the equals sign.
        key, value = part.split("=")

        # Remove extra spaces and standardise the field name.
        key = key.strip().lower()
        value = value.strip()

        # Convert numerical values into integers.
        try:
            record[key] = int(value)
        except ValueError:
            raise ValueError (f"Invalid number for '{key}': '{value}'")
        
    return record


def status_of(record):
    """Flag surveys with rating below 3."""

    if record["rating"] < 3:  # Check whether the rating is below the accepted threshold.
        return "FLAGGED"
    else:
        return "OK"


raw_records = []

with open ("raw_records.txt", "r") as file:
    for line in file:
        raw_records.append(line)


total_records = 0
total_flagged = 0


# Parse, classify and report each record.
for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)

    print (record, "-", status)

    total_records += 1

    if status == "FLAGGED":
        total_flagged += 1 


print ("\nTotal records:", total_records)
print ("\nTotal flagged:", total_flagged)


# Test the function with a rating that cannot be converted into an integer.
try:
    parse_line("Survey_2036, rating=high, age=22")
except ValueError as error:
    print ("\nError:", error)



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
