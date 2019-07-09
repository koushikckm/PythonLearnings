# Define the chunk Size
# Read the file
mychunk = 1000

# path to your image file
myimagefile = 'D:\\PYTHON\\workspace\\fileIO\\Koushik.jpg'
# Open a dummy file for dumping chunks
dummyfile = open('chunkfile.txt', 'wb+')

with open(myimagefile, 'rb') as fileloop:
    while True:
# Read 1000 byte chunks of the image
        filelines = fileloop.read(mychunk)
        if not filelines: break

  # write to dummy file (This file can be used for data transfer)
        dummyfile.write(filelines)
dummyfile.close()

# Destination
# reconstruct
readdummyfile= open('chunkfile.txt', 'rb')

# Create the jpg file
with open('D:\\PYTHON\\workspace\\fileIO\\Koushik_dump.jpg', 'wb') as tempfile:
    for f in readdummyfile:
        tempfile.write(f)