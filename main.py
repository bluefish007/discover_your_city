import sys
import datetime
from functions import *
import data

history_list = load_history_list()

# if calc_subdistricts_left(history_list) <= 3:  # If less than x subdistricts left -> the game is over!
#     send_email(subject="",
#                name=data.PLAYER[0]['name'],
#                email=data.PLAYER[0]['name'],
#                message="Game over! Weniger als drei Subdistrikte verbleiben!")
#     raise Exception('Game over! Too less subdistricts left!')
#
# if len(sys.argv) > 1:
#     distance = sys.argv[1]  # first argument from command
# else:
#     distance = data.distance  # backup argument from data.py
#
# winner_district_dict = draw_a_winner_district(distance, history_list)
# winner_name_dict = draw_a_winner_name(history_list)
#
# # print('Bezirk: {winner_district_dict["name"]}')
# # print(f'Sub-Bezirke: {', '.join(winner_district_dict["subdistrict"])}')
# print(f'(Winner: {winner_name_dict["name"]} - {winner_name_dict["mail"]})')
#
#
# send_mail_to_winner(winner_name_dict, winner_district_dict)
#
# status, winner_subdistrict = check_winner_feedback(winner_name_dict, winner_district_dict)
#
# if status == 1:
#     with open("history.txt", "a") as f:
#         f.write(f"{datetime.date.today()} , {winner_name_dict['name']} , {winner_district_dict['name']} , {winner_subdistrict}\n")
#
#     send_email(subject=f"Discover your City - {winner_subdistrict} in {winner_district_dict['name']} wurde eingetragen!",
#                name=winner_name_dict['name'],
#                email=winner_name_dict['mail'],
#                message=f"Danke für die Antwort! {winner_subdistrict} im Bezirk {winner_district_dict['name']} wurde eingetragen! Viel Spaß und einen schönen Ausflug!")
#
# elif status == 2:
#     send_email(subject="Discover your City - Zeit abgelaufen oder Antwort falsch!",
#                name=winner_name_dict['name'],
#                email=winner_name_dict['mail'],
#                message="Die Zeit ist abgelaufen oder die Antwort war falsch!")
#
# elif status == 3:
#     send_email(subject=f"Discover your City - Antwort '{winner_subdistrict}' falsch!",
#                name=winner_name_dict['name'],
#                email=winner_name_dict['mail'],
#                message=f"Die erhaltene Antwort '{winner_subdistrict}' ist leider nicht plausibel und nicht Teil der Antwortmöglichkeiten: {winner_district_dict['subdistrict']}!")
#
