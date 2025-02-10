FROM python:3.13-bookworm

WORKDIR /src
COPY /backend .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9999", "--reload"]