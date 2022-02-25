FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN apt-get update
COPY requirements.txt /app/requirements.txt
COPY start_server.sh /app/start_server.sh
RUN chmod a+x /app/start_server.sh
RUN pip install -r requirements.txt
COPY . /app

CMD ["/bin/sh", "/app/start_server.sh"]