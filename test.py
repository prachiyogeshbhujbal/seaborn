import pandas as pd
from plot import LinePlot, BarPlot, ScatterPlot, Histogram, Heatmap

# Sample data for testing
data = {
    "Category": ["A", "B", "C", "D"],
    "Values1": [10, 15, 20, 25],
    "Values2": [20, 25, 30, 35],
    "Values3": [5, 10, 15, 20],
    "Values4": [2, 4, 6, 8],
    "Values5": [3, 6, 9, 12],
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# 1. **Line Plot**
line_plot = LinePlot(
    data=df,
    title="Line Plot Example",
    x_label="Category",
    y_label="Values"
)
line_plot.plot(x_col="Category", y_cols=["Values1", "Values2"], linewidth=2)
line_plot.show()

# 2. **Bar Plot**
bar_plot = BarPlot(
    data=df,
    title="Bar Plot Example",
    x_label="Category",
    y_label="Values"
)
bar_plot.plot(x_col="Category", y_cols=["Values1", "Values2"], color=["blue", "orange"])
bar_plot.show()

# 3. **Scatter Plot**
scatter_plot = ScatterPlot(
    data=df,
    title="Scatter Plot Example",
    x_label="Values1",
    y_label="Values2"
)
scatter_plot.plot(x_col="Values1", y_col="Values2", color="green", s=100, alpha=0.8)
scatter_plot.show()

# 4. **Histogram**
histogram = Histogram(
    data=df,
    title="Histogram Example",
    x_label="Values1",
    y_label="Frequency"
)
histogram.plot(col="Values1", bins=5, color="purple", alpha=0.7)
histogram.show()

# 5. **Heatmap**
heatmap = Heatmap(
    data=df,
    title="Heatmap Example"
)
heatmap.plot(cmap="viridis")
heatmap.show()

# Additional examples:
# 6. **Saving plots**
line_plot.save("line_plot_example.png")
bar_plot.save("bar_plot_example.png")
scatter_plot.save("scatter_plot_example.png")
histogram.save("histogram_example.png")
heatmap.save("heatmap_example.png")

print("All plots created and saved successfully!")
