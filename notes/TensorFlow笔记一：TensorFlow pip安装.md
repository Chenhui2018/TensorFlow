# TensorFlow笔记一：TensorFlow pip安装

标签（空格分隔）： TensorFlow 深度学习

参考资料[^1.2下载与安装]

本文是基于“TensorFlow中文社区”[^中文社区]的教程（1.1~1.3）而写的笔记。
本文的目录如下：
> * TensorFlow pip安装
> * 教程文档的修正

---
## TensorFlow pip安装
一切按照教程走，没毛病。
推荐“基于 VirtualEnv 的安装”

***直到，步骤：***
“接下来, 使用类似命令运行 TensorFlow 程序:”
```
(tensorflow)$ cd tensorflow/models/image/mnist
(tensorflow)$ python convolutional.py
```
这里，你会发现安装路径tensorflow下根本就没有models。
所以，忽视它。不会影响你后续的使用，这段测试不必执行。
在后续2的教程中，会继续使用mnist来测试，只要2.3中的例子跑通就行。

至此，安装就结束了。


## 教程文档的修正
安装路径tensorflow下根本就没有models。
所以，这段测试不必执行。
在后续2的教程中，会继续使用mnist来测试，只要2.3中的例子跑通就行。

2.3中的例子，就相当于 TensorFlow 的 hello world.

keep move on, wishes you good luck!

---
[^中文社区]:http://www.tensorfly.cn/

[^1.2下载与安装]: http://www.tensorfly.cn/tfdoc/get_started/os_setup.html





