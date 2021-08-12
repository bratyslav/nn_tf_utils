import tensorflow as tf


def to_tflite_gpu(model, save_path_name):
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    converter.target_spec.supported_ops = [tf.float16]
    tflite_quant_model = converter.convert()

    with open(save_path_name, 'wb') as f:
        f.write(tflite_quant_model)
