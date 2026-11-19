# Spatial Territorial Analysis Model (STAM)

[![python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**STAM (Spatial Territorial Analysis Model)** is an open-source, modular Python framework designed for computational spatial data science, macro-regional infrastructure evaluation, territorial vulnerability assessment, and comparative urban morphology studies.

The framework bridges architecture, regional planning, and spatial computational modeling by integrating automated geospatial ingestion, metric projections, custom buffer analyses, topographic audits, hydrological overlays, and interactive multi-criteria evaluations (MCE).

---

## Key Features

* **Automated Spatial Ingestion:** Dynamic ingestion of country boundaries, administrative regions, and street networks utilizing standardized GIS geometries via OSMnx.
* **Vector-Native Visualizations:** Robust rendering pipeline optimized for cloud notebooks (Google Colab) and production environments, avoiding external tile blockages (`tiles=None`) and utilizing clean vector geometries.
* **Parametric Buffer Analysis:** Scalable spatial corridor modeling adaptable to diverse territorial dimensions (e.g., estuarine tropical nodes like Barcarena, highland Arctic corridors like Murmansk).
* **Topographic & Hydrological Audits:** Automated calculation of surface hydrological restrictions, watershed buffers, and altitudinal amplitude/relief profiling using DEM elevation APIs.
* **Multi-Criteria Evaluation (MCE):** Dynamic spatial risk heatmaps assessing multi-variable vulnerability across urban nodes.
* **Consolidated Executive Audit Output:** Automated generation of structured HTML matrices compiling all analytical metrics into a unified summary report.

---

## Methodology & Architecture

STAM models territorial vulnerability and infrastructure resilience through an integrated 4-phase computational pipeline:

1. **Phase 1 & 2 (Ingestion & Perimeter):** Fetches global administrative boundaries, projects geographic coordinates to Projected Coordinate Systems (EPSG:3857), builds parametric buffers, and extracts real-world OSM road networks.
2. **Phase 3 (Topographic & Hydrological Audit):** Intersects surface water bodies and wetlands within the corridor and computes elevation metrics (min, max, altitudinal amplitude).
3. **Phase 4 (Multi-Criteria Evaluation - MCE):** Generates dynamic spatial risk heatmaps combining environmental and topographic constraints into structured point grids.
4. **Consolidated Reporting:** Compiles all spatial, hydrological, and altitudinal metrics into a clean, executive HTML audit table.

---

## Project Structure

```text
STAM-Spatial-Territorial-Analysis-Model/
│
├── stam_pipeline_complete.py   # Unified 4-phase integrated execution pipeline
├── osm_ingestion.py            # Standalone Phase 1 & 2: OSM boundary & road network ingestion
├── topographic_audit.py        # Standalone Phase 3: Hydrological & DEM topographic audit
├── mce_risk_evaluation.py      # Standalone Phase 4: Multi-Criteria Evaluation risk heatmap
├── requirements.txt            # Python dependencies (osmnx, geopandas, folium, etc.)
└── LICENSE                     # MIT Open Source License

## Quick Start (Google Colab / Local Python)

You can run the fully integrated pipeline using the unified script `stam_pipeline_complete.py`:

```python
import osmnx as ox
import geopandas as gpd
import numpy as np
import requests
import folium
from shapely.geometry import Point
from IPython.display import display, HTML

# Execute the complete 4-phase STAM pipeline for any territorial node
# Example: Barcarena, Brazil (Estuarine/Tropical Node)
run_stam_pipeline_transparent(
    place_name="Barcarena, Para, Brazil",
    lat=-1.5053,
    lon=-48.6256,
    buffer_km=3.0)

## **Project Roadmap**

- [x] **Phase 1 & 2:** Core engine MVP, multi-scalar territorial validation, and OSM road network vector ingestion.
- [x] **Phase 3:** Topographic elevation (DEM) and hydrological river basin/wetland overlays.
- [x] **Phase 4:** Multi-Criteria Evaluation (MCE) for dynamic spatial risk heatmaps.
- [x] **Consolidated Reporting:** Automated executive HTML audit matrices and vector-native visualization stability.

## **Author**

**Diego Rodrigues Nascimento**  
Urban Planner & Spatial Data Science Researcher  
GitHub: [@ARCHIDiego](https://github.com/ARCHIDiego)



