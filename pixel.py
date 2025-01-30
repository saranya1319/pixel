import cv2
import numpy as np


def encrypt_image(image_path, key):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("Image not found or unable to read.")

    np.random.seed(key)  # Use key for deterministic shuffling
    indices = np.random.permutation(image.size // 3)
    reshaped_image = image.reshape(-1, 3)
    encrypted_image = reshaped_image[indices].reshape(image.shape)

    encrypted_path = "encrypted_image.png"
    cv2.imwrite(encrypted_path, encrypted_image)
    return encrypted_path


def decrypt_image(encrypted_path, key):
    encrypted_image = cv2.imread(encrypted_path, cv2.IMREAD_COLOR)
    if encrypted_image is None:
        raise ValueError("Encrypted image not found or unable to read.")

    np.random.seed(key)
    indices = np.random.permutation(encrypted_image.size // 3)
    reshaped_image = encrypted_image.reshape(-1, 3)
    decrypted_image = np.zeros_like(reshaped_image)
    decrypted_image[indices] = reshaped_image

    decrypted_path = "decrypted_image.png"
    cv2.imwrite(decrypted_path, decrypted_image.reshape(encrypted_image.shape))
    return decrypted_path


# Example usage
if __name__ == "__main__":
    key = 42  # Use a fixed key for reproducibility
    image_path = r"C:\Users\SARANYA\Pictures\Saved Pictures\paintings.png"

    encrypted_path = encrypt_image(image_path, key)
    decrypted_path = decrypt_image(encrypted_path, key)
    print(f"Encrypted image saved at: {encrypted_path}")
    print(f"Decrypted image saved at: {decrypted_path}")
