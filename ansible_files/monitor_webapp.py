import urllib.request
#import pytest
response = urllib.request.urlopen ("http://localhost:5000/")
data = response.read ()
# Asumiendo que la respuesta esperada es "Hello, World!"
assert data == b"Welcome!", "La respuesta no coincide con lo esperado"