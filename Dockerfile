FROM python:latest
#RUN apt-get update -y
#RUN apt-get install  -y python3 python3-pip python-dev
WORKDIR /src
COPY . .
COPY creativness /creativness/
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python","run.py"]

#NOTE>Deploy docker images