dogs = ["jack", "chrissy"]
people = ["michael", "matthew", "anton", "aayushi", "molly", "sparks", "justin"]
test_scores = [93, 99, 91, 75]

print("Initial values: ")
print(dogs)
print(people)
print(test_scores)

# change the lists so that...
# dogs = ["jack", "chrissy", "pixel", "byte"]
# people = ["matthew", "aayushi", "molly", "sparks"]
# test_scores = [93]





# now let's check!

if dogs == ["jack", "chrissy", "pixel", "byte"]:
    print('list 1: success!')
else:
    print('FAILED list 1 test')


if people == ["matthew", "aayushi", "molly", "sparks"]:
    print('list 2: success!')
else:
    print('FAILED list 2 test')


if test_scores == [93]:
    print('list 3: success!')
else:
    print('FAILED list 3 test')
