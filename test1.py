from echauffement import *


print("===============================================================================================================")
print("Q1.2")
#print(">>> decomposition(-14) \n", decomposition(-14))
assert decomposition(38) == [False, True, True, False, False, True]
assert decomposition(89) == [True, False, False, True, True, False, True]
assert decomposition(956) == [False, False, True, True, True, True, False, True, True, True]
assert decomposition(0) == []
# print("Test decomposition(2) :", decomposition(2))
print("\tTest decomposition(x) : OK\n")

print("===============================================================================================================")
print("Q1.3")
assert completion([False, True, True, False, False, True], 4) == [False, True, True, False]
assert completion([False, True, True, False, False, True], 8) == \
       [False, True, True, False, False, True, False, False]
assert completion([False, True, True, False, False, True], 0) == []
assert completion([], 7) == [False, False, False, False, False, False, False]
print("\tTest completion(l, n) : OK\n")

# qq exemples
print("===============================================================================================================")
print("Q1.4")
assert table(-2, 6) is None
assert table(0, 6) == [False, False, False, False, False, False]
assert table(38, 6) == [False, True, True, False, False, True]
assert table(2114, 12) == \
       [False, True, False, False, False, False, True, False, False, False, False, True]
print("\tTest table(x, n) : OK\n")