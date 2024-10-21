#1)
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    
    return numbers[0] + numbers[1]
#2)
def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    
    copy_numbers = numbers.copy()
    min_number = min(numbers)
    copy_numbers.remove(min_number)
    
    return copy_numbers
#3)
def stray(arr):
    for num in arr:
        if arr.count(num) == 1:
            return num
   