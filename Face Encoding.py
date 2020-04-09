import PIL.Image
import PIL.ImageDraw
import face_recognition
import PIL.ImageFont
import os
import pickle

## Requirements
font = PIL.ImageFont.truetype("arial.ttf", 15)
dir = os.getcwd()
people = dict()

train_dir = dir + '/people/'
for person in os.listdir(train_dir):
    name = person.replace('.jpg','')
    print(train_dir)
    print(person)
    image = face_recognition.load_image_file(train_dir + person)
    face_locations = face_recognition.face_locations(image) # for test
    face_encodings = face_recognition.face_encodings(image)
    if len(face_encodings) == 0:
        print("No faces were found.")
    else:
        people[name] = face_encodings[0] # There must be only one person in each photo since it is learning mode

print(people)

# Pickling (serializing) a dictionary into a file
with open('output.pickle', 'wb') as filename:
    pickle.dump(people, filename)
'''
face_img = PIL.Image.fromarray(image)
draw = PIL.ImageDraw.Draw(face_img)
for face in face_locations:
    draw.rectangle(face,outline="red",width=2)
    draw.text((face[0],face[1]), "Name",font=font)
face_img.show()
'''