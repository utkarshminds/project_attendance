FROM python:3

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8051

CMD ["streamlit", "run", "main.py"]