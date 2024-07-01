# Sentinel Imagery Indices Calculator

Welcome to the Indices Calculator for Sentinel Imagery Satellite. This tool is designed to calculate the Normalized Difference Vegetation Index (NDVI) and Soil Adjusted Vegetation Index (SAVI) from Sentinel-2 satellite imagery. The software reads satellite image bands, performs the calculations, and visualizes the results.

## Features

- Calculate NDVI from Sentinel-2 imagery
- Calculate SAVI from Sentinel-2 imagery
- Visualize the indices with a north arrow added to the plots

## Dependencies

This software requires the following Python libraries:

- `numpy` for numerical calculations
- `matplotlib` for visualization
- `rasterio` for reading satellite images

You can install the dependencies using the provided `requirements.txt` file:

```sh
  pip install -r requirements.txt


Usage

    Clone the repository:

```sh
    git clone https://github.com/your-username/sentinel-imagery-indices-calculator.git
    cd sentinel-imagery-indices-calculator

Install the required dependencies:

```sh

    pip install -r requirements.txt

Run the software:

```sh

    python pro_1.py

    Follow the on-screen prompts to provide the directories for the satellite image bands (Red and NIR) and choose the index to calculate (NDVI or SAVI).

Example

An example run of the software:

    Provide the directory for the Red (B04) band:

    mathematica

Provide Band Red (B04) Directory: path/to/red_band.jp2

Provide the directory for the NIR (B08) band:

mathematica

Provide Band NIR (B08) Directory: path/to/nir_band.jp2

Choose the index to calculate (NDVI or SAVI):

vbnet

    What would you like to do with the image (NDVI - SAVI)? Choose (1/2) respectively: 1

The software will then display the calculated index.

Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
Author

Your Name - Your GitHub Profile
Acknowledgments

    Sentinel-2 for providing the satellite imagery
    numpy
    matplotlib
    rasterio
