def calculate_structure_sum(*args):
    calc = 0
    for i in args:
        if isinstance(i, (int, float)):
            calc += i
        elif isinstance(i, str):
            calc += len(i)
        elif isinstance(i, dict):
            calc += calculate_structure_sum(*i.items())
        elif isinstance(i, (list, tuple, set)):
            calc += calculate_structure_sum(*i)
    return calc


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)