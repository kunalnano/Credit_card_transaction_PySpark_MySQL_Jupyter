# Data Engineering Take Home

## Overview
Candidate can use this code challenge as a showcase to demonstrate skills and knowledge on both Data Enginering and Software Engineering practices.

The candidate should be provided with 5 files:
- This README file
- unit-tests.py
- datasets/fraud.zip
- datasets/transaction-001.zip
- datasets/transaction-002.zip

We expect the candidate to write production grade code.

We are expecting the candidate to write unittest, (integration tests are a bonus and not required).


If at any point, you feel that you are missing a piece of information from the description, please make your best guess and make a note of it for discussions during the interview.


In part II and III, the candidate will needs the mapping of credit_card_vendor to list of card prefix.

```
# prefix_vendor = list of credit first digits that are representing this vendor.
maestro = ['5018', '5020', '5038', '56##']
mastercard = ['51', '52', '54', '55', '222%']
visa = ['4']
amex = ['34', '37']
discover = ['6011', '65']
diners = ['300', '301', '304', '305', '36', '38']
jcb16 = ['35']
jcb15 = ['2131', '1800']
```


# Part 0
Setup a Docker or Vagrant environment (we suggest to use centos 7 and install on it: PySpark, a SQL database (postgres or MySQL are fine)).


# Part I
Using Python, read fraud.zip and store the data into SQL database.

# Part II
Using PySpark, sanitize data of both transaction-001.zip and transaction-002.zip by removing transactions where column `credit_card_number` is not part of the previous provided list.

example: a credit card that start with `98` is not a valid card, it should be discarded from the sanitized dataset.
 
# Part III
- Candidate should assume that going forward, only the sanitized dataset should be used.

- Find in the sanitized dataset if it contains fraudulent transactions (from fraud.zip) and report their number.

- Create a report of the number of fraudulent transactions per state.

- Create a report of the number of fraudulent transactions per card vendor,eg: maestro => 45, amex => 78, etc..

- Create a dataset of 3 columns and save in both JSON and in a binary fileformat that you believe it's suitable for BI analysis:
  - column 1: masked credit card: replace 9 last digits of the credit card with `*`
  - column 2: ip address
  - column 3: state
  - column 4: sum of number of byte of (column 1 + column 2 + column 3)

## Expectations
As mentioned in the overview, we expect you to write unit tests.
To get you started, we have provided a sample unit test in the other file in the assignment.
If you already have a process to unit test your pipeline code, please feel free to use your own.

