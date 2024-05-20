# Convert emoji into text in Python - Converting emoticons or
emojis into text in Python can be done using thedemoji module. It
is used to accurately remove and replace emojis in text strings

pip install demoji

import demoji
demoji.download_codes()
def replace_emojis_with_text(text):
    return demoji.replace(text, lambda x: f":{demoji.replace_with_desc(x)}:")

# Example text containing emojis
text_with_emojis = "Hello! 🌍😊👍"
text_with_descriptions = replace_emojis_with_text(text_with_emojis)
print(text_with_descriptions)
