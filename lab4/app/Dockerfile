FROM python:3.10-slim

WORKDIR /otp/app

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "-m", "gunicorn", "-b", "0.0.0.0:3000", "-w", "4", "app:app"]