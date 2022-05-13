import random
import smtplib
import time
from email.message import EmailMessage
from data_city import city_districts
from retrieve_emails import retrieve_emails
import data

MAIL_ADDRESS = data.MAIL_ADDRESS
MAIL_PASSWORD = data.MAIL_PASSWORD
IMAP_SERVER = data.IMAP_SERVER
PLAYER = data.PLAYER


def load_history_list():
    h_list = []
    try:
        with open("history.txt", "r") as f:
            print("History.txt loaded")
            print(f.read())
            for line in f:
                line_list = line.rstrip('\n').split(" , ")
                h_list.append(line_list)
    except FileNotFoundError:
        with open("history.txt", "w") as f:
            pass
    print(f"returning {h_list}")
    return h_list


def last_winner_to_exclude(history_list):
    """ Check if the last 2 times was the same winner, if true then exclude.
    :return: name or False """
    if len(history_list) > 1:
        winner_last_time = history_list[-1][1]
        winner_second_last_time = history_list[-2][1]
        if winner_last_time == winner_second_last_time:
            return winner_last_time
        else:
            return False
    else:
        return False


def draw_a_winner_name(history_list):
    """ Draw a winner name
    :return: dict with winner name and mail """
    exclude_name = last_winner_to_exclude(history_list)  # exclude name if he/she was last two times the winner

    while True:
        winner_name = random.choice(PLAYER)
        if winner_name["name"] != exclude_name:
            return winner_name


def draw_a_winner_district(distance, history_list):
    """ Draw a winner district. Match with selected distance, remove district_exclude and remove
    all already won sub-districts.
    :return: dict """
    if len(history_list) > 0:
        exclude_district = history_list[-1][2]  # last name of district in history.txt
    else:
        exclude_district = None

    while True:
        possible_districts = []
        for district in city_districts:
            if district["distance"] == distance and district["name"] != exclude_district:
                possible_districts.append(district)

        winner_district = random.choice(possible_districts)
        winner_district_name = winner_district["name"]

        # remove sub-districts:
        for line in history_list:
            if line[2] == winner_district_name:
                winner_district["subdistrict"].remove(line[3])

        if len(winner_district["subdistrict"]) > 0:
            return winner_district


def calc_subdistricts_left(history_list):
    count_all = 0
    for line in city_districts:
        count_all += len(line["subdistrict"])
    count_winners = len(history_list)
    return count_all - count_winners


def send_mail_to_winner(winner_name, winner_district):
    msg = EmailMessage()
    msg["Subject"] = "Discover your City - Du hast gewonnen!"
    msg["From"] = f"Discover your City <{MAIL_ADDRESS}>"
    msg["To"] = f"{winner_name['name']} <{winner_name['mail']}>"
    msg.set_content(f'Gewonnen hat folgender Bezirk: {winner_district["name"]}. Zur Auswahl stehen folgende '
                    f'Sub-Bezirke: {", ".join(winner_district["subdistrict"])}. Bitte auf diese Mail mit dem '
                    f'ausgewählten Sub-Bezirk antworten.')

    msg.add_alternative(f"""
    <!DOCTYPE html>
    <html>
        <body>
            <h2>Discover your City - Du hast gewonnen!</h2>
            <p>Gewonnen hat folgender Bezirk: <br>
            <strong>{winner_district["name"]}</strong><p>
            <p>Zur Auswahl stehen folgende Sub-Bezirke: <br>
            <strong>{', '.join(winner_district["subdistrict"])}</strong></p>
            <p style="color:red;">Bitte auf diese Mail mit dem ausgewählten Sub-Bezirk antworten.</p>
            <img src='https://localpedia.de/wp-content/uploads/2017/03/berlin-stadtteile-bs-139151414.png' width='800'>
        </body>
    </html>
    """, subtype="html")

    with smtplib.SMTP_SSL(IMAP_SERVER) as smtp:
        smtp.login(user=MAIL_ADDRESS, password=MAIL_PASSWORD)
        smtp.send_message(msg)


def send_email(subject, name, email, message):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = f"Discover your City <{MAIL_ADDRESS}>"
    msg["To"] = f"{name} <{email}>"
    msg.set_content(f"{message}")

    msg.add_alternative(f"""\
    <!DOCTYPE html>
    <html>
        <body>
            <p>{message}</p>
        </body>
    </html>
    """, subtype="html")

    with smtplib.SMTP_SSL(IMAP_SERVER) as smtp:
        smtp.login(user=MAIL_ADDRESS, password=MAIL_PASSWORD)
        smtp.send_message(msg)


def check_winner_feedback(winner_name_dict, winner_district_dict):
    count = 0
    winner_subdistrict = ""
    while count < 180:
        mail_from, mail_text = retrieve_emails()

        if winner_name_dict['mail'] in str(mail_from) and mail_text is not False:
            winner_subdistrict = mail_text
            break
        else:
            count += 1
            time.sleep(10)

    if winner_subdistrict in winner_district_dict["subdistrict"]:
        return 1, winner_subdistrict
    elif winner_subdistrict == "":
        return 2, "Zeit ist abgelaufen"
    else:
        return 3, winner_subdistrict   # Answer is not plausible / not one of the subdistricts
