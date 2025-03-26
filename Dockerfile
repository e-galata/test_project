FROM python:3.13-slim-bookworm

LABEL "creator"="Yevgeniy Galata"
LABEL "email"="dushirak@gmail.com"

WORKDIR /
VOLUME /allureres
COPY . .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

CMD ["pytest", "-s", "-v", "./api", "./database/tests", "--alluredir=/allureres"]
