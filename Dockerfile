FROM python:2.7.10

RUN pip install web.py

COPY serve.py /
RUN chmod +x /serve.py

CMD /serve.py
