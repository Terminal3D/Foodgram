FROM python

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]