import numpy as np
import matplotlib.pyplot as plt
import rasterio

def main():
    print("Welcome to the Indices Calculator for Sentinel Imagery Satellite.")
    print("This tool calculates NDVI, SAVI, and NDWI from Sentinel-2 imagery.")

    try:
        if input('Would you like to try the software? (Y/N): ').lower() == 'y':
            option = input('Choose an option: 1. Download your own imagery, 2. Use demo imagery: ').lower()
            if option == "1":
                band_files = []
                required_bands = ["Green (B03)","Red (B04)", "NIR (B08)"]  
                for band in required_bands:
                    directory = input(f'Provide Band {band} Directory: ')
                    band_files.append(directory)
                img = load_image(band_files)
                
                operation = input('What would you like to do with the image (NDVI - SAVI - NDWI - FCC)? Choose (1/2/3/4) respectively: ')
                if operation == "1":
                    plot_index(calculate_ndvi(img), "NDVI")
                elif operation == "2":
                    plot_index(calculate_savi(img), "SAVI")
                elif operation == "3":
                    plot_index(calculate_ndwi(img), "NDWI")
                elif operation == "4":
                    plot_fcc(img)
                else:
                    print("Invalid option.")
            elif option == "2":
                img = load_demo_image()
                operation = input('What would you like to do with the image (NDVI - SAVI - NDWI - FCC)? Choose (1/2/3/4) respectively: ')
                if operation == "1":
                    plot_index(calculate_ndvi(img), "NDVI")
                elif operation == "2":
                    plot_index(calculate_savi(img), "SAVI")
                elif operation == "3":
                    plot_index(calculate_ndwi(img), "NDWI")
                elif operation == "4":
                    plot_fcc(img)
                else:
                    print("Invalid option.")
            else:
                print("Invalid option. Exiting the program.")
        else:
            print("Exiting the program.")
            exit()
    except Exception as e:
        print(f"An error occurred: {e}")



def calculate_ndvi(image):
    """Calculate Normalized Difference Vegetation Index (NDVI)."""
    red = image[:, :, 1]  
    nir = image[:, :, 2]  
    ndvi = (nir - red) / (nir + red)
    return ndvi

def calculate_savi(image, L=0.5):
    """Calculate Soil Adjusted Vegetation Index (SAVI)."""
    red = image[:, :, 1]  
    nir = image[:, :, 2] 
    savi = ((nir - red) / (nir + red + L)) * (1 + L)
    return savi

def calculate_ndwi(image):
    """Calculate Normalized Difference Water Index (NDWI)."""
    green = image[:, :, 0]  
    nir = image[:, :, 2]  
    ndwi = (green - nir) / (green + nir)
    return ndwi

def load_demo_image():
    """Load demo imagery bands and stack them into a single numpy array."""
    band_files = [
                "/media/ajay/main/Harvard's CS50p/final_pro/B03.tif",
                "/media/ajay/main/Harvard's CS50p/final_pro/B04.tif",
                "/media/ajay/main/Harvard's CS50p/final_pro/B08.tif"
    ]
    bands = [rasterio.open(file).read(1) for file in band_files]
    image = np.dstack(bands)
    if not np.issubdtype(image.dtype, np.floating):
        image = image.astype(np.float64)
    return image

def load_image(band_files):
    """Load user-provided bands and stack them into a single numpy array."""
    bands = [rasterio.open(file).read(1) for file in band_files]
    if not np.issubdtype(image.dtype, np.floating):
        image = np.dstack(bands)
    image = image.astype(np.float64)
    return image

def plot_index(index, title):
    """Plot a vegetation index with Matplotlib and add a colorbar."""
    fig, ax = plt.subplots(figsize=(10, 10))
    cax = ax.imshow(index, cmap='RdYlGn') 
    fig.colorbar(cax, ax=ax, orientation='vertical')
    ax.set_title(title)
    plt.show()

def plot_fcc(image):
    """Plot False Color Composite (FCC) image."""
    def normalize(array):
        array_min, array_max = array.min(), array.max()
        return (array - array_min) / (array_max - array_min)

    fcc_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.float32)
    fcc_image[:, :, 0] = normalize(image[:, :, 2])  # NIR band
    fcc_image[:, :, 1] = normalize(image[:, :, 1])  # Red band
    fcc_image[:, :, 2] = normalize(image[:, :, 0])  # Green band

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(fcc_image)
    ax.set_title('False Color Composite (B8, B4, B3)')
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram cancelled by user.")
