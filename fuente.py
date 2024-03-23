# fuente.py
import tensorflow as tf

def procesar_y_predecir_imagen(image_path="COCO.png"):
    try:
        image_raw = tf.io.read_file(image_path)
        image = tf.image.decode_jpeg(image_raw)
        print(image.shape)
        print(image.dtype)

        image_resized = tf.image.resize(image, [224, 224])
        image_normalized = image_resized / 255.0

        model = tf.keras.applications.MobileNetV2(weights='imagenet', input_shape=(224, 224, 3))
        image_batch = tf.expand_dims(image_normalized, 0)

        predictions = model.predict(image_batch)
        decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=5)
        for i, (imagenet_id, label, score) in enumerate(decoded_predictions[0]):
            print(f"{i + 1}: {label} ({score:.2f})")
    except tf.errors.NotFoundError:
        print(f"El archivo {image_path} no existe.")
        return False

    return True
