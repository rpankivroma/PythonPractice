"""
Python RegEx Task: Log File Analyzer

📌 Goal
Write a Python program that analyzes a text log using regular expressions.

📄 Given text (use this exact string)
2025-12-20 14:32 ERROR User john.doe@email.com failed to login from IP 192.168.1.10
2025-12-20 14:35 INFO User alice99@gmail.com logged in from IP 10.0.0.5
2025-12-21 09:10 WARNING User bob_smith@outlook.com password expires soon
2025-12-21 09:15 ERROR User admin@company.org failed to login from IP 172.16.0.3

📝 Tasks

Task 1 — Find all email addresses
Use re.findall() to extract all email addresses from the text.

Task 2 — Find all IP addresses
Use re.findall() to extract all IPv4 addresses.

Task 3 — Find only ERROR messages
Use re.search() or re.findall() to get only lines that contain ERROR.

Task 4 — Split the log into separate lines
Use re.split() to split the text into individual log lines.

Task 5 — Mask email usernames
Use re.sub() to replace the username part of each email with "***"
Example:
john.doe@email.com → ***@email.com

Task 6 — Case-insensitive search
Check if the word "error" exists in the log regardless of case using a regex flag.

🎯 Requirements
Use the re module
Use at least one regex flag
Print clear, readable output
No external libraries
"""

# Answer
import re

log_text = """
2025-12-20 14:32 ERROR User john.doe@email.com failed to login from IP 192.168.1.10
2025-12-20 14:35 INFO User alice99@gmail.com logged in from IP 10.0.0.5
2025-12-21 09:10 WARNING User bob_smith@outlook.com password expires soon
2025-12-21 09:15 ERROR User admin@company.org failed to login from IP 172.16.0.3
"""
# --------------------------------------------------
# Task 1 — Find all email addresses
# --------------------------------------------------
emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', log_text)
print("Emails found:")
for email in emails:
    print("-", email)

# --------------------------------------------------
# Task 2 — Find all IP addresses
# --------------------------------------------------
ips = re.findall(r'\b\d{1,3}(?:\.\d{1,3}){3}\b', log_text)
print("\nIP addresses found:")
for ip in ips:
    print("-", ip)

# --------------------------------------------------
# Task 3 — Find only ERROR messages
# --------------------------------------------------
error_lines = re.findall(r'^.*ERROR.*$', log_text, re.MULTILINE)
print("\nERROR log entries:")
for line in error_lines:
    print(line)

# --------------------------------------------------
# Task 4 — Split log into separate lines
# --------------------------------------------------
lines = re.split(r'\n+', log_text.strip())
print("\nLog lines:")
for line in lines:
    print("-", line)

# --------------------------------------------------
# Task 5 — Mask email usernames
# --------------------------------------------------
masked_log = re.sub(
    r'([\w\.-]+)@([\w\.-]+\.\w+)',
    r'***@\2',
    log_text
)

print("\nLog with masked emails:")
print(masked_log)

# --------------------------------------------------
# Task 6 — Case-insensitive search for "error"
# --------------------------------------------------
has_error = re.search(r'error', log_text, re.IGNORECASE)

if has_error:
    print("The word 'error' was found (case-insensitive).")
else:
    print("The word 'error' was NOT found.")

"""
Terminal output:
PS C:\Users\trade> & C:/Users/trade/AppData/Local/Programs/Python/Python314/python.exe "c:/Users/trade/Desktop/PythonPractice/PythonPractice/W3School/Python Tutorial/PythonRegEx.py"
Emails found:
- john.doe@email.com
- alice99@gmail.com
- bob_smith@outlook.com
- admin@company.org

IP addresses found:
- 192.168.1.10
- 10.0.0.5
- 172.16.0.3

ERROR log entries:
2025-12-20 14:32 ERROR User john.doe@email.com failed to login from IP 192.168.1.10
2025-12-21 09:15 ERROR User admin@company.org failed to login from IP 172.16.0.3

Log lines:
- 2025-12-20 14:32 ERROR User john.doe@email.com failed to login from IP 192.168.1.10
- 2025-12-20 14:35 INFO User alice99@gmail.com logged in from IP 10.0.0.5
- 2025-12-21 09:10 WARNING User bob_smith@outlook.com password expires soon
- 2025-12-21 09:15 ERROR User admin@company.org failed to login from IP 172.16.0.3

Log with masked emails:

2025-12-20 14:32 ERROR User ***@email.com failed to login from IP 192.168.1.10
2025-12-20 14:35 INFO User ***@gmail.com logged in from IP 10.0.0.5
2025-12-21 09:10 WARNING User ***@outlook.com password expires soon
2025-12-21 09:15 ERROR User ***@company.org failed to login from IP 172.16.0.3

The word 'error' was found (case-insensitive).
"""