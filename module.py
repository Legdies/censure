class Tester:
    def __init__(self, text):
        self.text = text

    def test(self):
        parsing = self.text.split()
        parsed = []

        with open("dictionary.txt", "r") as file:

            words = file.read().split()


        cleaned_words = set()
        for word in words:
            cleaned_word = ''.join(filter(str.isalnum, word))
            cleaned_words.add(cleaned_word.lower())

        try:
            for word in parsing:
                if word.lower() == "stink" or word.lower() in cleaned_words:
                    parsed.append("#####")
                else:
                    parsed.append(word)
            result = " ".join(parsed)
            print(result)
        except Exception as e:
            print("Ошибка:", e)