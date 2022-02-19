Here I show 3 methods on how to combine the dictionary. In the code, I stores the combined dictionary into a new dictionary but you can combine them into existing dictionary without the need to create a new one like what I did in the code.

The first method, you can use `.update()`. This method require an iterable with key value pairs as it argument. Please take note that this method will modified the dictionary and it return None as it will not return anything from it. Here as you can guess, if you want to combine the dictionary into the existing one, you need to call this method onto the dictionary that you want it to hold the new value with.

The second method is by using unpacking. As the name suggest, we unpack our dictionary into an empty dictionary. Thus all those unpacked key value pairs will then stores into this empty dictionary since we unpack them inside it.

The third method can only be use in python 3.9 and above. We use the pipe `|`.  