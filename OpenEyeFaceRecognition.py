import face_recognition

image = face_recognition.load_image_file("Cayden_Pierce.jpg")

list_of_face_encodings = face_recognition.face_encodings(image)

print(list_of_face_encodings[0])
