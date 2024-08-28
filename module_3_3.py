# 1
print("=" * 30)
print("Task: 1" + "\n")
def print_params(a = 1, b = "string", c = True):
    print(a, b, c)
    return(a, b, c)

print_params(1, 2, 3)
print_params(4, 5)
print_params()
print_params(b = 25) 
print_params(c = [1,2,3])
print()

# 2
print("=" * 30)
print("Task: 2" + "\n")
value_list = ["stroka", 45, [1,2,3]]
#print(value_list)
value_dict = {"a":9, "b":8, "c":7}

print_params(*value_list)
print_params(**value_dict)
print()

#3
print("=" * 30)
print("Task: 3" + "\n")
value_list2 = ["Text", False]
print_params(*value_list2, 42)
print()
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
