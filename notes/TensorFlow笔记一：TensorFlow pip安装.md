# TensorFlow笔记一：TensorFlow pip安装

标签（空格分隔）： TensorFlow 深度学习

参考资料[^1.2下载与安装]

本文是基于“TensorFlow中文社区”[^中文社区]的教程（1.1~1.3）而写的笔记。
本文的目录如下：
> * 墙内用户之殇及其解决办法
> * TensorFlow pip安装
> * 教程文档的修正

---
## 墙内用户之殇及其解决办法

安装好ubuntu16，假如已经换了 **软件源** 和 **pip源** 的兄弟姐妹，忽略本节。

已经可以访问外网的，也可以忽略。但是亲测，国内源会更快一点。其实都是看网速。


因为，墙之弥高，所以，换源。


**###1 换软件源**

ui界面操作[^换源]

System setting -> Software & update -> Download from -> Othre... -> China -> https://mirror.tuna.tsinghua.edu.cn/ubuntu （清华的）


**###2 换pip源**

这部应该在安装pip（python-pip）之后进行，先写在这里。

在用户目录下（也就是Desk,Download,Pictures...所在），CMD内，新建.pip

```
mkdir .pip # 这是一个隐藏目录
cd .pip 
touch pip.config
gedit pip.config
```

输入

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

OK。

---
## TensorFlow pip安装
一切按照教程走，没毛病。
推荐“基于 VirtualEnv 的安装”

"在 virtualenv 内, 安装 TensorFlow:"
```
(tensorflow)$ pip install --upgrade <$url_to_binary.whl>
```
命令修改如下：[^tensorflow清华包]
```
pip install \
  -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
  https://mirrors.tuna.tsinghua.edu.cn/tensorflow/linux/cpu/tensorflow-1.6.0-cp27-none-linux_x86_64.whl
```


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

[^换源]: https://www.linuxidc.com/Linux/2014-04/100476.htm

[^tensorflow清华包]: https://mirrors.tuna.tsinghua.edu.cn/help/tensorflow/


