import numpy as np
from skimage.filters import meijering, frangi

def normalize(array):
    """Normalize array to 0-1 range."""
    min_val = np.nanmin(array)
    max_val = np.nanmax(array)
    if max_val == min_val:
        return np.zeros_like(array)
    return (array - min_val) / (max_val - min_val)

def apply_structure_detection(data, clip_max=3.0, sigmas=range(2, 8, 2), method='frangi', **kwargs):
    """
    Applies vesselness filter to detect structural anomalies.
    
    Args:
        data: Input 2D numpy array.
        clip_max: Value to clip extreme highs.
        sigmas: Range of sigmas for the filter (controls thickness).
        method: 'frangi' or 'meijering'.
        **kwargs: Additional arguments for the filter (e.g., beta, alpha, black_ridges).
        
    Returns:
        tuple: (bright_norm, dark_norm)
    """
    # Fill Nodata
    data_filled = np.nan_to_num(data, nan=np.nanmedian(data))
    
    # Clip extreme values
    data_clipped = np.clip(data_filled, None, clip_max)
    
    filter_func = frangi if method == 'frangi' else meijering
    
    # 1. Detect Bright Ridges (High values)
    print(f"Detecting Bright Ridges ({method})...")
    # Handle specific args if needed, but kwargs usually works
    # Note: Meijering uses 'black_ridges' boolean too in recent versions or handles sign.
    # Frangi uses 'black_ridges'.
    
    bright_response = filter_func(data_clipped, sigmas=sigmas, black_ridges=False, **kwargs)
    bright_norm = normalize(bright_response)
    
    # 2. Detect Dark Ridges (Low values)
    print(f"Detecting Dark Ridges ({method})...")
    dark_response = filter_func(data_clipped, sigmas=sigmas, black_ridges=True, **kwargs)
    dark_norm = normalize(dark_response)
    
    return bright_norm, dark_norm
