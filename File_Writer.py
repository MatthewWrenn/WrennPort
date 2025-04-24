#import choice to generate fake test results
from random import choice
#set pass fail globals to 0
PASS = 0
FAIL = 0
#Create a loop to generate 50 test results also creates new file in append mode for results
with open('test.txt', 'a') as f:
    for i in range(50):
        pf = choice(['PASS', 'FAIL'])
        if pf == 'PASS':
            PASS += 1
        else:
            FAIL += 1
        # Write each result inline
        f.write(f'{pf}\n')

# Open the file again in append mode to write totals at the end
with open('test.txt', 'a') as f:
    f.write(f'\nPASS: {PASS}\n')
    f.write(f'FAIL: {FAIL}\n')
    f.write(f'TOTAL: {PASS + FAIL}\n')