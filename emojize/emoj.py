import emoji

def string_to_emoji(e_name):
    e_name = f":{e_name}:"
    return emoji.emojize(e_name)
