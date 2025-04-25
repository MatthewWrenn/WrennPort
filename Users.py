import csv
#takes useer name and paassword and stores them in a vaariable
#for loop allows 3 attempts
for i in range(1, 4):
    username = input("Username: ").strip()
    passw = input("Password: ").strip()
    
    # Check both username and password are letters and numbers
    if username and username.isascii() and passw and passw.isascii():
        storedN = username
        storedP = passw
        #opens the file in read mode
        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            # Check if username and password match any entry in the CSV file
            authenticated = False
            for row in reader:
                if row[0] == storedN and row[1] == storedP:
                    print("User name and password accepted")
                    authenticated = True
                    break
            
            if not authenticated:
                print("Invalid username or password")
                continue  # if you still have attempts left, this will keep the outer loop going
        break  # This will break the outer loop if the username and password are correct
    else:
        print("No blank spaces and ASCII characters only")
else:
    print("Too many attempts")