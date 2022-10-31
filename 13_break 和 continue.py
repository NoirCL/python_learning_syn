# Chlorine 
# Time : 2022/10/31 21:32

"""
    1. break用来直接结束整体的当前所在的循环
    2. continue用来结束当次循环
    3. for 和 break都只会影响到当前所在的循环
"""

###
for x in range(5):
    for y in range(11):
        if y == 10:
            break
    print(f"{x} + {y} = {x + y}")

for x in range(5):
    for y in range(11):
        if y == 10:
            continue
        print(f"{x} + {y} = {x + y}")
###
