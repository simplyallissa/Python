temp = 75
if temp < 40:
    print("Cold")

x = True
y = False

# Boolean expressions use relational operands: <, >, =<, =>

temp = 75
if temp < 40:
    print("Cold")

else:
    print("Not cold")

# Multiway decision pattern

if temp < 40:
    print("Cold")

elif 40 < temp < 72:
    print("Normal")

else:
    print("Hot")
    
# = is assignment vs == is used to check equality 
a = 3

if a == 2:
    print("is two")
    
if __name__ == '__main__':
    main()
