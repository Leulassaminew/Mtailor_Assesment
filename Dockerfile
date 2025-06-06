FROM python:3.12-bookworm
RUN apt-get update && apt-get install dumb-init
RUN update-ca-certificates

COPY . .

RUN pip install -r requirements.txt



EXPOSE 8192
CMD ["dumb-init", "--", "fastapi", "run", "app.py", "--port", "8192"]