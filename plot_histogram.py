import matplotlib.pyplot as plt

def plot_histogram(data_to_display: dict, title: str):
    plt.barh(range(len(data_to_display)), data_to_display.values())
    plt.yticks(range(len(data_to_display)), list(data_to_display.keys()))
    plt.title(label=title)
    plt.show()
    print("", end="\n\n")