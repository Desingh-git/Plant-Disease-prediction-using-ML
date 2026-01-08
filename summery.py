import tensorflow as tf
model = tf.keras.models.load_model('models/plant.h5')
model.summary()
