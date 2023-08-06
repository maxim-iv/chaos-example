FROM python:3

RUN apt update

RUN pip3 install --upgrade pip

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app

COPY main.py /
COPY requirements.txt /
RUN pip install -r requirements.txt
RUN python3 -m virtualenv --python=python3 virtualenv
EXPOSE 8001

CMD [ "python", "main.py" ]
