import webbrowser, sys

# Check if command line arguments wer epassed
if len(sys.argv) > 1:
    # ['webscrapery.py', '870', 'Valencia', 'St'.] we want to grab the arguments address into one string
    address = '+'.join(sys.argv[1:])

    # use webbrowser to open the full URL
    webbrowser.open('https://www.google.com/maps/place/' + address)
