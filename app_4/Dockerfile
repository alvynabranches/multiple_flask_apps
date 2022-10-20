FROM python:3.10

WORKDIR /app
COPY . .

RUN python3 -m pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

EXPOSE 5000
CMD [ "gunicorn", "-b", "0.0.0.0:5000", "app:app", "--workers=1" ]