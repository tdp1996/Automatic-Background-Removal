FROM python:3.9

LABEL Name=automaticbackgroundremoval Version=0.0.1

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD [ "streamlit", "run", "main.py" ]

EXPOSE 8502
