# Crossbar.io

## Crossbar Router via Docker

Image `crossbario/crossbar` available on docker-hub. A router can be started via

```
docker run -v  /crossbario/:/node  --name=crossbar_router -it -p 8080:8080 crossbario/crossbar
```


## Crossbar Autobahn Client via Docker (Python)

For the Python client the image `crossbario/autobahn-python` has to be used. Depending on the Python Script it will then be a publisher or a subscriber

Image reads and executes local python script 
```
docker run -v /crossbario/:/app -e CBURL="ws://crossbar:8080/ws" -e CBREALM="realm1" --link=crossbar_router --rm -it crossbario/autobahn-python  python /app/my_python_script.py
```


## Crossbar Autobahn Client for Python

## Crossbar Autobahn Client for Nodejs

1. Install Nodejs via website download and executable (not via brew, there are dependencies missing)

2. Install Autobahn crossbar client via npm

```
npn install autobahn@0.9.5

# with all rights to overwright
npm install -g autobahn@0.9.5 --unsafe-perm=true --allow-root
```


Warning! The module for nodejs always fails on installation (os and ubuntu) due to weird dependencies.
This could be only solved by using and older version of the autobahn module
https://github.com/crossbario/autobahn-js/issues/216

