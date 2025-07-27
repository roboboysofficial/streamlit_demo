FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir streamlit numpy pandas matplotlib
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
