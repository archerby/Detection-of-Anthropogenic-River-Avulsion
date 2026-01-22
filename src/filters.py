import numpy as np
from skimage.filters import frangi

def normalize(array):
    """Normalize array to 0-1 range."""
    min_val = np.nanmin(array)
    max_val = np.nanmax(array)
    if max_val == min_val:
        return np.zeros_like(array)
    return (array - min_val) / (max_val - min_val)

def apply_structure_detection(data, nodata=None, clip_max=3.0, sigmas=range(2, 8, 2), method='frangi'):
    """
    Apply structural detection (Frangi or Meijering vesselness) to identify ridges.
    
    Args:
        data (np.ndarray): Input image data.
        nodata (float, optional): Nodata value to mask/fill.
        clip_max (float): Maximum value to clip input data to (enhances contrast).
        sigmas (iterable): Range of sigmas for the filter.
        method (str): 'frangi' or 'meijering'.
        
    Returns:
        tuple: (bright_norm, dark_norm) - Normalized structure maps for bright and dark ridges.
    """
    from skimage.filters import frangi, meijering

    # Filter selector
    filter_func = meijering if method == 'meijering' else frangi

    # Fill Nodata for filter stability
    if nodata is not None:
         data_filled = np.where(data == nodata, np.nanmedian(data), data)
         data_filled = np.where(np.isnan(data_filled), np.nanmedian(data_filled), data_filled)
    else:
         data_filled = data

    # Clip extreme values
    data_clipped = np.clip(data_filled, None, clip_max)
    
    # 1. Detect Bright Ridges (High values)
    # Meijering and Frangi logic for black_ridges is similar
    bright_response = filter_func(data_clipped, sigmas=sigmas, black_ridges=False)
    bright_norm = normalize(bright_response)
    
    # 2. Detect Dark Ridges (Low values)
    dark_response = filter_func(data_clipped, sigmas=sigmas, black_ridges=True)
    dark_norm = normalize(dark_response)
    
    return bright_norm, dark_norm
