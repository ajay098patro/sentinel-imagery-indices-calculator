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

def load_image(band_files):
    """Load bands and stack them into a single numpy array."""
    bands = [rasterio.open(file).read(1) for file in band_files]
    image = np.dstack(bands)
    return image

def plot_index(index, title):
    """Plot a vegetation index with Matplotlib and add a north arrow."""
    fig, ax = plt.subplots(figsize=(10, 10))
    cax = ax.imshow(index, cmap='RdYlGn') 
    fig.colorbar(cax, ax=ax, orientation='vertical')
    ax.set_title(title)
    plt.show()

def main():
    print("Welcome to the Indices Calculator for Sentinel Imagery Satellite.")
    print("This tool calculates NDVI, SAVI, and EVI from Sentinel-2 imagery.")

    try:
        a = input('Would you like to try the software? (Y/N): ').lower()
        if a == 'y':
            b = input('There are two options: either download the imagery of your own or use demo imagery (1/2): ').lower()
            if b == "1":
                band_files = []
                required_bands = ["Red (B04)", "NIR (B08)"]
                for band in required_bands:
                    c = input(f'Provide Band {band} Directory: ')
                    band_files.append(c)
                img = load_image(band_files)
                
                c = input('What would you like to do with the image (NDVI - SAVI)? Choose (1/2) respectively: ')
                if c == "1":
                    plot_index(calculate_ndvi(img), "NDVI")
                elif c == "2":
                    plot_index(calculate_savi(img), "SAVI")
                else:
                    print("Invalid option.")
            else:
                print("Demo imagery option not implemented yet.")
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
