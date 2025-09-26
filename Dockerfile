FROM python:3.13.7-slim-trixie 

WORKDIR /app

VOLUME ["/config"]


COPY . .

RUN pip install -r requc.txt

EXPOSE 8000

CMD fastapi run src/main.py
