import numpy as np
import plotly.graph_objects as go
import streamlit as st

# Create theta values
theta = np.linspace(0, 2 * np.pi, 100)

# Create x and y coordinates for the circle
x = np.cos(theta)
y = np.sin(theta)

# Initialize the figure
fig = go.Figure()

# Add the static blue circle trace (this will remain throughout the animation)
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='blue'), name='Circle'))

# Add the point that will move along the circle
point = go.Scatter(x=[np.cos(0)], y=[np.sin(0)], mode='markers', marker=dict(color='red', size=10), name='Moving Point')

# Add the point trace to the figure
fig.add_trace(point)

# Define frames for animation
frames = [go.Frame(data=[
    go.Scatter(x=x, y=y, mode='lines', line=dict(color='blue')),  # Keep blue circle
    go.Scatter(x=[np.cos(t)], y=[np.sin(t)], mode='markers', marker=dict(color='red', size=10))  # Update red point
]) for t in np.linspace(0, 2 * np.pi, 100)]

# Add animation settings
fig.update(frames=frames)

# Set layout for the animation with 1:1 aspect ratio
fig.update_layout(
    xaxis=dict(range=[-1.5, 1.5], autorange=False, scaleanchor="y", scaleratio=1),  # 1:1 ratio for axes
    yaxis=dict(range=[-1.5, 1.5], autorange=False),
    updatemenus=[dict(type="buttons",
                      buttons=[dict(label="Play",
                                    method="animate",
                                    args=[None, dict(frame=dict(duration=50, redraw=True), fromcurrent=True)])])],
    showlegend=False
)

# Display the plot in Streamlit
st.plotly_chart(fig)
