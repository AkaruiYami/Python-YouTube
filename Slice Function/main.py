def get_secret_string():
    return "MdTScEruVSgZFQhevSZarsoieZnldeJOQtgDqpUayxbiGFOCQDymOgqXYRlUfKAavXPcDenjoZatnkvTFUZMYGL nqvhzauFNjImuidXrKEVssQaTxfOZLNTsDDjaiutUcNTAcKuzTxXUWajVcj anSqObtnsfijbzwVjNFmrURaOJHdptmOncEyhqgAXtPFBGHajFBroCwCKGdempXGpwtepBBeDllBmeyhPcsmbTjfFxkpMsPmPwKMUdwoUKW"


def greet(msg):
    print("The secret message is: {}".format(msg.upper()))


def main():
    secret = get_secret_string()

    # slice(start, stop)
    # the same as [1:10]
    my_slice = slice(1, 10)

    # slice(stop)
    # the same as [:10]
    my_slice = slice(10)

    # slice(start, stop, step)
    # the same as [10::23]
    my_slice = slice(10, None, 23)

    # slice(start, stop, step)
    # the same as [3:196:12]
    my_slice = slice(3, 196, 12)

    print(secret[my_slice])
    print(secret[my_slice])
    print(secret[my_slice])
    print(secret[my_slice])
    greet(secret[my_slice])


if __name__ == "__main__":
    main()
