import matplotlib.pyplot as plt

def save_plot(filename):
    """Save current figure to a file."""
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

def apply_labels(xlabel=None, ylabel=None, title=None):
    """Apply consistent labels and title to the current figure."""
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    if title:
        plt.title(title)

def close_figure():
    """Close current figure to free memory."""
    plt.close()
