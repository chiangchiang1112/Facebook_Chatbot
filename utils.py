import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAb6Na9tWuIBAAAZCBDSnK4up0ex1hINXn9ghdLRKm3O48NelHemkh9py5Xp2Ae4WVRZBIOhESo4lZCKbnZBFaZAtLw3ZBUfC573sDnm3lnOY9RfHVydp1wCerIw8fUcTsEYZAbpLtnTuvPRcaxQYHFUQiVFxi142q5BtFHcCZCpHwZDZD"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response



def send_image_url(id, img_url):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {
            "attachment":{
                "type":"image",
                "payload":{
                    "url":img_url,
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

"""
def send_button_message(id, text, buttons):
    pass
"""
