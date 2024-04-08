import numpy as np
import matplotlib.pyplot as plt
import dionysus as d
from matplotlib.ticker import FuncFormatter

# Example: Create a random point cloud
points = np.random.random((70, 3)) # Generate 70 points in 3D space, each coordinate is randomly chosen from [0,1)

# Convert point cloud to a Vietoris-Rips filtration
f = d.fill_rips(points, 3, 2.0) # Create a Vietoris-Rips complex with points, targeting 3D homology, radius up to 2.0

# Compute persistent homology
p = d.homology_persistence(f) # Calculate the persistent homology of the filtration

# Extract persistence diagrams
dgms = d.init_diagrams(p, f) # Initialize persistence diagrams from the computed homology


# Helper functions for formatting tick labels
def H_formatter(x, pos):
    return f'H{x:.0f}'

def t_formatter(x, pos):
    return f'{x:.0f}s'

def plot_barcode(diagrams):
# Create a single figure and axes for the plot
    fig, ax = plt.subplots()

    # Calculate the number of diagrams to set y-ticks accordingly
    num_diagrams = len(diagrams)
    y_ticks = np.arange(num_diagrams)
    y_tick_labels = [f'$H_{{{i}}}$' for i in range(num_diagrams)]

    base_colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    colors = base_colors * (len(diagrams) // len(base_colors) + 1)

    # Iterate through each dimension's diagram
    for i, dgm in enumerate(diagrams):
        # Plot each bar in the barcode
        for p in dgm:
            ax.plot([p.birth, p.death], [i, i], colors[i])

    # Setting custom formatter for the y-axis
    formatter = FuncFormatter(H_formatter)
    ax.yaxis.set_major_formatter(formatter)

    # Setting custom formatter for the x-axis
    formatter_t = FuncFormatter(t_formatter)
    ax.xaxis.set_major_formatter(formatter_t)

    # Set the y-ticks and labels according to homology dimensions
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_tick_labels)

    # Positions and labels for the x-axis
    tick_positions = [0,1, 2, 3, 4] # Assuming these positions are relevant for your data
    tick_labels = ['$t_0$','$t_1$', '$t_2$', '$t_3$', '$t_4$'] # Labels for the x-axis
    ax.set_xticks(tick_positions)
    ax.set_xticklabels(tick_labels)

    # Setting the plot title and labels
    plt.title("Persistence Barcode with Vietoris-Rips filtration")
    plt.xlabel("Time")
    plt.ylabel("Homology dimension")

    # Show the complete plot
    plt.show()
    plt.savefig('persistence_barcode.png')

# Call the plotting function with the calculated diagrams
plot_barcode(dgms)


