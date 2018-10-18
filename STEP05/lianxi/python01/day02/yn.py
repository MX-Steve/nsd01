# while True:
#     yn = input("Continue?(y/n)")
#     if yn in ['n','N']:
#         break
#     print("working...")

# while True:
#     xxx
# else:
#     xxx

result = 0
counter = 0

while counter < 101:
    counter += 1
    if counter %2:
        continue
    else:
        result +=counter

print(result)
