FROM python:3.9

RUN mkdir -p /var/www/html/marketplace

WORKDIR /var/www/html/marketplace

COPY --chown=www-data . /var/www/html/marketplace

RUN ["pip3", "install", "pipenv"]
RUN pipenv install

CMD pipenv run python main.py

