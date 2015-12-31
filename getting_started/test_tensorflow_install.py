import tensorflow as tf

def test_hello_tensorflow():

    # Define 'hello' constant
    hello = tf.constant('Hello, TensorFlow!')

    # Create tensorflow session
    sess = tf.Session()

    # Test tensorflow
    assert sess.run(hello) == 'Hello, TensorFlow!'

    # Close session
    sess.close()
    
