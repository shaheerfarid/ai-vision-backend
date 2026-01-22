import matplotlib.pyplot as plt
import numpy as np

def plot_heatmap(heatmap: dict, title="Library Desk Occupancy Heatmap"):

    zones = list(heatmap.keys())
    values = list(heatmap.values())

    heatmap_array = np.array(values).reshape(1, -1)

    plt.imshow(heatmap_array, cmap="coolwarm", aspect="auto")
    plt.colorbar(label="Occupancy / Confidence")
    plt.xticks(range(len(zones)), zones)
    plt.yticks([])
    plt.title(title)
    plt.show()


# Example
if __name__ == "__main__":
    example_heatmap = {
        "zone_1": 0.32,
        "zone_2": 0.87,
        "zone_3": 0.79
    }

    plot_heatmap(example_heatmap)
