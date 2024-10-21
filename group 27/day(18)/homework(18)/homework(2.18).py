#1)
num_list=[1,2,3,5,6]
if max(num_list)-num_list[3]>max(num_list)-num_list[2] and max(num_list)-num_list[3]>max(num_list)-num_list[1] and max(num_list)-num_list[3] > max(num_list)-num_list[0]:
    print(num_list[3])
elif max(num_list)-num_list[2]>max(num_list)-num_list[3] and max(num_list)-num_list[2]>max(num_list)-num_list[1] and max(num_list)-num_list[2] > max(num_list)-num_list[0]:
    print(num_list[2])
elif max(num_list)-num_list[1]>max(num_list)-num_list[3] and max(num_list)-num_list[1]>max(num_list)-num_list[2] and max(num_list)-num_list[1] > max(num_list)-num_list[0]:
    print(num_list[1])
elif max(num_list)-num_list[0]>max(num_list)-num_list[3] and max(num_list)-num_list[0]>max(num_list)-num_list[2] and max(num_list)-num_list[0] > max(num_list)-num_list[1]:
    print(num_list[0])
else:
    print("error")

#2)
num_list=[1,2,3,5,6]
if min(num_list)+num_list[4]>min(num_list)+num_list[2] and min(num_list)+num_list[4]>min(num_list)+num_list[1] and min(num_list)+num_list[4] > min(num_list)+num_list[0]:
    print(num_list[4])
elif min(num_list)+num_list[3]>min(num_list)+num_list[2] and min(num_list)+num_list[3]>min(num_list)+num_list[1] and min(num_list)+num_list[3] > min(num_list)+num_list[0]:
    print(num_list[3])
elif min(num_list)+num_list[2]>min(num_list)+num_list[3] and min(num_list)+num_list[2]>min(num_list)+num_list[1] and min(num_list)+num_list[2] > min(num_list)+num_list[0]:
    print(num_list[2])
elif min(num_list)+num_list[1]>min(num_list)+num_list[3] and min(num_list)+num_list[1]>min(num_list)+num_list[2] and min(num_list)+num_list[1] > min(num_list)+num_list[0]:
    print(num_list[1])
elif min(num_list)+num_list[0]>min(num_list)+num_list[3] and min(num_list)+num_list[0]>min(num_list)+num_list[2] and min(num_list)+num_list[0] > min(num_list)+num_list[1]:
    print(num_list[0])
else:
    print("error")
#3)
number_list=[11,2,15,4,10,6]
print(number_list.index(11))
print(number_list.index(15))
print(number_list.index(10))
#4)
#5)
#6)
#7)
#8)

#9)
strings=['nika','xato','mari','shorena','aleqsandre']
numbers=[16,16,15,44,78]
print(sum(numbers))
combined_strings=" ".join(strings)
print(combined_strings)

#10)
element_lists=[0,1,2,3,4,5,6,7,8,9,10]
element_lists2=[]
element_lists2=element_lists[0]+2,element_lists[2]+2,element_lists[4]+2,element_lists[6]+2,element_lists[8]+2
print(element_lists2)


