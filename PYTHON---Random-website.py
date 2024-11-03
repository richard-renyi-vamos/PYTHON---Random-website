import webbrowser
import random

# List of popular or interesting websites
websites = [
    "https://www.wikipedia.org",   # Wikipedia
    "https://www.reddit.com",      # Reddit
    "https://www.nytimes.com",     # New York Times
    "https://www.bbc.com",         # BBC
    "https://www.youtube.com",     # YouTube
    "https://www.github.com",      # GitHub
    "https://www.stackoverflow.com", # Stack Overflow
    "https://www.medium.com",      # Medium
    "https://www.imdb.com",        # IMDb
    "https://www.ted.com",         # TED Talks
]

# Open a random website
random_website = random.choice(websites)
webbrowser.open(random_website)

print(f"Opening: {random_website}")
