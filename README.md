
# ShadowMaker

ShadowMaker is a simple tool for creating silhouette images from any input image using a GUI built with PyQt5.
<img width="432" alt="Screenshot 2024-08-29 at 23 14 44" src="https://github.com/user-attachments/assets/59767920-93fa-4622-a79f-bd47649a0ba4">
<img width="369" alt="Screenshot 2024-08-29 at 23 14 31" src="https://github.com/user-attachments/assets/8896019f-c4b4-4e31-b353-902890fcbae9">


![Example 1](https://github.com/user-attachments/assets/1e92d192-c2b1-449b-9337-ddafd6023d8f)
![Example 2](https://github.com/user-attachments/assets/f5b061a1-98c8-4bab-83dc-cbf75fbc0a10)



## Installation

To get started with ShadowMaker, follow the steps below:

### Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/shadowmaker.git
cd shadowmaker
```

### Install Dependencies
Install the required dependencies listed in the `setup.py` file:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application
To run the GUI application, execute the following command in your terminal:

```bash
python -m shadowmaker.gui
```

### How It Works
1. **Select an Image**: Use the GUI to select an image file.
2. **Process the Image**: The tool will create a silhouette version of the image by converting the selected image to a grayscale version and applying contour detection.
3. **Save the Output**: The processed image will be saved to your desktop with "_shadow" appended to the original file name.

## Running Tests

To run tests and ensure everything is working as expected, you can use:

```bash
python -m unittest discover tests
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contribution

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any improvements or bugs you find.

## Author
- Ahmet Kaptan(@codescaptain)

**Your Name**  
[GitHub Profile](https://github.com/codescaptain)
