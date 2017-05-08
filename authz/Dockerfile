FROM tiangolo/uwsgi-nginx

ADD uwsgi.ini /app/uwsgi.ini
ADD requirements.txt /app/requirements.txt
ADD authz.py /app/authz.py
RUN cd /app && pip install -r requirements.txt
RUN mkdir /app/socket

