# 20241120
# 变量
a = 10086
print(a)
print(id(a))
print(type(a))

# is ==
# is：身份是否相等
# ==：比较左右两个值是否相等
a = "age"
b = a
c = "age"
d = "info: egon : 18"
e = "info: egon : 18"
print(id(d))
print(id(e))
print(a == b)
print(a is b)
print(a == c)
print(a is c)

x = -5
y = -5
print(x is y)
x = -6
y = -6
print(x is y)
# 最后的结果和解释器的优化有关系可能是true也可能是false

# 变量：驼峰或者全小写加杠
# 常量：全大写加杠

# 基本数据类型
# 1 数字
a = 1
b = 1.0
print(type(a))
print(type(b))
print(a == b)
print(a is b)

c = 10
d = 2.0
e = c / d
f = 5
print(type(e))
print(e == f)
print(e is f)

# 2 字符串
# 双引号可以包含在单引号里面
str1 = 'print "hello world"'
print(str1)
str2 = "It's a beautiful day!"
str2 = """This is another example
of a multi-line string."""  # multi-line
print(str2)

str3 = 'It\'s a "beautiful" day!'  # 使用转义符
str4 = 'It\'s a "beautiful" day!'  # 另一种方式
print(str3)
print(str4)

str5 = "*"
print(str5 * 5)
print(str5 + "5")

# 3 列表，索引从0开始
l = [100, 2, "3", "dfosif"]
print(l)

# 4 字典
dic = {"a": 111, "b": 222, "c": 333}
print(type(dic))
print(dic["a"])

# bool
is_ok = True
is_no = False
