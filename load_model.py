import tensorflow as tf

model = tf.keras.models.load_model('mnist_ann_model.h5')
print(model)