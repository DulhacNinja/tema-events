import config
import time
from publication import Publication
from subscription import Subscription
from concurrent.futures import ProcessPoolExecutor

def generate_publications():
    publications = []
    for _ in range(config.PUBLICATIONS_COUNT):
        publication = Publication()
        publications.append(publication)
    return publications


def generate_subscriptions():
    subscriptions = []
    for _ in range(config.SUBSCRIPTIONS_COUNT):
        subscription = Subscription()
        subscriptions.append(subscription)
    return subscriptions

def generate_publication_batch(size):
    return [Publication() for _ in range(size)]

def generate_subscription_batch(size):
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

# TODO: modify how weights work to make it more accurate
def main():
    start = time.time()
    if config.THREAD_COUNT == 1:
        publications = generate_publications()
        subscriptions = generate_subscriptions()
    else:
        publications = generate_parallel(generate_publication_batch, config.PUBLICATIONS_COUNT)
        subscriptions = generate_parallel(generate_subscription_batch, config.SUBSCRIPTIONS_COUNT)
    end = time.time()
    duration = round(end-start, 4)

    print(f"Generated {config.PUBLICATIONS_COUNT} publications and {config.SUBSCRIPTIONS_COUNT} subscriptions in {duration} seconds with {config.THREAD_COUNT} threads")

    with open("publications.txt", "w") as f:
        for publication in publications:
            f.write(str(publication) + "\n")

    with open("subscriptions.txt", "w") as f:
        for subscription in subscriptions:
            f.write(str(subscription) + "\n")


if __name__ == "__main__":
    main()

