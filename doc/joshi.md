# Joshi: the joern shell interpreter

Joshi connects to an Octopus server and lets it execute a script. A script is
Gremlin code that you would normally send to the Octopus shell, except that
the following extras are allowed:

* Shebang line. May be useful if you want to execute the script directly, allthough it may not be so useful because it would tie the script to a particular database. Example:

   #!joshi.py -p myProject.tar.gz

* File includes. Can be used to include other scripts into the current script.

   #include file

# Usage

```
usage: joshi.py [-h] [-p PROJECT] [-r] [--no-json] file

positional arguments:
  file                  execute script from file instead of stdin

optional arguments:
  -h, --help            show this help message and exit
  -p PROJECT, --project PROJECT
                        project to execute
  -r, --raw             do not convert response data to string.
  --no-json             disable json encoding for response
```

* `-p` project: specify the project on which to run the query.
* `-r`: displays the data structure as received directly, without converting it to a string.
* `-no-json`: does not use JSON to communicate with the server.


