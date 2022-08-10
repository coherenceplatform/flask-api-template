FROM python:3.7

WORKDIR /app

#RUN mkdir /nonexistent
#RUN chown nobody:nogroup /nonexistent

#USER nobody:nogroup

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN ln -sf /app/migrate_db.sh /usr/bin/migrate_db.sh
RUN chmod +x entrypoint.sh

#ADD https://www.postgresql.org/media/keys/ACCC4CF8.asc ./
#RUN apt-key add ACCC4CF8.asc

#RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" > /etc/apt/sources.list.d/pgdg.list

RUN DEBIAN=noninteractive apt-get update && apt-get install -y postgresql-client-13


EXPOSE 5000


#RUN chown nobody:nogroup /app
#USER nobody:nogroup

#CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
#CMD ["uwsgi", "--socket", "0.0.0.0:5000", "--protocol=http", "-w", "wsgi:app"]
CMD ["uwsgi", "--socket", "0.0.0.0:5000", "--protocol=http", "--ini", "app.ini"]
#CMD ["./entrypoint.sh"]
#CMD ["uwsgi", "--ini", "app.ini"]
