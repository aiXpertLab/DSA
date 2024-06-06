import streamlit as st
from utils import st_def

st.set_page_config(page_title='👋 AI',  page_icon="🚀",)
st.title('🔍 AI')
st_def.st_logo()
#------------------------------------------------------------------------------------------------
# https://levelup.gitconnected.com/not-another-python-interview-guide-top-501-problems-to-solve-part-1-24441d435932
num = st.number_input('Q1. Write a Python function to check whether a given number is prime')
num_int = int(num)
yn = 0
prime = "YES"
for div in range(num_int):
    # st.text(yn)
    if num_int/(div+1) == int(num_int/(div+1)): yn = yn + 1
        
    if yn > 2:
        prime = 'NO prime'
        break
st.success(prime)
#------------------------------------------------------------------------------------------------
st.info('2) Write a Python function to find the largest continuous sum in a given list of integers.')
st.info('list1 = [2, 8, 1, 29, 2, -50, 7]')
# list1 = [2, 8, 1, 29,30, 12,13,14,15, 16 -50, 7]
# list1 = [1,2,-5, -7, 8,9,10, 101, 102]
# def max_subarray_sum(arr):
#     max_sum = current_sum = arr[0]
#     for num in arr[1:]:
#         current_sum = max(num, current_sum + num)
#         max_sum = max(max_sum, current_sum)
#     return max_sum

# # Example usage:
# # st.text(max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]))  # Output: 7
# st.text(max_subarray_sum(list))  # Output: 7
#------------------------------------------------------------------------------------------------
st.info('4) What is the purpose of the ‘enumerate’ function in Python? Provide an example.')
st.text('enumerate provides a convenient way to access both the index and the value of items in a list, making it useful for loops where you need both.')
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):  st.write(index, fruit)
    
#------------------------------------------------------------------------------------------------
st.info('5) What is the purpose of the ‘zip’ function in Python? Provide an example.')
st.text('Explanation: zip combines elements from multiple lists into a single iterable of tuples, pairing elements based on their position.')
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    st.write(f"{name} - {age} pair")
#------------------------------------------------------------------------------------------------
st.info('6) What is the purpose of the ‘yield’ keyword in Python? Provide an example.')
st.text('Explanation: yield allows a function to return values one at a time as they are needed, creating a generator that can be iterated over.')
def count_down(num):
    while num > 0:
        yield num
        num -= 1

# Example usage:
for number in count_down(3):st.write(number)

#------------------------------------------------------------------------------------------------
st.info('7) What is the difference between a list comprehension and a generator expression in Python? Provide an example of each.')
squares = [x**2 for x in range(10)]
st.write(squares)

#------------------------------------------------------------------------------------------------
st.info('8) Write a Python function to check whether a given string is a palindrome')
st1 = '123456'
st2 = st1[::-1]    
st.text(f'{st1} {st2}')

#------------------------------------------------------------------------------------------------
st.info('9) Write a Python function to find the second highest number in a list.')
nl = [5, 2, 8, 0, 8]
nlset = set(nl)
mylist = list(nlset)
mylist.sort()
st.write(mylist[-2])

#------------------------------------------------------------------------------------------------
st.info('10) Write a Python function to count the number of vowels in a given string.')
vowelList = list('aeiouAEIOU')

def countVowels(para_str):
    assert isinstance(para_str, str), "Input must be a string"
    newStr = para_str    
    print(newStr)
    for s in vowelList:
        newStr = newStr.replace(s,'')
        
    return (len(para_str) - len(newStr))

def count_vowels(s): return sum(1 for char in s if char.lower() in 'aeiou')

st.write(countVowels('abceasdafsa'))

# https://levelup.gitconnected.com/not-another-python-interview-guide-top-501-problems-to-solve-part-1-24441d435932