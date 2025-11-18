FROM python:3.11

WORKDIR /serviceUsers

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY users.py .

EXPOSE 8000

CMD ["python", "users.py"]
