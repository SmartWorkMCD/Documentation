FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update
# RUN apt-get install -y libgtk2.0-dev
RUN apt-get install -y v4l-utils
# RUN v4l2-ctl --list-devices

COPY src/ .

CMD ["python", "main.py"]