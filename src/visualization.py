import matplotlib.pyplot as plt
import numpy as np

def plot_structure_composite(data, bright_norm, dark_norm, 
                             thresh_bright=None, thresh_dark=None, 
                             percentiles=None,
                             output_path=None):
    """
    Generate a composite visualization of structural detection results.
    
    Args:
        data (np.ndarray): Original background data (e.g., PC3).
        bright_norm (np.ndarray): Normalized bright ridge response.
        dark_norm (np.ndarray): Normalized dark ridge response.
        thresh_bright (float, optional): Manual threshold for showing bright ridges.
        thresh_dark (float, optional): Manual threshold for showing dark ridges.
        percentiles (tuple, optional): (bright_pct, dark_pct) to calculate thresholds automatically.
        output_path (str or Path, optional): Path to save the figure. If None, shows the plot.
    """
    if percentiles is not None:
        if len(percentiles) >= 2:
            thresh_bright = np.percentile(bright_norm, percentiles[0])
            thresh_dark = np.percentile(dark_norm, percentiles[1])
            
    if thresh_bright is None:
        thresh_bright = np.percentile(bright_norm, 95)
    if thresh_dark is None:
        thresh_dark = np.percentile(dark_norm, 95)
        
    fig, ax = plt.subplots(figsize=(18, 12))
    
    # Background: Original (Greyscale)
    # Robust scaling for background
    valid_data = data[~np.isnan(data)]
    if valid_data.size > 0:
        vmin, vmax = np.percentile(valid_data, [2, 98])
    else:
        vmin, vmax = -2, 4 # Fallback
        
    plt.imshow(data, cmap='gray', vmin=vmin, vmax=vmax, interpolation='nearest', alpha=1.0)
    
    # Overlay Bright -> Red/Orange
    bright_viz = np.ma.masked_where(bright_norm < thresh_bright, bright_norm)
    plt.imshow(bright_viz, cmap='Reds', interpolation='nearest', alpha=0.7, vmin=thresh_bright, vmax=1.0)
    
    # Overlay Dark -> Blue/Cyan
    dark_viz = np.ma.masked_where(dark_norm < thresh_dark, dark_norm)
    plt.imshow(dark_viz, cmap='Blues', interpolation='nearest', alpha=0.7, vmin=thresh_dark, vmax=1.0)
    
    plt.title("Structural Detection Composite")
    plt.axis('off')
    
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        
    plt.show()
