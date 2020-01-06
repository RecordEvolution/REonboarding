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

#### Google Chrome Browser
[Download from: https://www.google.de/chrome/](https://www.google.de/chrome/)


### Google GDrive 
Install the GDrive file stream adapter to your mac so that our GDrive system is available on your local file system on your Mac Book
Therefore follow the instructions in
[Download and HowTo at: https://www.google.com/drive/download/ ](https://www.google.com/drive/download/)

### Slack
Go to the Apple App Store, install the local client to your Mac Book and create your user account. ([More information: ](https://slack.com/intl/de-de/downloads/mac))
Join our workspace `recordevolution.slack.com` where you should have been added. If not reach out to Marko


### Homebrew 
(https://brew.sh/)

### Git 
[Download git from https://git-scm.com/downloads](https://git-scm.com/downloads) and install on your Mac Book.
Configure git and connect it to Github. 

### Node and npm 
[Download Node.js from https://nodejs.org/en/download/](https://nodejs.org/en/download/) and install on your Mac Book.
!Warning: do not install node and npm via brew. This causes some weird error on using the Crossbar and Autobahn modules.

When npm is installed install the following packages:
* Bower package manager
``` 
npm install -g bower
```

* Polymer cli 
```
npm install -g polymer-cli
```

* Vue cli 
```
npm install -g @vue/cli
```
* Crossbar Autobahn client 
```
# check the installed npm version
npm -version
# if version < 4.5.0
sudo npm install -g ws@1 autobahn
# if version >= 4.5.0
sudo npm install -g ws@2 autobahn
```
This client is sometimes tricky to install localy. If you have issues [check the manual at https://github.com/crossbario/autobahn-js](https://github.com/crossbario/autobahn-js)


### Python 3
Install Python3 and Pypy3 (pip) 


5.3 pypy3 (brew install pypy3) —> done
5.4 python3 (brew install python3) —> done
5.4.1 bumpversion (sudo pip3 install bumpversion)

6. Sublime text3 — done
6.1 package mangager sublime text 3 -> done
6.2 gitsavvy -> done
6.2 GitGutter -> Issue
6.3 SublimeCodeIntel -> done
6.4 SideBarEnhancement -> done
6.5 html, css, js beautify
6.6 auto pep8
6.7 REPL

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




