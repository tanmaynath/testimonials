FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /testimonial-app
WORKDIR /testimonial-app
COPY requirements.txt /testimonial-app/
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install vim -y --no-install-recommends
COPY . .


