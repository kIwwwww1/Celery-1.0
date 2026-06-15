from celery import Celery

app = Celery(
    "shop_app.celery_app",
    broker="amqp://guest:guest@localhost:5672//",
    backend="rpc://",
)
