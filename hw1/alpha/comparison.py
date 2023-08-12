import matplotlib.pyplot as plt

def read_time_data(filename):
    with open(filename, 'r') as file:
        return [float(line.strip()) for line in file]

def plot_comparison(x_values, y1_values, y2_values, xlabel, ylabel, title, filename):
    plt.figure(figsize=(10, 6))

    plt.plot(x_values, y1_values, label='S-Tree')
    plt.plot(x_values, y2_values, label='AVL-Tree')

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)

    plt.savefig(filename)
    plt.show()

if __name__ == '__main__':
    tree_sizes = list(range(100, 500100, 100))  # Adjust the range based on your data
    s_tree_insertion_times = read_time_data('stree_insert_time.txt')
    avl_tree_insertion_times = read_time_data('avl_insertion_time.txt')
    s_tree_deletion_times = read_time_data('stree_delete_time.txt')
    avl_tree_deletion_times = read_time_data('avl_delete_time.txt')

    # Insertion Time Comparison
    plot_comparison(tree_sizes, s_tree_insertion_times, avl_tree_insertion_times,
                    xlabel='Tree Size', ylabel='Time (seconds)',
                    title='Insertion Time Comparison between S-Tree and AVL-Tree',
                    filename='insertion_comparison.png')

    # Deletion Time Comparison
    plot_comparison(tree_sizes, s_tree_deletion_times, avl_tree_deletion_times,
                    xlabel='Tree Size', ylabel='Time (seconds)',
                    title='Deletion Time Comparison between S-Tree and AVL-Tree',
                    filename='deletion_comparison.png')
