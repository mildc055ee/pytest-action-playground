import pytest
import tensorflow as tf


@pytest.fixture(scope="session")
def fashion_mnist():
    return tf.keras.datasets.fashion_mnist.load_data()
