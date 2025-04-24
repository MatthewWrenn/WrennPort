#sets global pass/fail variables to 0
fails = 0
passes = 0
#for loop for each of the 4 log files
for i in range(1, 5):
    #checks to see if it's the first log file
    if i == 1:
        with open('log_1.txt', 'r') as log:
         for line in log:
            if 'FAIL' in line:
                fails += 1
            if 'PASS' in line:
                passes += 1
    #checks to see if it's the second log file
    elif i == 2:
        with open('log_2.txt', 'r') as log:
            for line in log:
                if 'FAIL' in line:
                    fails += 1
                if 'PASS' in line:
                    passes += 1
    #checks to see if it's the third log file
    elif i == 3:
        with open('log_3.txt', 'r') as log:
            for line in log:
                if 'FAIL' in line:
                    fails += 1
                if 'PASS' in line:
                    passes += 1
    #checks to see if it's the fourth log file
    else:
        with open('log_4.txt', 'r') as log:
            for line in log:
                if 'FAIL' in line:
                    fails += 1
                if 'PASS' in line:
                    passes += 1
#prints the number of passes and fails
print(f'Number of passes: {passes}\nNumber of fails: {fails}')