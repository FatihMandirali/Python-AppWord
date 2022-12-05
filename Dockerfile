FROM python:3

WORKDIR /app

RUN pip install Flask
RUN pip install beautifulsoup4
RUN pip install requests

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
