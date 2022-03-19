import imaplib
import email
from email.header import decode_header, make_header
import data

MAIL_ADDRESS = data.MAIL_ADDRESS
MAIL_PASSWORD = data.MAIL_PASSWORD
IMAP_SERVER = data.IMAP_SERVER


def retrieve_emails():
    """ Retrieve email and return "Status" (True/False) and first line of the retrieved mail. """

    imap = imaplib.IMAP4_SSL(IMAP_SERVER)
    imap.login(MAIL_ADDRESS, MAIL_PASSWORD)
    imap.list()
    imap.select('inbox')

    ret_code, messages = imap.search(None, 'UNSEEN')
    if ret_code != 'OK':
        return False, False

    for num in messages[0].split():
        typ, data = imap.fetch(num, '(RFC822)')

        n = 0
        for response in data:
            if isinstance(response, tuple):
                break
            n += 1
        msg = email.message_from_bytes(data[n][1])

        email_from = str(make_header(decode_header(msg['From'])))

        text_plain = False
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                text_plain = part.get_payload(decode=True).decode().strip()
                text_plain = text_plain.replace("\r", "").replace("*", "").split("\n")[0].strip()  # First line in the Mail

        return email_from, text_plain

    return False, False
