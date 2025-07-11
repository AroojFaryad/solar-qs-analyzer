import numpy as np
from astropy.io import fits
import os

# Dataset paths 
dataset_paths = [] #Datasets paths

qs_means = []

def compute_qs_mean(dataset_path):
    qs_file = os.path.join(dataset_path, "qs.txt") #qs.txt file contain QS values (y1:y2, x1:x2)
    wings_file = os.path.join(dataset_path, "wings.fits") #H_alpha wing 

    # Load QS region
    qs_coords = np.loadtxt(qs_file).astype(int)
    x1, x2, y1, y2 = qs_coords

    # Load first frame of wings.fits
    wing_data = fits.getdata(wings_file)[0]
    qs_region = wing_data[y1:y2, x1:x2]

    # Compute and return mean
    return np.mean(qs_region)

# Compute and print QS mean for each dataset
for path in dataset_paths:
    try:
        qs_mean = compute_qs_mean(path)
        qs_means.append(qs_mean)
        print(f"QS mean for {path}: {qs_mean:.2f}")
    except Exception as e:
        qs_means.append(None)
        print(f"Failed to process {path}: {e}")

print("\nFinal list of QS means:", qs_means)
######################end###################################
