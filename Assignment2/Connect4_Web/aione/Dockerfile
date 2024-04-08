FROM python:3.7-alpine
WORKDIR /code
RUN pip install flask
RUN pip install requests
EXPOSE 1234
COPY . .
CMD ["python3", "aione.py"]