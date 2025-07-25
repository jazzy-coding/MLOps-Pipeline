FROM python:3.10-slim

WORKDIR /src

COPY /src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "hello.py"]