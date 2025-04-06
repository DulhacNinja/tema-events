import config
from publication import Publication
from subscription import Subscription


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


# TODO: parallelize this and modify how weights work to make it more accurate
def main():
    publications = generate_publications()
    subscriptions = generate_subscriptions()

    with open("publications.txt", "w") as f:
        for publication in publications:
            f.write(str(publication) + "\n")

    with open("subscriptions.txt", "w") as f:
        for subscription in subscriptions:
            f.write(str(subscription) + "\n")


if __name__ == "__main__":
    main()
