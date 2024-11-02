import numpy as np
import matplotlib.pyplot as plt

def plotf():
    # Open the data file and count intervals
    filename = 'quadrature.data'
    with open(filename, 'r') as fid:
        num_intervals = sum(1 for line in fid)

    # Set up arrays to store interval data and thread info
    a = np.zeros(num_intervals, dtype=float)
    b = np.zeros(num_intervals, dtype=float)
    thread_id = np.zeros(num_intervals, dtype=int)

    # Read data from file, recording start, end points, and thread number
    with open(filename, 'r') as fid:
        for k, line in enumerate(fid):
            linelist = line.split()
            thread_id[k] = int(linelist[0])  # Thread number
            a[k] = float(linelist[1])  # Start of interval
            b[k] = float(linelist[2])  # End of interval

    # Colors for each thread
    colors = ['b', 'r', 'g', 'm', 'c', 'y']
    
    # Plot intervals assigned to each thread
    plt.figure(figsize=(10, 8))
    plt.title("Subintervals Used in Adaptive Quadrature")
    plt.axis("off")
    plt.rc("font", size=16)
    for k in range(num_intervals):
        color_index = thread_id[k] % len(colors)  # Cycle through colors
        plt.plot([a[k], b[k]], [-float(k), -float(k)], color=colors[color_index], linewidth=2)

    plt.savefig('adapt_quad_parallel_1.png', dpi=400, bbox_inches='tight')
    plt.show()

    # Generate data points for plotting function and intervals
    xtmp = np.zeros(5 * num_intervals, dtype=float)
    xs = 0
    for k in range(num_intervals):
        h = b[k] - a[k]
        xtmp[xs] = a[k]
        xtmp[xs + 1] = a[k] + 0.25 * h
        xtmp[xs + 2] = a[k] + 0.5 * h
        xtmp[xs + 3] = a[k] + 0.75 * h
        xtmp[xs + 4] = b[k]
        xs += 5

    # Ensure unique points in x for plotting
    xsorted = np.unique(xtmp)
    fsorted = func(xsorted)
    xfine = np.linspace(-2.0, 4.0, 1001)
    ffine = func(xfine)

    # Plot the function and sampled points from adaptive quadrature
    plt.figure(figsize=(10, 6))
    plt.plot(xfine, ffine, color='b', linewidth=2, label='f(x)')
    plt.plot(xsorted, fsorted, 'o', color='r', markersize=5, label='Sample Points')
    plt.plot(xsorted, -1.1 + 0.0 * xsorted, 'k|', markersize=10)
    plt.xlim(-2.1, 4.1)
    plt.ylim(-1.55, 1.55)
    plt.xticks(np.linspace(-2.0, 4.0, 7))
    plt.yticks(np.linspace(-1.5, 1.5, 7))
    plt.title("Adaptive Quadrature Sampling Points")
    plt.legend()
    plt.savefig('adapt_quad_parallel_2.png', dpi=400, bbox_inches='tight')
    plt.show()

def func(x):
    return np.exp(-(10.0 * x) ** 2) + np.sin(x)

if __name__ == "__main__":
    plotf()
