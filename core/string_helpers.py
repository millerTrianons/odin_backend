import re


def clean_text(text: str) -> str:
    # Regex to find emojis and special symbols
    emoji_pattern = re.compile(
        '['
        '\U0001F600-\U0001F64F'  # Emoticons
        '\U0001F300-\U0001F5FF'  # Symbols & pictograms
        '\U0001F680-\U0001F6FF'  # Transport & maps
        '\U0001F700-\U0001F77F'  # Alchemical symbols
        '\U0001F780-\U0001F7FF'  # Geometric shapes
        '\U0001F800-\U0001F8FF'  # Additional symbols
        '\U0001F900-\U0001F9FF'  # Additional emojis
        '\U0001FA00-\U0001FA6F'  # Additional emojis
        '\U00002702-\U000027B0'  # Miscellaneous symbols
        '\U000024C2-\U0001F251'  # Miscellaneous symbols
        ']+', flags=re.UNICODE)
    
    # Remove emojis
    text = emoji_pattern.sub(r'', text)
    # Replace newlines with spaces
    text = text.replace('\n', ' ')
    return text

