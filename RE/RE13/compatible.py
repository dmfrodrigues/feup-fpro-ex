def compatible(A, B):
    if len(A[0]) != len(B):
        return AssertionError("A and B cannot be multiplied")
    else:
        return "A and B can be multiplied"

print(compatible([[2,2], [1,1]], [[5,5,5,5], [5,5,5,5]]))
print(compatible([[1,2,2], [1,2,2]], [[1,2,3,4], [1,2,3,4]]))