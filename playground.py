import tensorflow as tf

my_tensor = tf.zeros([5, 5, 5, 5])

my_tensor = tf.reshape(my_tensor, [25, 25])
print(my_tensor)
