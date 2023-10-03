### In this section we use an already existing git repo https://github.com/fortenforge/cryptopals.git to generate a MD4 collision

### The repo contains a python script that generates a MD4 collision

### In order for you to run the md4_collision.py script you should first use the sys library to set the path of your directory, it will not be able to recognize your path directly on Windows

## The script does not take any input but will generate a MD4 collision based on randomness

## We get all hex values and hashes through this

# We need to convert these strings to base64 and find out the collisions