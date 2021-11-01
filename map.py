import pandas as pd
targets = pd.read_csv("honeypot_small.csv")

import plotly.express as px

# fig = px.scatter_mapbox(targets, lat="latitude", lon="longitude", hover_name="title", hover_data=["title", "city","state", "country"],
#                         color_discrete_sequence=["fuchsia"], zoom=3, height=900)

fig = px.scatter_mapbox(targets, lat="latitude", lon="longitude", hover_name="country", hover_data=["datetime", "srcstr", "proto"],
                        color_continuous_scale=px.colors.cyclical.IceFire, zoom=3, height=900, color="proto")
fig.update_layout(mapbox_style="open-street-map")
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
fig.write_html("map.html")


