import geopandas as gpd
import pandas as pd
import folium
from shapely.geometry import Point

def algoritmo_stam_analise_territorial(nome_pais='China', raio_buffer_km=150, exportar_mapa=True):
    """
    STAM (Spatial Territorial Analysis Model) - Core Engine MVP (Versão Completa)
    Calcula buffers de análise territorial, projeção métrica, métricas de impacto e gera mapa interativo Folium.
    """
    print(f"[STAM Engine] A carregar limites territoriais para: {nome_pais}...")
    
    # 1. Obter limites do país via Natural Earth (GeoPandas dataset)
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    pais = world[world['name'] == nome_pais]
    
    if pais.empty:
        raise ValueError(f"País '{nome_pais}' não encontrado na base de dados.")
    
    # 2. Rejeição e Projeção Métrica (EPSG:3857 para cálculos em metros/km)
    pais_projected = pais.to_crs(epsg=3857)
    area_total_km2 = pais_projected.geometry.area.sum() / 1e6
    
    # 3. Ponto centroidal de análise
    centroid_proj = pais_projected.geometry.centroid.iloc[0]
    
    # 4. Geração do Buffer Paramétrico de Infraestrutura
    buffer_geom = centroid_proj.buffer(raio_buffer_km * 1000)
    gdf_buffer = gpd.GeoDataFrame(geometry=[buffer_geom], crs="EPSG:3857")
    area_buffer_km2 = gdf_buffer.geometry.area.sum() / 1e6
    
    # 5. Cálculo do Rácio de Impacto Territorial
    impact_ratio = (area_buffer_km2 / area_total_km2) * 100
    
    # Resumo quantitativo em DataFrame
    df_resultados = pd.DataFrame([{
        'Território': nome_pais,
        'Área Total (km²)': round(area_total_km2, 2),
        'Raio Buffer (km)': raio_buffer_km,
        'Área Buffer (km²)': round(area_buffer_km2, 2),
        'Rácio de Impacto (%)': round(impact_ratio, 2)
    }])
    
    # 6. Geração de Mapa Interativo (Folium) para visualização web
    if exportar_mapa:
        print("[STAM Engine] A gerar mapa interativo espacial (Folium)...")
        # Converter de volta para WGS84 (EPSG:4326) para exibição correta no leaflet/web
        pais_wgs84 = pais_projected.to_crs(epsg=4326)
        buffer_wgs84 = gdf_buffer.to_crs(epsg=4326)
        
        centroid_wgs84 = pais_wgs84.geometry.centroid.iloc[0]
        m = folium.Map(location=[centroid_wgs84.y, centroid_wgs84.x], zoom_start=4)
        
        # Adicionar polígono do país à camada do mapa
        folium.GeoJson(
            pais_wgs84,
            style_function=lambda x: {'fillColor': '#1b4d3e', 'color': '#000000', 'weight': 1, 'fillOpacity': 0.4}
        ).add_to(m)
        
        # Adicionar buffer de infraestrutura ao mapa
        folium.GeoJson(
            buffer_wgs84,
            style_function=lambda x: {'fillColor': '#d4af37', 'color': '#b8860b', 'weight': 2, 'fillOpacity': 0.6}
        ).add_to(m)
        
        nome_arquivo_mapa = f"stam_mapa_{nome_pais.lower()}.html"
        m.save(nome_arquivo_mapa)
        print(f"[STAM Engine] Mapa interativo guardado com sucesso como '{nome_arquivo_mapa}'.")
        
    print("[STAM Engine] Análise concluída com sucesso.")
    return df_resultados

if __name__ == "__main__":
    df = algoritmo_stam_analise_territorial(nome_pais='China', raio_buffer_km=150, exportar_mapa=True)
    print(df)
