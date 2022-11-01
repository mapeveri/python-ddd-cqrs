FROM python:3.9

RUN mkdir -p /var/www/html/marketplace

WORKDIR /var/www/html/marketplace

ENV PYTHONPATH "${PYTHONPATH}:/var/www/html/marketplace/src"

COPY --chown=www-data . /var/www/html/marketplace

RUN ["pip3", "install", "pipenv"]
RUN ["pipenv", "install"]

EXPOSE 5000

CMD ["pipenv", "run", "flask", "run"]
