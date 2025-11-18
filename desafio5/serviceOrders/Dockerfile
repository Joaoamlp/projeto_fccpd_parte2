FROM python:3.11

WORKDIR /serviceOrders

COPY requirements.txt .
RUN pip install -r requirements.txt 

COPY orders.py .

EXPOSE 8001

CMD ["python", "orders.py"]
