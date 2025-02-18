#type casting
num1 = 1
num2 = 2
word = "The sum of "
sum = num1 + num2

print(word + str(num1) + " and " +str(num2) + " is " + str(sum))

#another way of calling the variables
print(f"{word}{num1} and {num2} is {sum}") #this is the new way of calling variables
print("%s %d and %d is %d" % (word, num1, num2, sum)) #this is the old way of calling variables