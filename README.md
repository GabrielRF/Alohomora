[![](https://dockerbuildbadges.quelltext.eu/status.svg?organization=gabrielrf&repository=alohomora)](https://hub.docker.com/r/gabrielrf/alohomora/builds/)

# Alohomora

![Alohomora](img/alohomora.gif)

* [About](#about)
* [Setup](#setup)
  * [Docker Compose](#docker-compose)
  * [Python](#python)
* [Contribute](#contribute)
* [Contact](#contact-me)

## About 

Alohomora is a Docker Container that opens a door if movement is detected. 

In other words, it watches a folder where a CFTV camera saves video files and, if a video is created, the container sends a command to open the door. 

It works on a ControlID IDFlex. A few changes are necessary to make it work on other ControlID models. 

## Setup

### Docker Compose

```
alohomora:
    image: gabrielrf/alohomora
    environment:
        - FOLDER=/
        - EXTENSION=mp4
        - DEVICE_IP=
        - LOGIN=admin
        - PASSWORD=
    restart: always
    volumes:
        - host_folder:container_folder
```

`FOLDER`: Folder that will be monitored by the script. In case of a folder tree, set the top-level folder.

`EXTENSION`: The extension of the file that should be sent. Usually `mp4` is the case.

`DEVICE_IP`: The IP of the ControlID IDFlex.

`LOGIN`: Web user of the ControlID. Default `admin`.

`PASSWORD`: Password of the web user.

### Python

First:

```
pip install inotify
```

Open `alohomora.py` and fill the variables `FOLDER`, `EXTENSION`, `DEVICE_IP`, `LOGIN` and `PASSWORD`.

Then:

```
python alohomora.py
```

## Contribute

Pull Requests and issues are always welcome!

## Contact me


[GabRF.com](https://gabrf.com)

[@GabrielRF](https://t.me/gabrielrf) on Telegram.
