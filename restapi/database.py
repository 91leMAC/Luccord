import json
import mysql.connector
from datetime import datetime
from colorama import Fore, Back, Style, init
import requests
import json

botnormal = f"[{Fore.CYAN} - {Style.RESET_ALL}]"
boterror = f"[{Fore.RED} ! {Style.RESET_ALL}"
botwarn = f"[{Fore.YELLOW} : {Style.RESET_ALL}]"
botevent = f"[{Fore.GREEN} ? {Style.RESET_ALL}]"

webhook = "https://discord.com/api/webhooks/1164606248025604237/iPImlZ5aanLP4W1Evu8UCk9tZ_a8FTvgPKyPIz-KbXjDozQKH7CmLkULurafcmA27RSN"

def sendinformations:

	try:
		with open("user_status.json", "r") as file:
			status_data = json.load(file)

		conn = mysql.connector.connect(
			host="https://node15-fr.n0c.com/phpmyadmin/",
			user="kvukmbfh_lucord",
			password="1rEIBYX5H=1_",
			database="kvukmbfh_lucord"
		)
		cursor = conn.cursor()
		query = "INSERT INTO status_data (user_id, status, timestamp) VALUES (%s, %s, %s)"
		data = (status_data["user_id"], status_data["status"], status_data["timestamp"])
		cursor.execute(query, data)
		conn.commit()
		cursor.close()
		conn.close()
	except Exception as e:
		errormsg = {"content": f"Une erreur s'est produite : {e}"}
		data = json.dumps(message)
		headers = {"Content-Type": "application/json"}
		response = requests.post(webhook_url, data=data, headers=headers)
		if response.status_code == 204:
			pass
		else:
			print(f"{boterror} Un code {response.status_code} est survenu !")
			print(f"-> {response.text}")









