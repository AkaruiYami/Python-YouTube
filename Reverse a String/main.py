def main():
    message = "!dlroW olleH"

    # using list convertion
    words = list(message)
    words.reverse()
    print("".join(words))
    
    # using built-in reversed function
    reversed_message = reversed(message)
    print("".join(reversed_message))

    # using index stepping
    print(message[::-1])

if __name__ == "__main__":
    main()
