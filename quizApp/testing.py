lis = ['nick','jim','kim','wix']


for i in range(len(lis)) :
    exec(f"var{i+1} = lis[{i}]")


print(var1)
print(var2)
