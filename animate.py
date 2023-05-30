# ==================================

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animateXY(x_values,y_values,interval=50):
   # Sample x and y values
    # x_values = [1, 2, 3, 4, 5]
    # y_values = [1, 4, 9, 16, 25]

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Create an empty marker (initially invisible)
    marker, = ax.plot([], [], 'ro', markersize=10)

    # Create empty lists to store the trace
    trace_x = []
    trace_y = []

    # Create an empty trace line or scatter plot
    trace, = ax.plot([], [], 'b-')  # Change the line style/color as desired
    # Alternatively, you can use scatter plot to represent the trace points:
    # trace = ax.scatter([], [], color='blue')

    # Set the axis limits
    ax.set_xlim(min(x_values), max(x_values))
    ax.set_ylim(min(y_values), max(y_values))

    # Add a grid
    ax.grid(True)

    # Animation update function
    def update(frame):
        # Get the current x and y values
        x = x_values[frame]
        y = y_values[frame]

        # Update the marker data
        marker.set_data(x, y)

        #  Add the current position to the trace
        trace.set_data(x_values[:frame+1], y_values[:frame+1])

        # Add the current position to the trace
        # trace_x.append(x)
        # trace_y.append(y)
        
        # Update the trace plot
        # ax.plot(trace_x, trace_y, 'b-')  # Change the line style/color as desired
        # Alternatively, you can use scatter plot to represent the trace points:
        # ax.scatter(trace_x, trace_y, color='blue')

        return marker, trace

    # Create the animation
    animation = FuncAnimation(fig, update, frames=len(x_values), interval=interval, blit=True)

    # Show the plot
    plt.show()

# ==================================
