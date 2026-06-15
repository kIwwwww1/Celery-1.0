import random
import string

from shop_app.tasks import send_email_newsletter


def fetch_users_ids():
    return [random.randint(1, 100) for _ in range(random.randint(20, 50))]


def send_newsletters_task():
    user_ids = fetch_users_ids()
    promo_code = "".join(random.choices(string.ascii_letters, k=5))
    result = send_email_newsletter.delay(
        user_ids=user_ids,
        sale_id=random.randint(50, 200),
        promocode=promo_code,
    )

    print("send task", result, repr(result))
