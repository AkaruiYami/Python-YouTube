# Reverse a String

## Method 1: List Convertion
What we do here is we convert our string into a list of letters and then we use method `.reverse()` onto our newly created list.

## Method 2: Built-In Reversed Function
Here, we will use built-in function available in python which is `reversed()`. This function will return an iterator. So we need to join all the character from the iterator using `.join()` method onto an empty string to extract the result.

## Method 3: Index Stepping
This method is most simple and easy to understand. What we do is accessing the characters from the string from left to right. Which is from last item to the first item. Here we can ignore the start and end part of the indexing. `message[START:END:STEP]`.