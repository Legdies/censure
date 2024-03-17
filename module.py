import configparser

class Tester:
    def __init__(self, text):
        self.text = text

    def test(self):
        parsed = []
        config = configparser.ConfigParser()
        config.read("config.ini")
        path_to_dictionary = config.get("dictionary_path", "path")

        with open(path_to_dictionary, "r", encoding="utf-8") as file:
            allowed_words = set(word.strip().lower() for word in file)

        try:
            words = self.text.split()
            for word in words:
                if word.lower() in allowed_words:
                    parsed.append(word)
                else:
                    parsed.append("*****")
            result = " ".join(parsed)
            return result
        except Exception as e:
            print("Ошибка:", e)