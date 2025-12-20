import requests

question_data = []
class GenerateQuestion():
    @staticmethod
    def get_question():
        global question_data

        parameters = {
            "amount" : 10,
            "type"  : "boolean"
        }

        response  = requests.get("https://opentdb.com/api.php", params=parameters)
        response.raise_for_status()

        question_data  = response.json()['results']

GenerateQuestion.get_question()