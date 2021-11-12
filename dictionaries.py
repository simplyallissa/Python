students = {} #initialize empty dictionary
students = dict() #initialize empty dictionary

students = {
    "Bob": 34345,
    "Charly": 45345
}

students['Dan'] = 234356
print(list(students.keys()))
print(list(student.values()))

student_ids = {123, 1232, 23423} # set, not dictionary
student_ids = set() # initialize an empty set

1 = [1,1,2,2,2,2,2,]
print(set(1)) # prints {1, 2} This is a use-case for sets

# Tuples are used to store multimple items in a single variable.
# A collection that is ordered and immutable

this_is_a_tuple = ("apple", "banana", "cherry") # use it if you don't want it to be modified


# Raw, expose memory buffer

bt = bytes(b"Byte string")
memv = memoryview(bt)
