import numpy as np
from project import calculate_ndvi, calculate_savi, calculate_ndwi

def test_calculate_ndvi():
    # Create a 6x6 sample image with synthetic data for three bands: red, NIR, and green
    image = np.zeros((6, 6, 3))
    image[:, :, 0] = np.linspace(0, 225, num=36).reshape(6, 6)  # Red band
    image[:, :, 1] = np.linspace(225, 0, num=36).reshape(6, 6)  # NIR band
    image[:, :, 2] = np.linspace(112, 337, num=36).reshape(6, 6)  # Green band

    red = image[:, :, 0]
    nir = image[:, :, 1]
    expected_ndvi = (nir - red) / (nir + red)
    np.testing.assert_array_almost_equal(calculate_ndvi(image), expected_ndvi)
    print("NDVI test passed.")

def test_calculate_savi():
    # Create a 6x6 sample image with synthetic data for three bands: red, NIR, and green
    image = np.zeros((6, 6, 3))
    image[:, :, 0] = np.linspace(0, 225, num=36).reshape(6, 6)  # Red band
    image[:, :, 1] = np.linspace(225, 0, num=36).reshape(6, 6)  # NIR band
    image[:, :, 2] = np.linspace(112, 337, num=36).reshape(6, 6)  # Green band

    red = image[:, :, 0]
    nir = image[:, :, 1]
    L = 0.5
    expected_savi = ((nir - red) / (nir + red + L)) * (1 + L)
    np.testing.assert_array_almost_equal(calculate_savi(image, L), expected_savi)
    print("SAVI test passed.")

def test_calculate_ndwi():
    # Create a subset of synthetic data (100x100) for two bands: green and NIR
    subset_size = 100
    image = np.zeros((subset_size, subset_size, 2))
    image[:, :, 0] = np.linspace(112, 337, num=subset_size*subset_size).reshape(subset_size, subset_size)  # Green band
    image[:, :, 1] = np.linspace(225, 0, num=subset_size*subset_size).reshape(subset_size, subset_size)  # NIR band
    
    green = image[:, :, 0]
    nir = image[:, :, 1]
    expected_ndwi = (green - nir) / (green + nir)
    
    # Assert the calculated NDWI against the expected NDWI with a tolerance level
    np.testing.assert_array_almost_equal(calculate_ndwi(image), expected_ndwi, decimal=4)
    print("Large NDWI test passed.")
    
if __name__ == '__main__':
    test_calculate_ndvi()
    test_calculate_savi()
    test_calculate_ndwi()
