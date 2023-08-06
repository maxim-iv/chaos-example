FROM python:3

COPY main.py /
COPY requirements.txt /
RUN pip install -r requirements.txt
RUN python3 -m virtualenv --python=python3 virtualenv
EXPOSE 8000
CMD [ "python", "main.py" ]