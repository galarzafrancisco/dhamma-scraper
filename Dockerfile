FROM python:3.8-alpine

WORKDIR /code
COPY . .

# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python", "./main.py" ]