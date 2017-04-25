import tensorflow as tf

x1 = tf.constant(3)
x2 = tf.constant(9)

res = tf.multiply(x1, x2)
#res = x1 * x2


print(res)

with tf.Session() as ses:
    print(ses.run(res))
