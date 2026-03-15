# 1번 
def filter_even_length_string(input_strs: list[str]) -> list[str]:
    
    result=[]
    
    for s in input_strs:
        if len(s) % 2==0:
            result.append(s)
            
    return result
       
input1 = ["cat", "dog", "fish", "elephant"]
print("Input:", input1)
print("Output:", filter_even_length_string(input1))

input2 = ["q", "w", "e", "r", "t", "y"]
print("Input:", input2)
print("Output:", filter_even_length_string(input2))

input3 = ["qq", "ww", "ee", "rr", "tt", "yy"]
print("Input:", input3)
print("Output:", filter_even_length_string(input3))

# 2번
def reverse_elements(input_nums: list[int]) -> list[int]:
    
    result = []
    
    for i in range(len(input_nums)-1, -1, -1):
        result.append(input_nums[i])
        
    return result
    
input1 = [1, 2, 3, 4, 5]
print("Input:", input1)
print("Output:", reverse_elements(input1))

input2 = []
print("Input:", input2)
print("Output:", reverse_elements(input2))

input3 = [20, 15, 25, 10, 30, 5, 0]
print("Input:", input3)
print("Output:", reverse_elements(input3))

# 3번
def filter_type_str(input_list: list[str | int]) -> list[str]:
    result = []

    for item in input_list:
        if isinstance(item, str):
            result.append(item)

    return result


input1 = ["hello", 1, 2, "www"]
print("Input:", input1)
print("Output:", filter_type_str(input1))

input2 = []
print("Input:", input2)
print("Output:", filter_type_str(input2))

input3 = [1, 2, 3, 4, 5]
print("Input:", input3)
print("Output:", filter_type_str(input3))