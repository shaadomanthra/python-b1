# # Conditional Statments

a,b = 20,20
# if, else, elif

if(a>b):
    message = "A is greater than B"
elif(a==b):
    message = "A is same as B"
else:
    message = "A is less than B"

print(message)

a = 20
b = 30
# single line code
message = "A is less than B" if(a<b) else "A is greater than B"
print(message)