# wordlists

Utilities to download word lists in Python.

## Usage

```py
from wordlists import update_lists, read_words


# Update the word lists from the web
update_lists()

# Get the words from a list
words = read_words("dwyl_alpha")

# Filter words which are 27 characters
words = [w for w in words if len(w) == 27]

# Print the words
print(words)  # ['electroencephalographically', 'hydroxydesoxycorticosterone', 'microspectrophotometrically']
```
