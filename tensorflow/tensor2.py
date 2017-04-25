'''
programa entrenado para reconocer digitos escritos a mano
'''

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#one hot en tabla booleana

#numero dee nodos para cada layer de red neuronal
n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

#numero de clases resultados
n_clases = 10

#tamanio de batch para ver cuantas lee a la vez
batch_size = 100

# alto por ancho para convertir imagenes en arreglo unidimensional 28x28 = 784
x = tf.placeholder('float',[None,784])
y = tf.placeholder('float')

def neural_network_model(data):

    hidden_1_layer = {'weights':tf.Variable(tf.random_normal([784, n_nodes_hl1])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))}

    hidden_2_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl2]))}

    hidden_3_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl3, n_nodes_hl3])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl3]))}

    output_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl3, n_clases])),
                      'biases':tf.Variable(tf.random_normal([n_clases]))}

    layer1 =  tf.add(tf.matmul(data, hidden_1_layer['weights']) , hidden_1_layer['biases'])
    layer1 = tf.nn.relu(layer1)

    layer2 =  tf.add(tf.matmul(layer1, hidden_2_layer['weights']) , hidden_2_layer['biases'])
    layer2 = tf.nn.relu(layer2)

    layer3 =  tf.add(tf.matmul(layer2, hidden_3_layer['weights']) , hidden_3_layer['biases'])
    layer3 = tf.nn.relu(layer3)

    salida =  tf.matmul(layer3, output_layer['weights']) + output_layer['biases']

    return salida


def train_nnetwork(x):
    prediction = neural_network_model(x)
    cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))
    #optimizador integrado a tensorflow
    optimizador = tf.train.AdamOptimizer().minimize(cost)
    #ciclos de retoalimentacio
    hm_epochs = 15

    with tf.Session() as ses:
        ses.run(tf.global_variables_initializer())

        for epoch in range(hm_epochs):
            epoch_loss = 0

            for _ in range(int(10000/batch_size)):
                ep_x,ep_y = mnist.train.next_batch(batch_size)
                _,c = ses.run([optimizador, cost], feed_dict={x: ep_x, y:ep_y})
                epoch_loss += c

            print("Epoch ", epoch, " completado de ", hm_epochs, " perdida = ",epoch_loss)

        correct = tf.equal(tf.argmax(prediction,1), tf.argmax(y,1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))

        print("Precision = ", accuracy.eval({x:mnist.test.images, y:mnist.test.labels}))

train_nnetwork(x)
