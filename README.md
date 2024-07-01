# Sentinel Imagery Indices Calculator

Welcome to the Sentinel Imagery Indices Calculator! This tool is designed to calculate key vegetation indices from Sentinel-2 satellite imagery. It supports the Normalized Difference Vegetation Index (NDVI), Soil Adjusted Vegetation Index (SAVI), and Normalized Difference Water Index (NDWI). The tool reads satellite image bands, performs the calculations, and provides visualizations of the results.

## Features

- Calculate NDVI from Sentinel-2 satellite imagery
- Calculate SAVI from Sentinel-2 satellite imagery
- Calculate NDWI from Sentinel-2 satellite imagery
- Visualize the calculated indices with a colorbar for reference

## Dependencies

This software relies on the following Python libraries, which can be installed using `pip` and the provided `requirements.txt` file:

- `numpy` for efficient numerical operations
- `matplotlib` for visualizing the calculated indices
- `rasterio` for reading and manipulating satellite image data

To install the dependencies, use the command:

```bash
pip install -r requirements.txt
```

## Usage

### Installation

Clone the repository and navigate into it:

git clone https://github.com/ajay098patro/sentinel-imagery-indices-calculator.git
cd sentinel-imagery-indices-calculator

Install the required Python libraries:

```pip install -r requirements.txt```

### Running the Software

To run the software, execute the following command:

python pro_1.py

Follow the on-screen prompts to provide the directories for the satellite image bands (Red and NIR) and choose the index to calculate (NDVI or SAVI).

### Example

Here's an example run of the software:

1. Provide the directory for the Red (B04) band:
   Provide Band Red (B04) Directory: path/to/red_band.jp2

2. Provide the directory for the NIR (B08) band:
   Provide Band NIR (B08) Directory: path/to/nir_band.jp2

The software will display the calculated index with a range scale on the plot.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## Author

 Ajay Kumar Patro - ajay098patro

## Acknowledgments

- **Sentinel-2**: Providing the satellite imagery used in this project
- **numpy**: Efficient numerical operations in Python
- **matplotlib**: Visualization library for Python
- **rasterio**: Python library for reading and writing raster data formats
