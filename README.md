![GitHub last commit](https://img.shields.io/github/last-commit/richardschrauwen/hello-worlds?style=plastic)

# hello-worlds & other sample code
Collection of the basic code in various programming languages. Will always be a work in progress...

## the go way
Run hello world:
```golang
go run hello.go
```

other:

* Testing: `go test`

* Build: `go build`

* Install binary: `go install`

## the java legacy
Install Java SDK

Open a command prompt and execute:
```java
cd .\Javahelloworld\
javac ./Hello.java
java Hello
```
## the Python track
Install Python 3

Open a command prompt and execute: `python hellopython.py`

## AWS Lambda functions
AWS function-as-a-service

## Azure Webapp (Java)
Azure App Service web application (Java WAR file)

## Kubernetes

yaml file with a load-balanced helloworld example

## Docker
Dockerfile with hello world text in a clean directory

run: sudo docker build .

## AWK
One of my first scripting languages for text processing

Open a \*NIX command prompt and execute: echo "AWK World!" | awk -f hello.awk

## Other Python utilities

Open a command prompt in the directory where the scripts are.

```
cd hello-worlds/Pythonhelloworld
```
Usage examples below

Example code to read or write a comma separated value file and present as dictionaries
```
python .\csvreader.py
python .\csvwriter.py
```

Find files containing (part of) the input string 

```
python .\filefind.py -n java -d C:\ProgramData\Oracle
```

Find files larger than a size limit (bytes) in current dir or other path
```
python .\filesize.py -d C:\temp -l 1024

```

Count number of files of certain extension type in a path. Takes parameters from INI config file.
```
python .\filetypecount.py

```

Find files larger than a size Limit (bytes) and Extension type in a Dir.

Use `-e *` for all file types

```
python .\listfilesandsavetofile.py -d C:\temp -l 1024 -e .csv

```



## Other Java: Sending SMS and more

Code snippet for sending a Hello SMS message using the SMPP v3.4 protocol

Verzameld.java contains a collection of functions
