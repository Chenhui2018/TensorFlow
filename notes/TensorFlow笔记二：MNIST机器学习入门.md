# TensorFlow笔记二：MNIST机器学习入门

标签（空格分隔）： TensorFlow 深度学习

参考资料
[^2.2MNIST数据下载] 
[^2.3MNIST机器学习入门]

本文是基于“TensorFlow中文社区”[^中文社区]的教程（2.2+2.3）而写的笔记。
本文的目录如下：
> * python程序怎么运行
> * 数据集下载
> * Softmax回归介绍
> * 完整代码

---
## python程序怎么运行
以运行TensorFlow的测试程序为例：
```
import tensorflow as tf
matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.],[2.]])

# 'product' is the multiplication result of 2 matrixs.
product = tf.matmul(matrix1, matrix2)

sess = tf.Session()
print sess.run(product)
```

###方法1 使用了virtualven安装，以语句运行
在命令行（Command Line，简称CMD）输入：
```CMD
source ~/tensorflow/bin/activate #开启 virtualven 的 TensorFlow 空间
python #进入python的CMD界面
依次输入以上例子的所有指令
deactivate #退出 virtualven 的 TensorFlow 空间
```
注意，CMD中，python是和matlab类似的。以语句为单位（回车是一句）运行，
这不方便修改，当代码比较少的时候可以使用。但如果是大量的，就要以文件为单位运行。下面开始介绍：

###方法2 使用virtualven安装，以文件运行
在命令行（Command Line，简称CMD）输入：
```CMD
source ~/tensorflow/bin/activate #开启 virtualven 的 TensorFlow 空间
touch test.py
gedit test.py
在文本中复制以上例子的代码，保存，关闭
python test.py #执行 python 代码
deactivate #退出 virtualven 的 TensorFlow 空间
```
假如你没使用virtualven安装，那就不需要执行“source”和“deactivate”，其余操作相同。

---
## 数据集下载
我试过很多次，在安装路径下，并 ***没有*** “tensorflow/models/image/mnist”
但是，这不代表不可以继续后续的学习。

在教程2.3中，代码：
``` python
import input_data
```
很可能运行失败（你可以使用 ***方式1***  试试），原因是找不到“input_data.py”。
“input_data.py”的路径：
```
~/tensorflow/local/lib/python2.7/site-packages/tensorflow/examples/tutorials/mnist$ 
```
所以为了方便，我们将 ***测试文件*** 新建在此。
这里开始，要给出使用mnist数据集的一段softmax算法的代码，所以推荐使用“以文件为单位运行的程序”。
在命令行（Command Line，简称CMD）输入：
```CMD
source ~/tensorflow/bin/activate #开启 virtualven 的 TensorFlow 空间
touch mnist_test_softmax.py #新建
gedit mnist_test_softmax.py #编辑
```
2.3教程中后续的所有代码，都可以写在这里。

---

## Softmax回归介绍
详细的算法参见其他的说明。

---

## 完整的代码
或者你可以在 codes/mnist_test_softmax.py 找到
```
# MNIST test, softmax

#1 input mnist data

#You need to find the "input_data.py" in your installing path.
#Maybe like "~/tensorflow/lib/python2.7/site-packages/tensorflow/examples/tutorials/mnist"
#Then, you can "import input_data" without error.

import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)


import tensorflow as tf
x = tf.placeholder("float", [None, 784])

W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))


#each computed type in training process
y = tf.nn.softmax(tf.matmul(x,W) + b)

#real type
y_ = tf.placeholder("float", [None,10])

#cross_entropy to measure the accuracy
cross_entropy = -tf.reduce_sum(y_*tf.log(y))

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

init = tf.global_variables_initializer()

#start a session
sess = tf.Session()
sess.run(init)

for i in range(1000):
	batch_xs, batch_ys = mnist.train.next_batch(100)
	sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

#disp
print sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})

```

---
[^中文社区]:http://www.tensorfly.cn/

[^2.2MNIST数据下载]: http://www.tensorfly.cn/tfdoc/tutorials/mnist_download.html

[^2.3MNIST机器学习入门]: http://www.tensorfly.cn/tfdoc/tutorials/mnist_beginners.html




