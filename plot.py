import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class Plot:
    def __init__(self, data, title=None, x_label=None, y_label=None,
                 color_scheme=None, figsize=(10, 6)):
        """
        Base class for creating plots with customizable properties.

        Args:
            data (pd.DataFrame or dict): Data to be plotted.
            title (str, optional): Plot title.
            x_label (str, optional): X-axis label.
            y_label (str, optional): Y-axis label.
            color_scheme (dict, optional): Custom color mapping.
            figsize (tuple, optional): Figure size (width, height).
        """
        self.data = self._validate_data(data)
        self.fig, self.ax = plt.subplots(figsize=figsize)
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.color_scheme = color_scheme or {}

    def _validate_data(self, data):
        """Validate and prepare input data."""
        if isinstance(data, pd.DataFrame):
            return data
        elif isinstance(data, dict):
            return pd.DataFrame(data)
        else:
            raise ValueError("Data must be a pandas DataFrame or dictionary.")

    def set_labels(self, title=None, x_label=None, y_label=None):
        """Set plot labels."""
        if title:
            self.ax.set_title(title)
        if x_label:
            self.ax.set_xlabel(x_label)
        if y_label:
            self.ax.set_ylabel(y_label)
        return self

    def show(self):
        """Display the plot."""
        plt.tight_layout()
        plt.show()
        return self

    def save(self, filename):
        """Save the plot to a file."""
        self.fig.savefig(filename)
        return self


class LinePlot(Plot):
    def plot(self, x_col, y_cols, **kwargs):
        """
        Create a line plot.

        Args:
            x_col (str): Column to use for x-axis.
            y_cols (str or list): Column(s) to plot on y-axis.
            **kwargs: Additional plotting parameters.
        """
        y_cols = [y_cols] if isinstance(y_cols, str) else y_cols

        for col in y_cols:
            self.ax.plot(self.data[x_col], self.data[col], label=col, **kwargs)

        self.ax.legend()
        self.set_labels(
            title=self.title or "Line Plot",
            x_label=self.x_label or x_col,
            y_label=self.y_label or "Values"
        )
        return self


class BarPlot(Plot):
    def plot(self, x_col, y_cols, **kwargs):
        """
        Create a bar plot.

        Args:
            x_col (str): Column to use for x-axis categories.
            y_cols (str or list): Column(s) to plot as bars.
            **kwargs: Additional plotting parameters.
        """
        y_cols = [y_cols] if isinstance(y_cols, str) else y_cols

        x = np.arange(len(self.data[x_col]))
        width = kwargs.get("width", 0.8 / len(y_cols))

        for i, col in enumerate(y_cols):
            offset = (i - len(y_cols) / 2) * width
            self.ax.bar(x + offset, self.data[col], width, label=col, **kwargs)

        self.ax.set_xticks(x)
        self.ax.set_xticklabels(self.data[x_col])
        self.ax.legend()

        self.set_labels(
            title=self.title or "Bar Plot",
            x_label=self.x_label or x_col,
            y_label=self.y_label or "Values"
        )
        return self


class ScatterPlot(Plot):
    def plot(self, x_col, y_col, **kwargs):
        """
        Create a scatter plot.

        Args:
            x_col (str): Column to use for x-axis.
            y_col (str): Column to use for y-axis.
            **kwargs: Additional plotting parameters.
        """
        self.ax.scatter(self.data[x_col], self.data[y_col], **kwargs)

        self.set_labels(
            title=self.title or "Scatter Plot",
            x_label=self.x_label or x_col,
            y_label=self.y_label or y_col
        )
        return self


class Histogram(Plot):
    def plot(self, col, bins=10, **kwargs):
        """
        Create a histogram.

        Args:
            col (str): Column to plot.
            bins (int or array-like, optional): Number of bins or bin edges.
            **kwargs: Additional plotting parameters.
        """
        self.ax.hist(self.data[col], bins=bins, **kwargs)

        self.set_labels(
            title=self.title or "Histogram",
            x_label=self.x_label or col,
            y_label=self.y_label or "Frequency"
        )
        return self


class Heatmap(Plot):
    def plot(self, **kwargs):
        """Create a heatmap."""
        numeric_data = self.data.select_dtypes(include=[np.number])  # Select only numeric columns
        if numeric_data.empty:
            raise ValueError("No numeric data available to plot a heatmap.")

        cax = self.ax.matshow(numeric_data.corr(), cmap=kwargs.get("cmap", "coolwarm"))
        self.fig.colorbar(cax)

        self.ax.set_xticks(np.arange(len(numeric_data.columns)))
        self.ax.set_yticks(np.arange(len(numeric_data.columns)))
        self.ax.set_xticklabels(numeric_data.columns, rotation=90)
        self.ax.set_yticklabels(numeric_data.columns)

        self.set_labels(title=self.title or "Heatmap")
        return self
