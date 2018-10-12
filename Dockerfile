FROM python:3.7-alpine

RUN pip install pytelegrambotapi
RUN pip install inotify

ADD alohomora.py / 

CMD [ "python", "./alohomora.py" ]
