first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(elem) for elem in first_strings if len(elem) > 5]
print(first_result)
second_result = [(first_elem, second_elem) for first_elem in first_strings for second_elem in second_strings if len(first_elem)==len(second_elem)]
print(second_result)
third_result = [{string: len(string)} for string in first_strings+second_strings if len(string)%2 == 0]
print(third_result)