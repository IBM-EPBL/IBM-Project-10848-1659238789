FROM python:3.9
LABEL maintainer="upassini"
RUN apt-get update
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirement.txt
EXPOSE 5000
CMD [ "python", "app.py" ]