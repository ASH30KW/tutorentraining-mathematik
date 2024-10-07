import numpy as np
import plotly.graph_objects as go
import streamlit as st

st.title("Tutorentraining Mathematik")

# Second plot: 2D Circle Animation

# Create theta values
theta = np.linspace(0, 2 * np.pi, 100)

# Create x and y coordinates for the circle
x_circle = np.cos(theta)
y_circle = np.sin(theta)

# Initialize the figure
fig2 = go.Figure()

# Add the static blue circle trace (this will remain throughout the animation)
fig2.add_trace(go.Scatter(x=x_circle, y=y_circle, mode='lines', line=dict(color='blue'), name='Circle'))

# Add the point that will move along the circle
fig2.add_trace(go.Scatter(x=[np.cos(0)], y=[np.sin(0)], mode='markers', marker=dict(color='red', size=10), name='Moving Point'))

# Define frames for animation
frames2 = [go.Frame(data=[
    go.Scatter(x=x_circle, y=y_circle, mode='lines', line=dict(color='blue')),  # Keep blue circle
    go.Scatter(x=[np.cos(t)], y=[np.sin(t)], mode='markers', marker=dict(color='red', size=10))  # Update red point
]) for t in np.linspace(0, 2 * np.pi, 100)]

# Add animation settings
fig2.update(frames=frames2)

# Set layout for the animation with 1:1 aspect ratio
fig2.update_layout(
    xaxis=dict(range=[-1.5, 1.5], autorange=False, scaleanchor="y", scaleratio=1),  # 1:1 ratio for axes
    yaxis=dict(range=[-1.5, 1.5], autorange=False),
    updatemenus=[dict(type="buttons",
                      buttons=[dict(label="Play",
                                    method="animate",
                                    args=[None, dict(frame=dict(duration=50, redraw=True), fromcurrent=True)])])],
    showlegend=False
)

# Display the 2D circle animation in Streamlit
st.plotly_chart(fig2)

# First plot: 3D Parametric Curve

# Create the parameter t values
t = np.linspace(0, 2 * np.pi, 500)

# Parametric equations
x = np.cos(t)
y = np.sin(t)
z = t

# Create the 3D plot
fig1 = go.Figure()

# Add the parametric curve (static line)
fig1.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines', line=dict(color='blue', width=5), name='Curve'))

# Add the initial point that will move along the curve
fig1.add_trace(go.Scatter3d(x=[x[0]], y=[y[0]], z=[z[0]], mode='markers', marker=dict(color='red', size=5), name='Moving Point'))

# Create frames for the animation
frames1 = [go.Frame(data=[go.Scatter3d(x=x, y=y, z=z, mode='lines', line=dict(color='blue', width=5)),
                          go.Scatter3d(x=[x[k]], y=[y[k]], z=[z[k]], mode='markers', marker=dict(color='red', size=5))])
           for k in range(len(t))]

# Update the layout to include buttons and animation settings
fig1.update_layout(
    scene=dict(
        xaxis_title="γ1",
        yaxis_title="γ2",
        zaxis_title="γ3"
    ),
    updatemenus=[dict(type='buttons', showactive=False,
                      buttons=[dict(label='Play',
                                    method='animate',
                                    args=[None, dict(frame=dict(duration=20, redraw=True), fromcurrent=True, mode='immediate')]),
                               dict(label='Pause',
                                    method='animate',
                                    args=[[None], dict(frame=dict(duration=0, redraw=False), mode='immediate')])])],
    showlegend=False
)

# Add the frames to the figure
fig1.update(frames=frames1)

# Display the 3D parametric curve in Streamlit
st.plotly_chart(fig1)


