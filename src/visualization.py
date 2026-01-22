import matplotlib.pyplot as plt
import numpy as np

def plot_structure_composite(original_data, bright_norm, dark_norm, output_path=None, percentiles=(95, 95)):
    """
    Generates a composite visualization of the structural detection.
    
    Args:
        original_data: The background data (e.g. PC3).
        bright_norm: Normalized bright ridge detection.
        dark_norm: Normalized dark ridge detection.
        output_path: Path to save the figure (optional).
        percentiles: Tuple of (bright_percentile, dark_percentile).
    """
    thresh_bright = np.percentile(bright_norm, percentiles[0])
    thresh_dark = np.percentile(dark_norm, percentiles[1])
    
    fig, ax = plt.subplots(figsize=(18, 12))
    
    # Background: Original Data (Greyscale)
    plt.imshow(original_data, cmap='gray', vmin=np.nanpercentile(original_data, 2), vmax=np.nanpercentile(original_data, 98), interpolation='nearest', alpha=1.0)
    
    # Overlay Bright -> Red/Orange
    bright_viz = np.ma.masked_where(bright_norm < thresh_bright, bright_norm)
    plt.imshow(bright_viz, cmap='Reds', interpolation='nearest', alpha=0.7, vmin=thresh_bright, vmax=1.0)
    
    # Overlay Dark -> Blue/Cyan
    dark_viz = np.ma.masked_where(dark_norm < thresh_dark, dark_norm)
    plt.imshow(dark_viz, cmap='Blues', interpolation='nearest', alpha=0.7, vmin=thresh_dark, vmax=1.0)
    
    plt.title("Structural Detection (Frangi Vesselness)")
    plt.axis('off')
    
    plt.figtext(0.5, 0.02, 
               "Red = Bright Ridges (High Values)\nBlue = Dark Ridges (Low Values)", 
               ha='center', fontsize=12, color='white', bbox=dict(facecolor='black', alpha=0.7))
    
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"Saved visualization: {output_path}")
        plt.close()
    else:
        plt.show()
