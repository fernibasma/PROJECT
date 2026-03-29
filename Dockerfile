FROM python:3.10
WORkDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
cmd ["python", "-m", "pytest", "tests/"]