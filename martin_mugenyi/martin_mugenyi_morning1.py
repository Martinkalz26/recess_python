# Control flows
"""
# Conditional Statements (if-elif-else)
eg
if gen_gender_sex:
    print('Male')
else:
    print(''Female)
"""

"""
if condition1:
    print('True') # code block is only executed if condition1 is True
elif condition2:
    print('True') # code block is only executed if condition2 is True
else:
    print('False') # code block is only executed if all conditions are False

"""

# Example 1

def age_filter(age):
    if(age < 18):
        print("You are underage")
    elif(age >= 18 and age <= 65):
        print("Your are an adult.")
    else:
        print("Your are a senior citzen.")

age_filter(17)
age_filter(20)
age_filter(75)
# Loops
# (for, while)

"""
for item in sequence:
    loop through the sequence 
    # print(item)
"""
print('------------$$$$$$-------------')
cars = ['Volvo', 'Tesla', 'BMW', 'Jeep', 'Ford', 'Toyota', 'Audi']

for car in cars:
    print(car)
print('------------$$$$$$-------------')

fruits = ['mango', 'pawpaw', 'jack fruit', 'orange']
for fruit in fruits:
    print(fruit)
count = 0
while(count < len(fruits)):
    print(fruits[count])
    count +=1
print('------------$$$$$$-------------')
x = 0
while(x < 6):
    print(x)
    x+=1
print('------------$$$$$$-------------')
# Break and continue statements

# #break
for num in range(1,10):
    if(num == 5):
        break
    print(num)

print('------------$$$$$$-------------')
# # continue
for num in range(1,10):
    if num == 5:
        continue
    print(num)


# Exception handling (try, except, finally)
"""
try block:

except:

finally:
"""

try:
    x = 10/0
except ZeroDivisionError:
    print("Error: Division by Zero") # can't divide by zero
finally:
    print("This is always executed") # complete execution

emotions = {
    'happy': "I'm glad to hear that you're happy",
    'sad': "I'm sorry to hear that you're feeling sad.",
    'angry': "Take a deep breath and try to stay alive.",
    'fearful': "I understand that fear can be challenging.",
    'disgusted': "That's unfortunate to feel disgusted."
}

#prompt the user to enter their emotions
user_emotion = input("How are you feeling today?")

# convert user input  to lowercase
user_emotion = user_emotion.lower()

if user_emotion in emotions:
    print(emotions[user_emotion])
else:
    print("i'm sorry, I don't understand that emotion.")


mental_health_degree = {
    1: "Severe: Requires immediate professional intervention. Individual is unable to function in daily life.",
    2: "Very high: Significant impairment in daily functioning. Professional help is essential.",
    3: "High: Noticeable impact on daily life. Professional assistance is strongly recommended.",
    4: "Moderately high: Some difficulty in fuctioning. Professional support is advisable.",
    5: "Moderate: Experiencing challenges but able to manage daily life with some effort.",
    6: "Moderately low: Mild impact on daily functioniong. Supportive measures may be beneficial.",
    7: "Low: Minimal impact on daily life. Minor support may be helpful",
    8: "Very low: Rarely interferes with daily functioning. Minimal support needed if any.",
    9: "Almost none: Negligible impact on daily life. No support required in most cases.",
    10: "None: No discernable impact on mental health. Individual is functioning optimally."
}

mental_health_rating = int(input("Please rate your mental_health on a scale of 1 - 10: \t"))


try:
    if(mental_health_rating < 1 or mental_health_rating > 10):
        print("Invalid input.")
    else:
         if mental_health_rating in mental_health_degree:
            print(mental_health_degree[mental_health_rating])
         else:
             print("Sorry, but we have nothing to say about your mental health")
     
except Exception as error:
    print("Error: ", error)
finally:
    print("Execution complete.")



