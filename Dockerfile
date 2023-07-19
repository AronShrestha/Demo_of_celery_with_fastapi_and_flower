FROM python
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade paramiko cryptography
WORKDIR /app 
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app
