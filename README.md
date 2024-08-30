
# ShadowMaker

ShadowMaker is a simple tool for creating silhouette images from any input image using a GUI built with PyQt5.

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
