from python:3.10.12

RUN apt-get update

WORKDIR cars_manager
COPY . /cars_manager/

RUN pip install --no-cache -r requirements.txt

ENV PYTHONUNBUFFERED=1
EXPOSE 8000

ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]