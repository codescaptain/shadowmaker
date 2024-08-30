import cv2
import numpy as np
import os
from PyQt5.QtWidgets import QMessageBox

def process_image(file_path):
    image = cv2.imread(file_path)

    if image is None:
        QMessageBox.critical(None, "Error", "The image file could not be read!")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    silhouette = np.ones_like(threshold) * 255
    cv2.drawContours(silhouette, contours, -1, (0), thickness=cv2.FILLED)

    file_dir, file_name = os.path.split(file_path)
    file_base, file_ext = os.path.splitext(file_name)
    output_file_name = f"{file_base}_shadow{file_ext}"
    
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_image_path = os.path.join(desktop_path, output_file_name)
    cv2.imwrite(output_image_path, silhouette)

    QMessageBox.information(None, "Completed", f"The silhouette image was successfully saved:\n{output_image_path}")
