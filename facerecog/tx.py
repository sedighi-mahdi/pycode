import tensorflow as tf
import numpy as np

def tf_descent(X_tf, d_tf, mu, N_epochs):
    N = X_tf.get_shape().as_list()[0]
    f = 2 / N

    w = tf.Variable(tf.zeros((2, 1)), name="w_tf")
    y = tf.matmul(X_tf, w, name="y_tf")
    e = y - d_tf
    grad = f * tf.matmul(tf.transpose(X_tf), e)

    training_op = tf.assign(w, w - mu * grad)
    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        init.run()
        for epoch in range(N_epochs):
            sess.run(training_op)
        opt = w.eval()
    return opt

np.random.seed(444)

N = 10000
sigma = 0.1
noise = sigma * np.random.randn(N)
x = np.linspace(0, 2, N)
d = 3 + 2 * x + noise
d.shape = (N, 1)

# We need to prepend a column vector of 1s to `x`.
X = np.column_stack((np.ones(N, dtype=x.dtype), x))
print(X.shape)


X_tf = tf.constant(X, dtype=tf.float32, name="X_tf")
d_tf = tf.constant(d, dtype=tf.float32, name="d_tf")

mu = 0.001
N_epochs = 10000

tf_w = tf_descent(X_tf, d_tf, mu, N_epochs)
print(tf_w)