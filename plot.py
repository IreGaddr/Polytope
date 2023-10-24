import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Earth parameters

Re = 6371e3  # Equatorial radius of Earth (meters)
             # Corresponds to 'a' in oblate spheroid equation
             # Used to calculate gravitational force and centrifugal force

Rp = 6357e3  # Polar radius of Earth (meters) 
            # Corresponds to 'c' in oblate spheroid equation
            # Defines flattening of spheroid vs equatorial radius

ω = 7.29e-5 # Rotational angular velocity of Earth (radians/sec)
            # Determines strength of centrifugal force
            # Key parameter creating oblateness

G = 6.67e-11 # Gravitational constant (m^3/kg*s^2) 
             # Used in calculating gravitational force 

ρ = 5515    # Average density of Earth (kg/m^3)
            # Used to find Earth's mass from volume
            # Impacts gravitational force

# 3D grid
n = 100   
φ = np.linspace(0, 2*np.pi, n)
θ = np.linspace(0, np.pi, n)
Φ, Θ = np.meshgrid(φ, θ)

# Gravitational acceleration 
m = ρ * 4/3 * np.pi * Re**3
g = G * m / Re**2

# Centrifugal acceleration
acf = ω**2 * Re * np.cos(Θ)   

# Oblate spheroid equation 
r = Re / (1 + acf/g * (1 - np.sin(Θ)**2))  

# Generate mesh
X = r * np.sin(Θ) * np.cos(Φ) 
Y = r * np.sin(Θ) * np.sin(Φ)
Z = r * np.cos(Θ)

# Plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='viridis', linewidth=0, antialiased=False)

# Axis labels  
ax.set_xlabel('X (km)', linespacing=3.2)
ax.set_ylabel('Y (km)', linespacing=3.1)
ax.set_zlabel('Z (km)', linespacing=3.4)

# Title
ax.set_title('Oblate Spheroid Earth', fontsize=14, pad=25)  

# Colorbar
cbar = fig.colorbar(surf, shrink=0.6, aspect=12) 
cbar.set_label('Radius (km)', rotation=270, labelpad=20)

# Annotations
ax.text2D(0.05, 0.93, 'Centrifugal Bulge Due to Rotation', fontsize=12, transform=ax.transAxes)
ax.text2D(0.05, 0.03, 'Cross-Section', fontsize=12, transform=ax.transAxes)

plt.show()