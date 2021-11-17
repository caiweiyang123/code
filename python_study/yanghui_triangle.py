# 方法一：迭代
def triangle_1(x):
    """
    :param x: 需要生成的杨辉三角行数
    :return:
    """
    triangle = [[1], [1, 1]] # 初始化杨辉三角
    n = 3 # 从第三行开始计数,逐行添加
    while n <= x:
        for i in range(0, n-1):
            if i == 0:
                # 添加初始列表[1,1],杨辉三角每行的首位和末位必为1
                triangle.append([1, 1])
            else:
                # 逐位计算，并插入初始列表中
                triangle[n-1].insert(i, triangle[n - 2][i] + triangle[n - 2][i - 1])
        n += 1
    return triangle


x = 15
triangle = triangle_1(x)

# 遍历结果，逐行打印
for i in range(x):
    print(str(triangle[i]).center(200)) # 转为str,居中显示

# 方法二：生成器
def triangle_2(n):
    """
    :param n: 需要生成的杨辉三角行数
    :return:
    """
    triangle = [1] # 初始化杨辉三角
    for i in range(n):
        yield triangle
        triangle.append(0) # 在最后一位加个0，用于计算下一行
        triangle = [triangle[i] + triangle[i - 1] for i in range(len(triangle))]

# 从生成器取值
for i in triangle_2(15):
    print(''.join(str(i)).center(100)) # 格式化输出

# 方法三：递归
def triangle_4(n):
    """
    :param n:需要生成的杨辉三角行数
    :return:
    """
    triangle = [1] # 初始化杨辉三角
    if n == 0:
        return triangle
    return [x+y for x, y in zip([0] + triangle_4(n - 1), triangle_4(n - 1) + [0])]
for i in range(10):
 print(''.join(str(triangle_4(i))).center(100))