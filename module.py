import configparser
import re
class Tester:
    def __init__(self, text):
        self.text = text

    def test(self):
        parsed = []
        config = configparser.ConfigParser()
        config.read("config.ini")
        path_to_dictionary = config.get("dictionary_path", "path")

        with open(path_to_dictionary, "r") as file:
            bad_phrases = [re.escape(phrase.strip()) for phrase in file.readlines()]

        try:
            regex = r"\b(" + "|".join(bad_phrases) + r")\b"
            result = re.sub(regex, lambda m: "*" * len(m.group()), self.text, flags=re.IGNORECASE)
            return result
        except Exception as e:
            print("Ошибка:", e)