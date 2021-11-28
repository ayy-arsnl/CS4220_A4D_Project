# CS4220_A4D_Project
Data visualization project with mapbox and AWS botnet dataset - Fall, 2021

## Group Members

Alexander Urquhart

Andrew Nguyen

Aleksandra Anderson

Dylan Batizy

Ahmad Najee-Ullah

## About

Our dataset contains information on AWS honeypots that have caught a botnet attempting 
to infect them. This information includes the source's IP address, the date and time 
of capture, the protocol being used, and precise information about each honeypot's 
location. We have provided two different visualization styles for the data: a heatmap 
of all captures from 3/3/2013 to 3/15/2013, and a detail map that shows each honeypot 
individually.

## Usage

To switch between the two views, find the button in the top left that says "Change 
Map Style". 

On the heatmap, clusters are displayed on a color scale from blue to red, where blue 
indicates a less dense cluster of honeypots and red indicates a high concentration 
of honeypots. Click the magnifying glass icon to search for a specific location. Use 
either the scroll wheel on your mouse or the +/- buttons on the map to zoom in and 
out. If your map gets rotated, you can use the "Reset bearing to north" button 
(button with arrows, directly under +/- button) to reset the rotation. 

On the detail map, each data point (honeypot) is displayed individually. The points 
shown are filtered by date, so you will only see data points collected over a 
timespan of one (particular) day at any given time. To select the day, find the 
slider at the bottom and slide the dot to the day you would like to view. To see a 
timelapse of the days together, click the "play" button to the left of the slider, 
and to stop the timelapse, click the stop button directly to the right of the play 
button. Each point is color-coded depending on the protocol used for infection. 
A blue point is TCP, an orange point is UDP, and a green point is ICMP. 
Additionally, you may hover your mouse over any point on the map to reveal more 
information about that specific honeypot. 

### Honeypot Heatmap Preview 
https://api.mapbox.com/styles/v1/aurquhart/ckv47hzoo5f9o14o34w82filu.html?title=view&access_token=pk.eyJ1IjoiYXVycXVoYXJ0IiwiYSI6ImNrdWVzZGIxcTBjbzQyb3Q5MDRtbXNudHgifQ.1gI2_puV4N2zOcUzml7PyQ&zoomwheel=true&fresh=true#5.41/38.689/-90.221
