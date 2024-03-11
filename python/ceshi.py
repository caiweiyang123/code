with open("D:\invest_cai_80694\Downloads\labeled_qingxi_clip.txt")as f:
    lines = [line.strip("\n") for line in f]
print(lines)
dict1 = {}
for i in lines:
    if i.split("#")[-1] in dict1:
        dict1[i.split("#")[-1]]+=1
    else:
        dict1[i.split("#")[-1]] = 1
print(dict1)
sum=0
for i in dict1.values():
    sum +=i
print(sum)