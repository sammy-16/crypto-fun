### Some basic commands for creating and encrypting JSON

# This is how you create JSON using the CLI directly instead of dealing with an editor.

```bash
echo '{
    "name": "John",
    "age": 30,
    "city": "New York"
}' > output.json
```

# This is how you create a zip file using the CLI directly instead of dealing with an editor.

```bash
Compress-Archive -Path 'F:\CSE 545\crypto-fun\JSON_encrypt\hacker.json' -DestinationPath 'F:\CSE 
545\crypto-fun\JSON_encrypt\hacker.zip'
```

# This is how you encrypt the zip file using the CLI directly instead of dealing with an editor.

```bash
7z u hacker.zip -pHacker -mhe
```