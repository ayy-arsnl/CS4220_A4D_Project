import pandas as pd
targets = pd.read_csv("honeypot_data.csv")

import plotly.express as px

fig = px.scatter_mapbox(targets, lat="latitude", lon="longitude", hover_name="country", hover_data=["srcstr"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=900)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
fig.write_html("map.html")


