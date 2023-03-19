FROM python:3.10

WORKDIR /app

RUN apt-get update && \
    apt-get install -y xsel xclip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501
CMD ["streamlit", "run", "src/app.py"]
