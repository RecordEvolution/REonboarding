# Tech Stack Setup

## Setup a blank Mac Book
Reset the Mac Book and install a fresh OS 
Set up your user

## Get accounts set up
1) **Google:** get work email and google account in the company account --> Marko
2) **Github:** add your privat account to the organisation --> Marko
3) **Slack:** add your work email to our Slack group --> Marko
4) **Sage Lohnabrechnung:** setup account on Sage Lohnabrechnung --> Marko


## Install the following Software on your Mac Book

### Google Chrome Browser
Download Chrome from: [https://www.google.de/chrome/](https://www.google.de/chrome/)


### Google GDrive 
Install the GDrive file stream adapter to your mac so that our GDrive system is available on your local file system on your Mac Book
Therefore follow the instructions in
[Download and HowTo at: https://www.google.com/drive/download/ ](https://www.google.com/drive/download/)

### Slack
Go to the Apple App Store, install the local client to your Mac Book and create your user account. ([More information on slack.com: ](https://slack.com/intl/de-de/downloads/mac))
Join our workspace `recordevolution.slack.com` where you should have been added. If not reach out to Marko


### Homebrew 
Check out the website for details [https://brew.sh/](https://brew.sh/)
open the terminal and install brew with the following comand
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```


### Git 
Download Git from [https://git-scm.com/downloads](https://git-scm.com/downloads) and install on your Mac Book.
Configure git so that you can connect via ssh to our Github repositories.

### Node and npm 
Download Node.js from [https://nodejs.org/en/download/](https://nodejs.org/en/download/) and install on your Mac Book.
!Warning: do not install node and npm via brew. This causes some weird error on using the Crossbar and Autobahn modules.

When npm is installed install the following packages:
#### 1. Bower package manager
``` 
npm install -g bower
```

#### 2. Polymer cli 
```
npm install -g polymer-cli
```

#### 3. Vue cli 
```
npm install -g @vue/cli
```
#### 4. Crossbar Autobahn client 
```
# check the installed npm version
npm -version
# if version < 4.5.0
sudo npm install -g ws@1 autobahn
# if version >= 4.5.0
sudo npm install -g ws@2 autobahn
```
This client is sometimes tricky to install localy. If you have issues check the manual at [https://github.com/crossbario/autobahn-js](https://github.com/crossbario/autobahn-js)


### Python
Install Python 3 and Pypy 3 (pip) 
The default version of Python on the Mac is still (Jan 2020) Python 2.7. Installing Python 3 directly to the OS can iterfere with the system Pyhton and cause a lot of mess if the path variables are wrong.

#### Install Python via Brew 
Simple way is to install Python 3 via brew but this might need some addional configurations of the PATH evironment variables [google it](https://programwithus.com/learn-to-code/install-python3-mac/)
1. Install `XCode` from the App Store
2. Install Python 3 via brew install
```
brew install python3
```

#### Install Python via Conda 
Installing Conda / Anacoda allows to easy create fully configured capsulated evironments that do not interfere with the system Python.
Compared to virtualenv conda also capsulates system dependencies like gcc or java sdk into the environment

1. Download Anaconda Python 3.7 version from [https://www.anaconda.com/distribution/](https://www.anaconda.com/distribution/)
2. Install Anaconda
3. Check if Conda is installed 
```
# list python packages installed
conda list 
```
4. Create new Conda environment
``` 
# check for already created environments
conda env list

# create a new conda environment with python 3.7 
conda create --name MyPython3 python=3.7

# clone an existing component 
conda reate --clone MyPython3 --name MyPython3-Clone

```
5. activate environment and set it up
```
# activate environment
conda activate MyPython3 

# deactivate environment 
conda deactivate 


# install conda packages 
conda install numpy

# install pip packages
pip install numpy 
# or
python -m pip install numpty
```

### Sublime
Download the installer from [https://www.sublimetext.com/3](https://www.sublimetext.com/3) and install Sublime text3 to your Mac book.
Sublime can be called directly from the terminal via `subl filename` 
Then add the following sublime packages 


#### 1. Package controll
perform the following steps to install package controll 
1. open sublime
2. click the Preferences > Browse Packages… menu
3. Browse up a folder and then into the Installed Packages/ folder
4. Download the Package Control.sublime-package from [https://packagecontrol.io/installation](https://packagecontrol.io/Package%20Control.sublime-package)and copy it into the Installed Packages/ directory
5. Restart Sublime Text

To install further packages this package manager can now directly be used. Package Control is driven by the Command Palette. To open the palette, press `cmd+shift+p` (OS X). All Package Control commands begin with `Package Control:`, so start searching by typing `Package`.

The command palette will now show a number of commands. The most relevant is the `Install Package` command.
Choose `Package Control: Install Package` and hit `enter` to browse in the list of available packages.
To install a package selet it and hit `enter`. Then restart Sublime.

Available packages can be browsed at [https://packagecontrol.io/](https://packagecontrol.io/)

We use typically the following packages
#### 2. Gitsavvy
Full git and GitHub integration with Sublime Text 3.
#### 3. 
Full-featured code intelligence and smart autocomplete engine

#### 4. SideBarEnhancement
Enhancements to Sublime Text sidebar. Files and folders.

#### 5. Javascript Beautify
js-beautify for sublime

#### 6. SqlBeautify
A sublime plugin to format SQL

#### 7. HTML-CSS-JS Prettify 
HTML, CSS, JavaScript, JSON, React/JSX and Vue code formatter for Sublime 3 via node.js

#### 6. Auto​PEP8
Automatically formats Python code to conform to the PEP 8 style guide using autopep8 and pep8 modules

#### 7. Dockerfile Syntax Highlighting
Dockerfile syntax

#### 8. Sublime​REPL
SublimeREPL - run an interpreter inside ST2 (Clojure, CoffeeScript, F#, Groovy, Haskell, Lua, MozRepl, NodeJS, Python + virtualenv, R, Ruby, Scala...)


### Docker
Install Docker for Mac including Kinematic (UI for Docker)
1. Download Docker from [https://download.docker.com/mac/beta/Docker.dmg](https://download.docker.com/mac/beta/Docker.dmg)
2. Double-click the DMG file, and drag-and-drop Docker into your Applications folder.
3. You need to authorize the installation with your system password.
4. Double-click Docker.app to start Docker.
5. The whale in your status bar indicates Docker is running and accessible.
6. Docker presents some information on completing common tasks and links to the documentation.
7. You can access settings and other options from the whale in the status bar. a. Select About Docker to make sure you have the latest version.

### Kubernetes
Install Minicube to create a single node virtual Kubernetes Cluster on your Mac


### Postgres 
####  1. Install a Postgres Database. 
Idealy you start a Docker container with Postgres
```
docker run -d -p 5432:5432 --name my-postgres -e POSTGRES_PASSWORD=tingel postgres
```

#### 2. Connect via Postgres shell 
```
# first open the bash on the docker container
docker exec -it my-postgres bash

# then enter the psql shell
psql -U postgress

# then fire psql commands

# 1. list all databases
=# \l

# 2. connect to a database
=# \c dvdrental

# 3. check out this databse
=# \d

# 4. Quit the postgres shell
=# \q
```

#### 3. Connect via PG Admin

#### 4. Connect via TablePlus

#### 5. Connect via Python 
Import the database adapter and Pandas

```
# Postgres database adapter 
import psycopg2 as pgsgl
# Pandas framework
import pandas as pd
```
Read SQL statement into Pandas dataframe

```
hostname = 'jumper1.repods.io'
username = 'tingel'
password = 'tingel'
database = 'reone'
port = '49161'

try:
    conn = pgsgl.connect( host=hostname, user=username, password=password, dbname=database, port=port )
    print("Yes!! connect to the database")
except:
    print("ERROR: I am unable to connect to the database")

try: 
    sqlquery='Select * from schema_abm.t_immoscout_2'
    df = pd.read_sql(sqlquery,con=conn)
    print("Hurra!! Data loaded into Dataframe")
except:
    print("ERROR: Data load failed")

conn.close()
```
Check the data and get some insights
```
df.head()
df.describe()
df.columns
```





