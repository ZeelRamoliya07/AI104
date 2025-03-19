"""
Create a tokenizer for your own language (mother tongue you speak). The tokenizer should
tokenize punctuations, dates, urls, emails, numbers (in all different forms such as “33.15”,

“3,22,243”, “313/77”), social media usernames/user handles. Use regular expressions to design
this. [Hint: Use unicode blocks for your language, check wikipedia pages]
"""

import re

def gujarati_tokenizer(text):
    # Regular expressions for different token types
    gujarati_words = r'[\u0A80-\u0AFF]+'  # Gujarati script range
    punctuation = r'[\.,!?;:\'\"()\[\]{}…]'  # Punctuation marks
    date_pattern = r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b|\b\d{1,2}(st|nd|rd|th)?\s+[A-Za-z]+\s+\d{2,4}\b'
    url_pattern = r'https?://\S+|www\.\S+'
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    number_pattern = r'\b\d{1,3}(,\d{2,3})*(\.\d+)?\b|\b\d+/\d+\b'
    social_media_pattern = r'[@#][A-Za-z0-9_]+'

    # Combine all regex patterns
    combined_pattern = f'({punctuation}|{date_pattern}|{url_pattern}|{email_pattern}|{number_pattern}|{social_media_pattern}|{gujarati_words})'

    # Tokenize using regex
    tokens = re.findall(combined_pattern, text)

    # Clean up tokens (remove empty strings)
    tokens = [token[0] for token in tokens if token[0]]

    return tokens

# Example Gujarati text with different token types
text = """
હેલો! મારી ઈમેલ test@example.com છે અને મારી વેબસાઈટ https://myblog.com છે.
હું 27-02-2025 ના રોજ જન્મ્યો હતો. મારું ફોન નંબર 987,654,321 છે.
મને ફોલો કરો @my_handle! #Gujarati
"""

# Tokenize the text
tokens = gujarati_tokenizer(text)

# Print the tokens
print(tokens)

