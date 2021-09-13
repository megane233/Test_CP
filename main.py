# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import json
import emoji


try:
        # téléchargement de la page
        page = requests.get("https://random-data-api.com/api/internet_stuff/random_internet_stuff")

        # print(page.status_code)

        # print(type(page.content))
        # print(page.content)

        content = page.content

        # conversion du contenu de la page en JSON
        my_new_string_value = content.decode("utf-8")

        my_json = json.loads(my_new_string_value)

        emo = None



        if "Windows" in my_json['user_agent']:
                emo = ('\U0001FA9F')
        elif "Mac OS" in my_json['user_agent']:
                emo = emoji.emojize(':red_apple:')
        elif "Linux" in my_json['user_agent']:
                emo = emoji.emojize(':penguin:')
        elif "Android" in my_json['user_agent']:
                emo = emoji.emojize(':robot:')

        print("L'adresse email de l'utilisateur " + my_json['username'] + " est " + my_json[
                'email'] + ". Iel utilise le système d'exploitation " + emo)

except requests.ConnectionError as e:
        print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
        print(str(e))

except requests.Timeout as e:
        print("OOPS!! Timeout Error")
        print(str(e))

except requests.RequestException as e:
        print("OOPS!! General Error")
        print(str(e))

except KeyboardInterrupt:
        print("Someone closed the program")

