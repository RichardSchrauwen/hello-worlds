![GitHub last commit](https://img.shields.io/github/last-commit/richardschrauwen/hello-worlds?style=plastic)

# hello-worlds & other sample code
Collection of the basic code in various programming languages. Will always be a work in progress...

## the go way
Prerequisites: install golang

Run hello world:
```golang
go run hello.go
```

other:

* Testing: `go test`

* Build: `go build`

* Install binary: `go install`

## the java legacy
Prerequisites: Install Java SDK

Open a command prompt and execute:
```java
cd .\Javahelloworld\
javac ./Hello.java
java Hello
```
## the Python track
Prerequisites: Install Python 3

Open a command prompt and execute: `python hellopython.py`

## AWS Lambda functions
Prerequisites: Amazon account

AWS function-as-a-service

## Azure Webapp (Java)
Prerequisites: Azure account

Azure App Service web application (Java WAR file)

## Kubernetes
Prerequisites: install Kubernetes and start cluster

yaml file with a load-balanced helloworld example

## Docker
Prerequisites: install Docker

Place the Dockerfile with hello world text in a clean directory and run: 
`sudo docker build .`

## AWK
One of my first scripting languages for text processing together with sed

Open a \*NIX command prompt and execute: `echo "AWK World!" | awk -f hello.awk`

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

Find all files larger than a threshold size **l**imit (bytes) in a **d**ir.
```
python .\filesize.py -d C:\temp -l 1024

```

Count number of files of certain extension type in a path. Takes its parameters from INI config file *Example.ini*. If present it replaces the keyword $USER with the OS login name, which is handy for a path containing the user name.
```
python .\filetypecount.py

```

Lists all files in a in a **d**ir and outputs to screen. 
```
python .\listallfiles.py

```

Find files larger than a threshold size **l**imit (bytes) and **e**xtension type in a **d**ir and output to file for offline analysis.

Use `-e *` for all file types

```
python .\listfilesandsavetofile.py -d C:\temp -l 1024 -e .csv

```



## Other Java: Sending SMS and more

Code snippet for sending a Hello SMS message using the SMPP v3.4 protocol

Verzameld.java contains a collection of functions
