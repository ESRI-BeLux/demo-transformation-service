import requests
import json  # To serialize the geometries into a JSON string

# URL for the Project operation, here we use a sample server of esri, if they kick you out, you can contact
# me to create an account on Arcgis Location Platform for free to use those services
url = "https://sampleserver6.arcgisonline.com/arcgis/rest/services/Utilities/Geometry/GeometryServer/project"

# Parameters for the request
# please refer to this page: https://developers.arcgis.com/rest/services-reference/enterprise/project/ for other geometry types
params = {
    "inSR": 31370,  # Input Spatial Reference Lambert72
    "outSR": 4326,  # Output Spatial Reference WGS84, use 3812 for Lambert2008
    "geometries": json.dumps(
        {
            "geometryType": "esriGeometryPoint",
            "geometries": [{"x": 147876.83, "y": 183333.66}],
        }
    ),
    "transformation": json.dumps(
        {"name": "Belge_1972_To_ETRS_1989"}
    ),  # specified transformation, dont change
    "f": "json",
}

response = requests.get(url, params=params)


print("Request URL:", response.url)

if response.status_code == 200:
    projected_geometry = response.json()
    print("Projected Geometry:", projected_geometry)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
