"""
RECORD CHECK  -  my version
===========================

Name  :  Wonshni Reedoy
Lane  :  AI
Date  :  22nd October 2026

Run it:   python template.py
"""


"""Load records from a file and report their usage, percentage and status."""


class Record:
    """Represent a record with a value and limit."""

    over_limit_count = 0   # Shared counter for all Record objects.


    def __init__ (self, label, value, limit):
        """Store the record's label, value and limit."""
        self.label = label
        self.value = value
        self.limit = limit
        self.difference = limit - value
        self.percentage = value/limit * 100

    
    def status(self):
        """Return the status based on the record's percentage"""
        p = (self.value / self.limit) * 100

        if p >= 100:
            return "OVER LIMIT"
        elif p  >= 90:
            return "WARNING"
        else:
            return "OK"


def load_records(path):
    """Return a list of Record objects read from a file."""
    records = []

    # Read each line and create a Record object.
    with open(path, "r") as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))

    return records


records = load_records("records.txt")   # Load records from the data file.


Record.over_limit_count = 0  # Reset the class-level counter before processing records.


for record in records:
    record_status = record.status()


    print ("=" * 34)
    print (f" RECORD CHECK - {record.label}")
    print ("=" * 34)
    print (f" {'Used': <17}: {record.value: >10.2f}")
    print (f" {'Total': <17}: {record.limit: >10.2f}")
    print (f" {'Free': <17}: {record.difference: >+10.2f}")
    print (f" {'Percent': <17}: {record.percentage: >10.2f} {'%'}")
    print (f" {'Status': <17}: {record.status(): >10}")
    print ("=" * 34)


    # Update the shared class-level counter
    if record_status == "OVER LIMIT":
        Record.over_limit_count =+ 1  


print (f"\n {'Over Limit Count': <17}: {Record.over_limit_count: >10}")  # Print the final over-limit count once, after the loop.



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
