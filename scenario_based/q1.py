"""
1. Log Processing
You are given a list of logs:
logs = ["ERROR: Disk full", "INFO: User login", "ERROR: Timeout", "INFO: Logout"]
Task: Count how many times each log level appears and return a dictionary.
"""

freq = {}

# if taking logs list from user
# logs = input().split(',')

logs = ["ERROR: Disk full", "INFO: User login", "ERROR: Timeout", "INFO: Logout"]

for log in logs:

    data = log.split(":")[0]

    if data in freq:

        freq[data] += 1

    else:
        
        freq[data] = 1

print(freq)


