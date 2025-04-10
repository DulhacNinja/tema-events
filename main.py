import config
import time
import platform
import multiprocessing
from publication import Publication
from subscription import Subscription
from concurrent.futures import ProcessPoolExecutor

def generate_publications(size):
    return [Publication() for _ in range(size)]

def generate_subscriptions(size):
    return [Subscription() for _ in range(size)]

def generate_parallel(generator, count):
    threads = config.THREAD_COUNT
    batch_size = count // threads
    extra_publications = count % threads

    batch_sizes = [batch_size + 1 if i < extra_publications else batch_size for i in range(threads)]

    with ProcessPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(generator, size) for size in batch_sizes]
        results = []
        for future in futures:
            results.extend(future.result())
    return results

def main():
    publications_count = config.PUBLICATIONS_COUNT
    subscriptions_count = config.SUBSCRIPTIONS_COUNT
    thread_count = config.THREAD_COUNT

    start = time.time()
    if thread_count == 1:
        parallel_type = "sequential (no parallelism)"
        publications = generate_publications(publications_count)
        subscriptions = generate_subscriptions(subscriptions_count)
    else:
        parallel_type = "parallel processing (processes)"
        publications = generate_parallel(generate_publications, publications_count)
        subscriptions = generate_parallel(generate_subscriptions, subscriptions_count)
    end = time.time()
    duration = round(end-start, 4)

    cpu_info = platform.processor()
    cpu_cores = multiprocessing.cpu_count()
    cpu_details = f"{cpu_info} ({cpu_cores} core{'s' if cpu_cores > 1 else ''})"

    print("\n--- Implementation Evaluation ---")
    print(f"Parallelization type: {parallel_type}")
    print(f"Parallelism factor: {thread_count} processes")
    print(f"Number of messages generated: {publications_count} publications, {subscriptions_count} subscriptions")
    print(f"Execution time: {duration} seconds")
    print(f"CPU specifications: {cpu_details}")
    print("----------------------------------\n")

    with open("publications.txt", "w") as f:
        for publication in publications:
            f.write(str(publication) + "\n")

    with open("subscriptions.txt", "w") as f:
        for subscription in subscriptions:
            f.write(str(subscription) + "\n")


if __name__ == "__main__":
    main()

