import tensorflow as tf

# Load the image
image_path = "COCO.png"  # Assuming the image is in JPEG format
image_raw = tf.io.read_file(image_path)

# Decode the image
image = tf.image.decode_jpeg(image_raw)

# Print image info (optional)
print(image.shape)
print(image.dtype)

# Resize the image to a specific size, e.g., 224x224
image_resized = tf.image.resize(image, [224, 224])

# Normalize pixel values to the range [0, 1]
image_normalized = image_resized / 255.0

# Load a pre-trained model, e.g., MobileNetV2
model = tf.keras.applications.MobileNetV2(weights='imagenet', input_shape=(224, 224, 3))

# Ensure the image has the correct shape (1, 224, 224, 3)
image_batch = tf.expand_dims(image_normalized, 0)

# Make predictions
predictions = model.predict(image_batch)

# Decode the predictions
decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=5)
for i, (imagenet_id, label, score) in enumerate(decoded_predictions[0]):
    print(f"{i + 1}: {label} ({score:.2f})")
