import multiprocessing

def cpu_intensive_task():
    while True:
        # Perform a more computationally intensive task
        x = 0
        for i in range(10**8):  # Reduce the loop size to make it faster
            x += i ** 2  # Add a heavier computation (e.g., squaring numbers)

if __name__ == "__main__":
    # Create more processes than CPU cores to increase CPU usage
    num_cores = multiprocessing.cpu_count()
    num_processes = int(num_cores * 1.5)  # Use 1.5x the number of CPU cores
    print(f"Starting {num_processes} CPU-intensive processes...")
    processes = []
    for _ in range(num_processes):
        p = multiprocessing.Process(target=cpu_intensive_task)
        processes.append(p)
        p.start()

    # Keep the processes running
    for p in processes:
        p.join()