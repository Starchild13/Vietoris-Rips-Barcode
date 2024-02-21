# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import dionysus as d  # Assuming 'd' refers to a library for TDA, adjust the import as per the actual library used

# Example: Create a random point cloud
points = np.random.random((200, 2))  # Generate 100 points in 2D space, each coordinate is randomly chosen from [0,1)

# Convert point cloud to a Vietoris-Rips filtration
f = d.fill_rips(points, 2, 2.0)  # Create a Vietoris-Rips complex with points, targeting 2D homology, radius up to 2.0

# Compute persistent homology
p = d.homology_persistence(f)  # Calculate the persistent homology of the filtration

# Extract persistence diagrams
dgms = d.init_diagrams(p, f)  # Initialize persistence diagrams from the computed homology

# Define a function to plot the persistence barcode
def plot_barcode(diagrams):
    # Iterate through each dimension's diagram
    for i, dgm in enumerate(diagrams):
        # Plot each bar in the barcode
        for p in dgm:
            plt.plot([p.birth, p.death], [i, i], 'k')  # 'k' for black color
    # Set plot titles and labels
    plt.title("Persistence Barcode")  # Title of the plot
    plt.xlabel("Time")  # X-axis label
    plt.ylabel("Homology dimension")  # Y-axis label indicating different homology dimensions
    plt.show()  # Display the plot

# Call the plotting function with the calculated diagrams
plot_barcode(dgms)