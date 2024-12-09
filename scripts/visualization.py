import matplotlib.pyplot as plt
import seaborn as sns

def generate_heatmap(df, title="Heatmap"):
    """
    Generates a heatmap for the correlation matrix of the DataFrame.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title(title)
    plt.show()
