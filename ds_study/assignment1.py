# 1번
def sum_even(input_nums: list[int])->int:
    return sum([num for num in input_nums if num%2==0])

print("Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
print("Output:", sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print("Input: [10, 20, 30, 40, 50]")
print("Output:", sum_even([10, 20, 30, 40, 50]))

print("Input: [9, 7, 5, 3, 1]")
print("Output:", sum_even([9, 7, 5, 3, 1]))    

# 2번
def remove_vowels(input_str: str) -> str:
    vowels = "aeiouAEIOU"
    return "".join(ch for ch in input_str if ch not in vowels)


print('Input: "Hello, World!"')
print('Output:', '"' + remove_vowels("Hello, World!") + '"')

print()

print('Input: "aeiouAEIOU"')
print('Output:', '"' + remove_vowels("aeiouAEIOU") + '"')

print()

print('Input: "zzxxxccvvvbbnnmmmLLKKUHH"')
print('Output:', '"' + remove_vowels("zzxxxccvvvbbnnmmmLLKKUHH") + '"')

# 3번
def get_longest_string(input_strs: list[str]) -> str:
    return max(input_strs, key=len)


print('Input: ["cat", "dog", "bird", "lizard"]')
print('Output: "' + get_longest_string(["cat", "dog", "bird", "lizard"]) + '"')

print()

print('Input: ["cat", "dog", "bird", "wolf"]')
print('Output: "' + get_longest_string(["cat", "dog", "bird", "wolf"]) + '"')

print()

print('Input: ["a", "b", "c", "d"]')
print('Output: "' + get_longest_string(["a", "b", "c", "d"]) + '"')