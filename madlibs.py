stories = {
    "one": {
        "string": "%s is %s",
        "words": ["noun", "adj"]
    },

    "two":  {
        "string": "The %s Dragon is the %s Dragon of all. It has %s, and a %s shaped like a %s. It loves to eat %s, although it will feast on nearly anything. It is %s and %s. You must be %s around it, or you may end up as it`s meal! ",
        "words": ["adjective", "adjective", "noun", "body part", "noun", "food", "adjective", "adjective", "adjective"]
    }
}

def start(story):
    for x in range(len(stories[story]["words"])):
        stories[story]["words"][x] = input(stories[story]["words"][x] + ": ")

    print (stories[story]["string"] % tuple(stories[story]["words"]))

start(input("Would you like story one or story two? Type one for story one and two for story two. "))
