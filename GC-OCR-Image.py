import os

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    of = open(path + ".txt", 'w')

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    of.write('Texts:' + '\n')

    for text in texts:
        of.write('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
            for vertex in text.bounding_poly.vertices])

        of.write('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))

inputdir = "../LinearA/000-Manage-Images/000 - GORILA"
for subdir, dirs, files in os.walk(inputdir):
    for file in files:
        if file[-3:] != "jpg":
            continue
        path = subdir + os.sep + file
        print(path)
        detect_text(path)
        #detect_text('/home/robert/Dev/LinearA/000-Manage-Images/000 - GORILA/GORILA-Vol1-040.jpg')

