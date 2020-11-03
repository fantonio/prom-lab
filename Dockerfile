FROM aluracursos/api-django:1.0
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install django-prometheus
COPY ./api-django/requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000