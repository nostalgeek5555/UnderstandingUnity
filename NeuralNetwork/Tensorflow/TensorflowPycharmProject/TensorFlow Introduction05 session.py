import tensorflow as tf
import numpy as np

sess = tf.Session()

a = tf.constant(3.0, dtype=tf.float32, name="a")
b = tf.constant(4.0, name="b")
total = tf.add( a, b, name="Add" )
#total = a + b

print(sess.run({'ab':(a, b), 'total':total}))
#7

sess.close()