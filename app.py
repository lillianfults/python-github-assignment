print ("Welcome to my Python program!") #welcome message
hours = input("How many hours did you study today? ") #enter # of hours input
hours = float(hours) #converts hours to flaot value
weekly_hours = hours * 7 #multiply hours by 7 so can get weekly hours
print(f"You are on track to study {weekly_hours} hours this week.") #display weekly hours using f-string
try:#error handling if incorrect input value type
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
