FROM python:3.11-slim
WORKDIR /django_iyzico_payment
COPY ./requirements.txt /django_iyzico_payment
RUN pip install -r requirements.txt
COPY . .
RUN python3 manage.py collectstatic --noinput

# Start Server
EXPOSE 80
CMD ["gunicorn", "--bind", "0.0.0.0:80", "core.wsgi:application"]