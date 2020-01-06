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
(https://brew.sh/)

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


5.3 pypy3 (brew install pypy3) —> done
5.4 python3 (brew install python3) —> done
5.4.1 bumpversion (sudo pip3 install bumpversion)

### Sublime
Download the installer from [https://www.sublimetext.com/3](https://www.sublimetext.com/3) and install Sublime text3 to your Mac book.
Sublime can be called directly from the terminal via `subl filename` 
Then add the following sublime packages 


#### 1. package controll
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

Now install the following packages we ofte use 
#### 2. gitsavvy
Full git and GitHub integration with Sublime Text 3.
#### 3. 
Full-featured code intelligence and smart autocomplete engine

#### 4. SideBarEnhancement
Enhancements to Sublime Text sidebar. Files and folders.

#### 5. Javascript Beautify
js-beautify for sublime

#### 6. SqlBeautify
A sublime plugin to format SQL

### 7. HTML-CSS-JS Prettify 
HTML, CSS, JavaScript, JSON, React/JSX and Vue code formatter for Sublime 3 via node.js

#### 6. Auto​PEP8
Automatically formats Python code to conform to the PEP 8 style guide using autopep8 and pep8 modules

#### Dockerfile Syntax Highlighting
Dockerfile syntax

#### 7. Sublime​REPL
SublimeREPL - run an interpreter inside ST2 (Clojure, CoffeeScript, F#, Groovy, Haskell, Lua, MozRepl, NodeJS, Python + virtualenv, R, Ruby, Scala...)


7. Docker for mac
7.1 Kinematic (UI for Docker)
7.2 Minikube (kubernetes) 

11. Anvil SimpleWebServer (https://anvilformac.com/)
12. MDWiki a MarkdownWiki (http://dynalon.github.io/mdwiki/#!index.md)

- PGAdmin 4
- TablePlus


## To learn
1. Docker -> done
- Kubenets
- Crossbario -> done
2. Ngix -> done
3. Create a Webserver with Docker and Ngix and NodeJs on Raspberry
4. Prime in Python: https://realpython.com/primer-on-python-decorators/




