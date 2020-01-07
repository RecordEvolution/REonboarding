# Create image from Dockerfile

based on the crossbario/autobahn-python image

## create image from the directory where the dockerfile is via 

$ docker build -t mycrossbario:version1 .

## check if created

$ docker images

## run with parameters

$ docker run -v /Users/aortner/Playground/crossbario/:/app -e CBURL="ws://crossbar:8080/ws" -e CBREALM="realm1" --link=crossbar --rm -it mycrossbario:version1  python /app/1.hello-world/my_python_publisher.py

or

$ docker run -v /Users/aortner/Playground/crossbario/:/app -e CBURL="ws://crossbar:8080/ws" -e CBREALM="realm1" --link=crossbar --rm -it mycrossbario:version1  python /app/python/my_python_publisher.py


# Run the different dockers

## 1. Crossbar Router
Image available on docker-hub
$ docker run -v  /Users/aortner/Playground/crossbario/:/node  --name=crossbar -it -p 8080:8080 crossbario/crossbar

## 2. Crossbar Publisher
Image reads local python script and sends regular a counter and stock prices along
$docker run -v /Users/aortner/Playground/crossbario/:/app -e CBURL="ws://crossbar:8080/ws" -e CBREALM="realm1" --link=crossbar --rm -it mycrossbario:version1  python /app/python/my_python_publisher.py

## 3. Crossbar Receiver
I can't run the scrip on local mac due to issues with the zope package
$ docker run -v /Users/aortner/Playground/crossbario/:/app --name crossbar_sub -e CBURL="ws://crossbar:8080/ws" -e CBREALM="realm1" --link=crossbar --rm -it mycrossbario:version1  python /app/python/<my_python_subscriber class="python"></my_python_subscriber>


