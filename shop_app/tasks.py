import logging
from time import sleep

from shop_app.celery_app import app
from shop_app.smtp_email_backend import SmtpEmailBackend

log = logging.getLogger(__name__)


def fetch_users_info(user_ids: list[int]) -> list[tuple[str, str]]:
    return [
        (f"User {user_id:02d}", f"email.user{user_id:02d}@example.com")
        for user_id in user_ids
    ]


newsletter_body_template = """\
Dear {name},

Our sale just started!
Sale #{sale_id}
Use our promo code: "{promo}"!
"""


@app.task
def send_email_newsletter(
    user_ids: list[int],
    sale_id: int,
    promocode: str,
):
    email_backend = SmtpEmailBackend(
        smtp_server="localhost", smtp_port=1025, from_email="noreply@shop.com"
    )
    users_info = fetch_users_info(user_ids)

    log.info(f"Start sending newsletter #{sale_id} email to {len(user_ids)}")

    for name, email in users_info:
        subject = f"{name}, join our sale #{sale_id}"
        body = newsletter_body_template.format(
            name=name,
            sale_id=sale_id,
            promo=promocode,
        )

        email_backend.send_email(
            recipient=email,
            subject=subject,
            body=body,
        )
        log.info(f"sending email to user {email}")

        # Для демо медленной отправки
        sleep(0.5)

    log.info(f"Finished sending newsletter #{sale_id} email to {len(user_ids)}")


print("HELLO!")
