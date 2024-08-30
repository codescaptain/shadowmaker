import unittest
import os
from shadowmaker.image_processor import process_image

class TestImageProcessor(unittest.TestCase):

    def test_image_processing(self):
        # Provide a path to a test image
        test_image_path = "tests/test_image.jpg"
        process_image(test_image_path)
        output_image_path = os.path.join(os.path.expanduser("~"), "Desktop", "test_image_shadow.jpg")
        self.assertTrue(os.path.exists(output_image_path))

if __name__ == '__main__':
    unittest.main()
