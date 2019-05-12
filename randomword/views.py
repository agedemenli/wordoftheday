from django.http import HttpResponse, JsonResponse
from datetime import date
from .dictionaries import dic_eng, dic_tr

# This is my random generator function. You can change it for another random formula.
# Takes the variables of the current date and the number of the words as parameter.
# Returns a, so called, random number between 0 and (mod-1) including
def get_random_by_date(year, month, day, mod):
    return (year ** 2 + month ** 3 + day ** 4) % mod

# This function takes a parameter, language code.
# It returns a list of two lists, one for the words, one for the definitions.
# It takes the words and definitions from a local file.
def get_words_and_definitions(lang):
    if lang == 'en':
        return [dic_eng.words_en, dic_eng.definitions_en]
    elif lang == 'tr':
        return [dic_tr.words_tr, dic_tr.definitions_tr]
    else:
        return [[], []]

# This is the main view of my Django app.
# It takes the language code as parameter.
# Returns the word of the day with its meaning in JSON format.
# Returns an Http Response that 'NO SUCH LANGUAGE AVAILABLE' if the language is invalid.
# Splits the date as day, month and year and sends them as random parameters.
# I used date because the random function must return the same random number in one day.
# Because it's the word of the 'day'.
def index(request, lang):
    words = get_words_and_definitions(lang)[0]
    definitions = get_words_and_definitions(lang)[1]
    if len(words) == 0:
        return HttpResponse('NO SUCH LANGUAGE AVAILABLE')
    today = str(date.today())
    year = int(today.split('-')[0])
    month = int(today.split('-')[1])
    day = int(today.split('-')[2])
    word_number = get_random_by_date(year, month, day, len(words))
    return JsonResponse({
        'word': words[word_number],
        'definition': definitions[word_number],
    })
    