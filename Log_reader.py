fails = 0
passes = 0
for i in range(1, 5):
    if i == 1:
        with open('log_1.txt', 'r') as log:
         for line in log:
            if 'FAIL' in line:
                fails += 1
            if 'PASS' in line:
                passes += 1
    elif i == 2:
        with open('log_2.txt', 'r') as log:
            for line in log:
                if 'FAIL' in line:
                    fails += 1
                if 'PASS' in line:
                    passes += 1
    elif i == 3:
        with open('log_3.txt', 'r') as log:
            for line in log:
                if 'FAIL' in line:
                    fails += 1
                if 'PASS' in line:
                    passes += 1
    else:
        with open('log_4.txt', 'r') as log:
            for line in log:
                if 'FAIL' in line:
                    fails += 1
                if 'PASS' in line:
                    passes += 1

print(f'Number of passes: {passes} and number of fails: {fails}')