import logging
from datetime import datetime
from celery import shared_task
from django.core.mail import EmailMessage
from nda.settings import EMAIL_HOST_USER, RECIPIENT_EMAIL
from nda_email.temporary_storage import temporary_storage

logger = logging.getLogger(__name__)

@shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={'max_retries': 5, 'countdown': 60})
def send_emails_task(self, html_message_for_nda, html_message_for_customer, customer_email, file_name):
    logger.info("send_emails_task started")  # Logging начала задачи
    logger.info(f"html_message_for_nda: {html_message_for_nda}")
    logger.info(f"html_message_for_customer: {html_message_for_customer}")
    logger.info(f"customer_email: {customer_email}")
    logger.info(f"file_name: {file_name}")

    subject_for_nda = f'Заказ с сайта от {datetime.now().strftime("%Y-%m-%d %H:%M.")}'
    logger.info(f"subject_for_nda: {subject_for_nda}")
    email_for_nda = EmailMessage(subject_for_nda,
                                    html_message_for_nda, EMAIL_HOST_USER, [RECIPIENT_EMAIL])
    logger.info(f"email_for_nda created")
    subject_for_customer = f'Ваш заказ от {datetime.now().strftime("%Y-%m-%d %H:%M.")}'
    logger.info(f"subject_for_customer: {subject_for_customer}")
    email_for_customer = EmailMessage(subject_for_customer,
                                        html_message_for_customer, EMAIL_HOST_USER, [customer_email])
    logger.info(f"email_for_customer created")

    try:
        if file_name is not None:
            logger.info(f"Attaching file: {file_name}")
            storaged_file_path = temporary_storage.path(file_name)
            logger.info(f"storaged_file_path: {storaged_file_path}")
            email_for_nda.attach_file(storaged_file_path)
            email_for_customer.attach_file(storaged_file_path)
            temporary_storage.delete(file_name)
            logger.info("File attached and deleted")

        logger.info("Sending email_for_nda")
        email_for_nda.send(fail_silently=False)
        logger.info("email_for_nda sent successfully")

        logger.info("Sending email_for_customer")
        email_for_customer.send(fail_silently=False)
        logger.info("email_for_customer sent successfully")
        logger.info(f"Successfully sent emails to {customer_email} and {RECIPIENT_EMAIL}")

    except Exception as e:
        logger.error(f"Failed to send emails. Error: {e}", exc_info=True)
        raise  # Allow Celery to retry

    logger.info("send_emails_task completed")
