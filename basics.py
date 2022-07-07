#Exercises

#counter
my_list = [1,2,3,4,5,6,7,8,9]

counter = 0
for num in my_list:
    counter += num

print(counter)

#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for row in picture:
    for item in row:
        if (item == 1):
            print('*', end='') #end with empty string keeps the new line from occuring
        else:
            print(' ', end='')
    print('') #adds new line after each row


#check for duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

res = []

for letter in some_list:
    if (some_list.count(letter) > 1):
        if letter not in res:
            res.append(letter)

print(res)