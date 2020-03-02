import re    # for regular expressions
from nltk.stem import SnowballStemmer  # PorterStemmer


Dick = {
    "Amount of categories": 1      # amount of categories that would be chosen with max amount of importance numbers
}


class Word:
    def __init__(self, root, frequency):
        self.root = root
        self.frequency = frequency

    def __str__(self):
        string = self.root + " " + str(self.frequency)
        return string

    def __add__(self, other):
        new_frequency = self.frequency + other.frequency
        return Word(self.root, new_frequency)

    def __setattr__(self, name: str, value) -> None:
        super().__setattr__(name, value)

    def __del__(self):
        del self.root
        del self.frequency


class Category:

    def __init__(self, word_dict, filename):
        self.dict = word_dict  # dictionary with keywords(stemmed already) as keys and importance numbers as values
        self.file = filename

    def __str__(self):
        return str(self.file)

    def __setattr__(self, name: str, value) -> None:
        super().__setattr__(name, value)

    def __del__(self):
        del self.dict
        del self.file


def to_lower(roster):
    """Makes all strings of the list lowercase"""

    for index, value in enumerate(roster):
        roster[index] = roster[index].lower()


def to_stem(roster):
    """Is stemming all strings in the list"""

    for i in roster:
        SnowballStemmer("english").stem(i)


def make_objects_list(roster) -> list:
    """Puts each element of the list in a Word object with frequency=1"""
    """Returns a list of Word objects"""

    manuscript = []
    for index, value in enumerate(roster):
        p = Word(value, 1)
        manuscript.append(p)

    return manuscript


def list_to_dict(roster) -> dict:
    """Gets a list of Word objects"""
    """Returns a dict with keys as obj.root and values as obj"""

    manuscript = {}
    for i in roster:
        if i.root in manuscript:
            manuscript[i.root] = manuscript[i.root] + i
        else:
            manuscript[i.root] = i

    return manuscript


def article_to_dictionary(string) -> dict:
    """
    Returns a dictionary of Word.root as keys and Word objects as values

    :param string: the file txt string
    :return: a dictionary of Word.root as keys and Word objects as values
    """

    roster = re.findall(r"[A-Za-z]+_?'?&?-?[a-zA-Z]+_?'?&?-?[a-zA-Z]+", string)   # makes a list of words that we need

    to_lower(roster)  # makes all words lower

    to_stem(roster)  # stemming

    roster = make_objects_list(roster)  # makes Word objects' list

    manuscript = list_to_dict(roster)   # makes a dict with keys as Word.roots and values as same Word objects

    return manuscript


def find_max_dict_value(dictionary) -> str:
    """
    Finds the key of the max int value of the dictionary

    :param dictionary: just dict
    :return: string - the key of dictionary
    """

    if not dictionary:
        return "What a fuck? Dictionary is empty!"

    value = -1
    needed_key = "#"
    for key in dictionary:
        if dictionary[key] > value:
            value = dictionary[key]
            needed_key = key

    assert not needed_key == "#", print("No keys in the dict")

    return needed_key


def make_dict_best_categories_list(dictionary) -> list:
    """
    Returns a list of best categories for a certain dict(made of a txt string by def make_file_keywords)
    For now we just find Dick["Amount of categories"] categories that have maximum amounts of important numbers

    :param dictionary: the dict that has Category objects as keys and amount of important numbers as values
    :return: a list of best categories
    """

    result = []

    for i in range(Dick["Amount of categories"]):
        key = find_max_dict_value(dictionary)
        result.append(key)
        del(dictionary[key])

    return result


def find_text_best_categories(txt_string, categories_list) -> list:
    """
    Counts the overall amount of importance numbers for a txt file with the filepath
    This amount is increased, when a keywords appear in the text, by the importance number of the keyword

    :param txt_string: the string of the txt file
    :param categories_list: the list of Category objects
    :return: a Txt object
    """

    file_words_dict = article_to_dictionary(txt_string)
    txt_dict = {}

    for category_obj in categories_list:
        amount = 0

        for root in category_obj.dict:
            try:
                assert float(category_obj.dict[root]), "Wow!!!"
                assert int(file_words_dict[root].frequency), "Wow!!!"

                amount += file_words_dict[root].frequency * category_obj.dict[root]
                # amount of the keyword in the txt file is multiplied by this keyword's importance number and added
            except KeyError:
                pass

        txt_dict[category_obj] = amount

    best_category = make_dict_best_categories_list(txt_dict)

    return best_category


text = "about efiafelkiafjkdjka about adfilajklijkla was;was"
cat_list = [Category({"fact": 3, "about": 5}, "Kanzas"), Category({"the": 1, "was": 2}, "Zatmenie")]

for category in find_text_best_categories(text, cat_list):
    print(category, end=' ')
