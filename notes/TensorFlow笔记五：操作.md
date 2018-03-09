# TensorFlow笔记五：操作

标签（空格分隔）：TensorFlow

参考[^专栏文章]


---
##1 constants 常量
```
#1
a = tf.constant(5)
a = tf.constant([2,2], name='a')
b = tf.constant([[0,1],[2,3]], name='b')

#if you want to diplay, do as I do in the command line of python.
a = tf.constant(5)
sess = tf.Session()
print sess.run(a)

>>>[2 2] # This is the output result.
```
---
##1.1 special constant value
```
#1 zeros SEE #3
tf.zeros()

#2 zeros_like SEE #4
b = tf.constant([[0,1],[2,3]], name='b')
x = tf.zeros_like(b)
>>>
[[1. 1.]
 [1. 1.]]
 
#3 ones
tf.ones([3,2], name='a')
>>> 
[[1. 1.]
 [1. 1.]
 [1. 1.]]

#4 ones_like
b = tf.constant([[0,1],[2,3]], name='b')
x = tf.ones_like(b)
>>>
[[1. 1.]
 [1. 1.]]

#5 fill
tf.fill([2, 3], 8)
>> [[8, 8, 8], [8, 8, 8]]

#6 linspace
tf.linspace(10.0, 13.0, 4)
>>> [10.0, 11.0, 12.0, 13.0]

#7 range
tf.range(3, limit=18, delta=3)
>> [3, 6, 9, 12, 15]
```
---
##1.2 random
```
#1 random_normal
tf.random_normal()
a = tf.Variable(tf.random_normal([2,2],seed=1))
>>>
[[-0.81131822  1.48459876]
 [ 0.06532937 -2.44270396]]

tf.truncated_normal()
tf.random_uniform()
tf.random_shuffle()
tf.random_crop()
tf.muiltinomial()
tf.random_gamma()
```
---
##2 variables
```
a = tf.Variable(2, name='scalar')
b = tf.Variable([2, 3], name='vector')
```
在使用变量之前必须对其进行初始化
```
# 全部初始化
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

# 部分初始化
init_ab = tf.variable_initializer([a, b], name='init_ab')
with tf.Session() as sess:
    sess.run(init_ab)

# 一个变量初始化
w = tf.Variable(tf.zeros([784, 10]))
with tf.Session() as sess:
    sess.run(w.initializer)
    
w.initializer # 初始化
```
##2.1 variable operation
```
# Get result:
w = tf.Variable(tf.truncated_normal([10, 10], name='normal'))
with tf.Session() as sess:
    sess.run(w.initializer)
    print(w.eval()) # way 1
    print(sess.run(w)) # way 2 common,better
    
# 赋值
x.assign() # 分配值给这个变量
# Compare P1 & P2

# P1
w = tf.Variable(10)
w.assign(100)
with tf.Session() as sess:
    sess.run(w.initializer)
    print(w.eval())
>> 10

# P2
w = tf.Variable(10)
assign_op = w.assign(100)
with tf.Session() as sess:
    sess.run(w.initializer)
    sess.run(assign_op) # do assgin
    print(w.eval())
>> 100
```
##2.2 Session 是函数式编程
```
x = assign() 
x = assign_add()
x = assign_sub()

W = tf.Variable(10)
sess1 = tf.Session() # seperately
sess2 = tf.Session()
sess1.run(W.initializer)
sess2.run(W.initializer)
print(sess1.run(W.assign_add(10))) # >> 20
print(sess2.run(W.assign_sub(2))) # >> 8
print(sess1.run(W.assign_add(100))) # >> 120
print(sess2.run(W.assign_sub(50))) # >> -42
sess1.close()
sess2.close()
```
---
##3 placeholder 占位符
```
tf.placeholder() 

#normal process of tensorflow: 1 define graphs, 2 compute graphs;
a = tf.placeholder(tf.float32, shape=[3])
b = tf.constant([5, 5, 5], tf.float32)
c = a + b
with tf.Session() as sess:
    print(sess.run(c, feed_dict={a: [1, 2, 3]}))
	# 'feed_dict' acts like the input parameters of function 'c';
```
---

##4 lazy loading (should AVOID)
May causing low speed of loading speed. 
```
# GOOD
# normal loading
x = tf.Variable(10, name='x')
y = tf.Variable(20, name='y')
z = tf.add(x, y)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for _ in range(10):
        sess.run(z)

# BAD
# lazy loading
x = tf.Variable(10, name='x')
y = tf.Variable(20, name='y')
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for _ in range(10):
        sess.run(tf.add(x, y))
```

---
##5 operaton
```
c = tf.add(a, b)
c = tf.multiply(a,b,name='dot_production')
```
---
##6 excution
```
with tf.Session() as sess:
	print(sess.run())
```
---
##tensorflow board

```
#in terminal:

tensorflowboard --logdir="PATH_TO_LOG_DATA"
http://localhost:6006/ # open with chrome
```
---

[^专栏文章]: https://zhuanlan.zhihu.com/p/28488510





