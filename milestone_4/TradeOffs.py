#TradeOffs

#Input

def find_sum(target, li):
    for i, x in enumerate(li):
        for j, y in enumerate(li):
            if i != j and x+y == target:
                return (i, j)
            else:
                continue
#The complexity is O(n^2)

def find_sum_fast(target, li):
     
    pairs_checked = {}
    for i, num in enumerate(li):
        complement = target - num
        if complement in pairs_checked:
            return (pairs_checked[complement],i)
        pairs_checked[num]=i
#The complexity is O(n)

#Output - a function that will pass the assertion
assert find_sum_fast(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}