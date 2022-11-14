test = ["a", "c", "c", "o", "z", "a", "a", "z", "z", "b", "c"]

print("origin", test)

pivot = 0
l, r = pivot + 1, len(test) - 1
while pivot < r:
    while l < r:
        while r > 0 and test[r] == test[pivot]:
            r -= 1
        
        while l < len(test) and test[l] != test[pivot]:
            l += 1
        
        if l < r:
            test[r], test[l] = test[l], test[r]
    
    pivot += 1
    l = pivot + 1

print(pivot, l, r)
print("res", test)
print(test[:l])
