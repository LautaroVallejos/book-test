FROM python:3.9

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

RUN apt-get install python3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]