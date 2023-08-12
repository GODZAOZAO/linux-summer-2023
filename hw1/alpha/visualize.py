import matplotlib.pyplot as plt

def read_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        times = [float(line.strip()) for line in lines]
    return times

insertion_times = read_data('stree_insert_time.txt')
deletion_times = read_data('stree_delete_time.txt')

tree_sizes = [100 * i for i in range(1, len(insertion_times) + 1)]

plt.figure(figsize=(10, 6))
plt.plot(tree_sizes, insertion_times, label='Insertion Time')
plt.plot(tree_sizes, deletion_times, label='Deletion Time')
plt.xlabel('Tree Size')
plt.ylabel('Time (seconds)')
plt.title('Insertion and Deletion Times in S-Tree')
plt.legend()
plt.grid()

# Save the plot as an image in the same directory
plt.savefig('s_tree_insertion_deletion_times.png')

# Show the plot
plt.show()
