# Spatial Territorial Analysis Model (STAM)

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**STAM (Spatial Territorial Analysis Model)** is an open-source, modular Python framework designed for computational spatial data science, macro-regional infrastructure evaluation, and territorial vulnerability assessment. 

The framework bridges architecture, regional planning, and spatial computational modeling by integrating automated geospatial ingestion, metric projections, custom buffer analyses, and interactive mapping.

---

## Key Features

- **Automated Spatial Ingestion:** Dynamic ingestion of country boundaries utilizing standardized GIS geometries.
- **Metric Vector Projections:** Real-time transformation of geographic coordinates to Projected Coordinate Systems (EPSG:3857) for precise metric area calculations ($km^2$).
- **Parametric Buffering:** Scalable spatial corridor modeling adaptable to diverse territorial dimensions (e.g., East Asian macro-regions, Eurasian continental corridors, Middle Eastern river basins).
- **Quantitative Vulnerability Output:** Automated generation of quantitative risk tables paired with clean geospatial visualization layers via interactive Leaflet/Esri maps.

---

## Methodology & Architecture

STAM models territorial vulnerability through a multi-step computational pipeline:

1. **Boundary Fetching:** Retrieves global administrative geometries.
2. **Geodetic Area Transformation:** Computes total continental surface area.
3. **Infrastructure Buffer Simulation:** Generates critical corridors around target geographic centroids.
4. **Impact Ratio Calculation:** Derives the proportional impact index:
$$\text{Impact Ratio (\%)} = \left( \frac{\text{Buffer Area}}{\text{Total Territorial Area}} \right) \times 100$$

---

## Quick Start (Google Colab / Local Python)

```python
import geopandas as gpd
import folium
import pandas as pd

# Execute the modular STAM engine
from stam_engine import algoritmo_stam_analise_territorial

# Example run for macro-territorial vulnerability assessment
df_results = algoritmo_stam_analise_territorial(nome_pais='China', raio_buffer_km=150)
```
## Project Roadmap
[x] Phase 1: Core engine MVP & multi-scalar territorial validation.

[ ] Phase 2: OSMnx real-world transport & energy infrastructure network ingestion.

[ ] Phase 3: Topographic elevation (DEM) & hydrological river basin overlays.

[ ] Phase 4: Multi-Criteria Evaluation (MCE) for dynamic spatial risk heatmaps.

---

## Author
Diego Rodrigues Nascimento

Architect & Spatial Data Science Researcher

GitHub: @ARCHIDiego
