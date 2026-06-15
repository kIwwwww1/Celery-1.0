from celery import Celery

app = Celery(
    "shop_app.celery_app",
    broker="amqp://guest:guest@localhost:5672//",
    include=["shop_app.tasks"],
    backend="rpc://",
)

app.conf.worker_enable_remote_control = False
