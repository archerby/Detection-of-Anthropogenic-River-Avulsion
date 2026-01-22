# Ghost River Detection Protocol

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9-blue)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/archerby/detection-of-anthropogenic-river-avulsion/blob/main/notebooks/03_analysis_meijering.ipynb)

## Story
This repository contains the algorithms used to detect the 19th-century avulsion of the Iput River (Dobrush, Belarus). By combining **Meijering ridge detection** on topographic data (FABDEM) with **Sentinel-2 spectral indices** (NDRE), we reveal a "Ghost River"—a massive paleochannel system abandoned due to anthropogenic engineering (the derivation canal construction).

## Installation

```bash
conda env create -f environment.yml
conda activate river-avulsion
```

## Quick Start

1.  **Clone the repo**:
    ```bash
    git clone https://github.com/archerby/detection-of-anthropogenic-river-avulsion.git
    cd detection-of-anthropogenic-river-avulsion
    ```
2.  **Run the analysis**:
    Launch Jupyter Lab and open `notebooks/03_analysis_meijering.ipynb`. The notebook is pre-configured to run on the sample data in `data/sample/`.

    ```bash
    jupyter lab
    ```

## Data Availability
- **Sample Data**: A 5x5 km subset of the study area is included in `data/sample/` for immediate reproducibility.
- **Full Dataset**: The complete 100 GB dataset (Sentinel-1, Sentinel-2, FABDEM) is available at Zenodo: [DOI Link Needed].

## Results
The algorithm identifies structural anomalies corresponding to the historical riverbed.
*(Insert Figure Here)*

## License
MIT License
