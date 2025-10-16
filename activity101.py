set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
symmetric_diff = set1.symmetric_difference(set2)
print("Symmetric Difference using method:", symmetric_diff)
symmetric_diff_operator = set1 ^ set2
print("Symmetric Difference using '^' operator:", symmetric_diff_operator)
