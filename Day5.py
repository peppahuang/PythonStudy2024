# 20241120
# 引用计数
x = 10  # 直接引用
y = x
l = ["a", x]  # 间接引用
print(id(x))
print(id(l[1]))
print(id(y))

x = 123
l = ["0", x]
y = x
print(l[1])
print(y)
x = 123123123
print(l[1])
print(y)
# 列表只是把值的内存放进去了

# 列表存储方式：存的是索引和值的内存地址
# 字典存储方式：散列表

l1 = [
    111,
]

l2 = [
    222,
]
l1.append(l2)
print(l1)
print(22222)
print(id(l1[1]))
print(id(l2))
l2.append(l1)
print(l2)
print(id(l2))
print(id(l1[1]))
print(22222)
print(l1)
del l1
print(l2)
# 哈哈，不要相互引用，会内存泄漏

# 与用户交互
# aa = input("type a word\n")
# input输入的内容都会存储成为str
# print(aa)

# 格式化输出(string)
# 1 %
print("my name is %s, my age is %s" % ("egon", "12"))
res = "str1 %(b)s str2 %(a)s" % {"a": "123", "b": "abc"}
print(res)

# 2 str.format 兼容性好
res = "my name is {1}, my age : {0}".format("peppa", 18)
print(res)
res = "my name is {0}, my age : {1}".format("peppa", 18)
print(res)
res = "my name is {name}, my age : {age}".format(name="peppa", age=18)
print(res)
x = "hello"
y = "world"
res = f"{x}, {y}"
print(res)

txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))

a = 10
b = 0.1
b += 1

print(a + b)

a = 11
b = 20
a, b = b, a
print(a)
print(b)

# 解压赋值
salary = [1, 2, 3, 4, 5]
l1, l2, l3, *_ = salary
print(l1)
print(_)  # 把后面的部分赋值成为了_，但是不要这样命名！
*_, l1, l2, l3 = salary
print(l1)  # 星可以取两头，不可以取中间

# 解压赋值字典，默认拿到的是key
diction = {"a": 123, "b": 234, "c": 3536, "d": 123123}
d1, d2, *_ = diction
print(d1)
print(d2)
print(diction[d1])
