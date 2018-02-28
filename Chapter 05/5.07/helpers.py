"""
Code illustration: 5.07

@Tkinter GUI Application Development Blueprints
"""


def get_time_in_minute_seconds(time_in_seconds):
    minutes = int(time_in_seconds / 60)
    seconds = int(time_in_seconds % 60)
    return (minutes, seconds)


def truncate_text(text, truncate_length):
    truncate_length_plus_two = truncate_length + 2  # account for double dots
    return (text[:truncate_length_plus_two] + '..') if len(text) > truncate_length else text
