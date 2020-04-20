![GitHub last commit](https://img.shields.io/github/last-commit/richardschrauwen/hello-worlds?style=plastic)
 and   ![hello-worlds](https://img.shields.io/github/repo-size/richardschrauwen/hello-worlds?style=plastic)
 and ![GitHub All Releases](https://img.shields.io/github/downloads/RichardSchrauwen/hello-worlds/total?style=plastic)

# hello-worlds & other sample code
Collection of the basic code in various programming languages I use / have used. Will always be a work in progress and in no way a complete collection of all helloworlds in the world.

## the go way
Prerequisites: install golang

E.g. Ubuntu:

`sudo apt-get update`

`sudo apt install golang-go`

Run hello world (compiles the application into a temporary folder and starts the executable binary. It properly cleans up the temporary files):
```golang
cd Gohelloworld/
go run hello.go
```

Other useful commands:

* Build the command in package 'main' and leave the result in the current working directory as a binary executable:
 
`go build`

and run the executable with:

`./hello`

* Cleaning up:

`go clean`

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
Prerequisites: Amazon Web Services (free) account

AWS function-as-a-service. AWS Lambda is a compute service that lets you run code without provisioning or managing servers.

Following tutorial:
https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html

Testing can be done in many ways. Easiest is to use the AWS Lambda console directly. Another one I tried is API Gateway, which is more costly because API endpoint uptime is charged.

## AWS CLI and Python SDK (Boto3)

Use the Python3 SDK for AWS (boto3) to use an AWS message queue, following tutorial:
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs.html

Some simple scripts to:
* List all available SQS queues `python3 aws-listSQSqueues`
* Create a new one if needed ('Test') `python3 aws-createSQSqueue`
* Send a new hello message to the queue `python3 aws-sendSQSmessage`
* Retrieve the message and remove from queue `python3 aws-processSQSmessage`

## Azure Webapp (Java)
Prerequisites: Azure account

Azure App Service is a fully managed web application hosting platform as a service (PaaS).

A web application *HelloWorld* can be run from a .WAR file, following Azure tuturial:
https://docs.microsoft.com/en-gb/azure/app-service/containers/quickstart-java

To start the resulting Azure App Service web application (Java WAR file) use the URL resulting from the deploy step. E.g.
https://helloworld-1579689050889.azurewebsites.net/

![website status](https://img.shields.io/website?down_message=down&style=flat-square&up_color=green&up_message=up&url=https%3A%2F%2Fhelloworld-1579689050889.azurewebsites.net%2F)

## Kubernetes
Prerequisites: install Kubernetes and start cluster

*hello-application.yaml* is a yaml file with a load-balanced helloworld example from:
https://kubernetes.io/docs/tasks/access-application-cluster/service-access-application-cluster/

```
cd K8helloworld/
sudo kubectl apply -f ./hello-application.yaml
sudo kubectl expose deployment hello-world --type=NodePort --name=example-service
sudo kubectl describe services example-service
```

Note down the *NodePort:* TCP port number from the response e.g. **31941**

Do a HTTP request to localhost if you are working locally

`curl http://localhost:31941`


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

List the total size of a path and the top N largest directories under it.
```
python .\dirsize.py -d C:\ProgramData -n 10
```

Find files containing (part of) the input string
```
python .\filefind.py -n java -d C:\ProgramData\Oracle
```

Find all files larger than a threshold size **l**imit (bytes) in a **d**ir.
```
python .\filesize.py -d C:\temp -l 1024

```

Count number of files of certain extension type in a path. Takes its parameters from INI config file *Example.ini*. If present it replaces the keyword *$USER* with the OS login name, which is handy for a path containing the user name.
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

MP3Count - media file statistics.  Takes its parameters from INI config file *Example.ini*. If present it replaces the keyword *$USER* with the OS login name, which is handy for a path containing the user name.
```
python .\mp3count.py

```

Number of files - Analyses the file types in a path.
```
python .\numberoffiles.py

```

Parse config files - Read a config file in INI format. Takes its parameters from INI config file *Example.ini*.
```
python .\parseconfigfile.py

```

Write config files - Create a config file in INI format. Creates parameters in INI config file *Example.ini*.
```
python .\writeconfigfile.py

```

## Other Java: Sending SMS and more

Code snippet for sending a Hello SMS message using the SMPP v3.4 protocol

Verzameld.java contains a collection of functions
