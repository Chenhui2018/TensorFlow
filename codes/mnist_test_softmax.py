
# MNIST test, softmax

#1 input mnist data
#You need to find the "input_data.py" in your installing path.
#Maybe like "~/tensorflow2/lib/python2.7/site-packages/tensorflow/examples/tutorials/mnist"
#And "touch test.py" right behind the "input_data.py"
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

#CHANGE
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


