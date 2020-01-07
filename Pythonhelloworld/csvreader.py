import unicodecsv
from datetime import datetime as dt

# open a csv file with a header row
with open('enrollments.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)
print(enrollments[0])

# Takes a date as a string, and returns a Python datetime object.
# If there is no date given, returns None
def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d %H:%M:%S')

# Takes a string which is either an empty string or represents an integer,
# and returns an int or None.
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

# Clean up the data types in the enrollments table
for enrollment in enrollments:
    enrollment['Date'] = parse_date(enrollment['Date'])
    enrollment['Enrolled'] = parse_maybe_int(enrollment['Enrolled'])
print(enrollments[0])

## Find the total number of rows and the number of unique students (account keys)
## in each table.
enrollment_num_rows = len(enrollments)
enrollment_num_unique_students = set()
for e in enrollments:
    enrollment_num_unique_students.add(e['Name'])

print(f"Total rows {enrollment_num_rows}")
print(f"Unique rows {len(enrollment_num_unique_students)}")
print(f"Enrolled are: {enrollment_num_unique_students}")
