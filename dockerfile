FROM python:3.9

WORKDIR /app

COPY ./requirement.txt /code/requirement.txt

RUN pip install --no-cache-dir --upgrade -r requirement.txt
RUN pip install fastapi unicorn
COPY ./ /code/app

ENTRYPOINT [ "unicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80" ]
