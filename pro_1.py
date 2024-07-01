import numpy as np
import matplotlib.pyplot as plt
import rasterio

def calculate_ndvi(image):
    """Calculate Normalized Difference Vegetation Index (NDVI)."""
    red = image[:, :, 0]  
    nir = image[:, :, 1]  
    ndvi = (nir - red) / (nir + red)
    return ndvi

def calculate_savi(image, L=0.5):
    """Calculate Soil Adjusted Vegetation Index (SAVI)."""
    red = image[:, :, 0]  
    nir = image[:, :, 1] 
    savi = ((nir - red) / (nir + red + L)) * (1 + L)
    return savi

def calculate_ndwi(image):
    """Calculate Normalized Difference Water Index (NDWI)."""
    green = image[:, :, 0]  
    nir = image[:, :, 1]  
    ndwi = (green - nir) / (green + nir)
    return ndwi

def load_demo_image():
    """Load demo imagery bands and stack them into a single numpy array."""
    band_files = [
        "/File_path/Band_B04.jp2",
        "/File_path/Band_B08.jp2",
        "/File_path/Band_B03.jp2",
    ]
    bands = [rasterio.open(file).read(1) for file in band_files]
    image = np.dstack(bands)
    return image

def load_image(band_files):
    """Load user-provided bands and stack them into a single numpy array."""
    bands = [rasterio.open(file).read(1) for file in band_files]
    image = np.dstack(bands)
    return image

def plot_index(index, title):
    """Plot a vegetation index with Matplotlib and add a colorbar."""
    fig, ax = plt.subplots(figsize=(10, 10))
    cax = ax.imshow(index, cmap='RdYlGn') 
    fig.colorbar(cax, ax=ax, orientation='vertical')
    ax.set_title(title)
    plt.show()

def main():
    print("Welcome to the Indices Calculator for Sentinel Imagery Satellite.")
    print("This tool calculates NDVI, SAVI, and NDWI from Sentinel-2 imagery.")

    try:
        if input('Would you like to try the software? (Y/N): ').lower() == 'y':
            option = input('Choose an option: 1. Download your own imagery, 2. Use demo imagery: ').lower()
            if option == "1":
                band_files = []
                required_bands = ["Red (B04)", "NIR (B08)", "Green (B03)"]  
                for band in required_bands:
                    directory = input(f'Provide Band {band} Directory: ')
                    band_files.append(directory)
                img = load_image(band_files)
                
                operation = input('What would you like to do with the image (NDVI - SAVI - NDWI)? Choose (1/2/3) respectively: ')
                if operation == "1":
                    plot_index(calculate_ndvi(img), "NDVI")
                elif operation == "2":
                    plot_index(calculate_savi(img), "SAVI")
                elif operation == "3":
                    plot_index(calculate_ndwi(img), "NDWI")
                else:
                    print("Invalid option.")
            elif option == "2":
                img = load_demo_image()
                operation = input('What would you like to do with the image (NDVI - SAVI - NDWI)? Choose (1/2/3) respectively: ')
                if operation == "1":
                    plot_index(calculate_ndvi(img), "NDVI")
                elif operation == "2":
                    plot_index(calculate_savi(img), "SAVI")
                elif operation == "3":
                    plot_index(calculate_ndwi(img), "NDWI")
                else:
                    print("Invalid option.")
            else:
                print("Invalid option. Exiting the program.")
        else:
            print("Exiting the program.")
            exit()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram cancelled by user.")
