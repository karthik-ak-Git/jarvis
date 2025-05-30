import eel

eel.init('www')

# Use Eel's built-in functionality to launch the app in Edge
# The 'edge' mode will launch Edge in app mode
eel.start('index.html', mode='edge', host='localhost', port=8000, block=True)
