def face_detect():
    import cv2
    import os
    import numpy as np



    # changing directory for loading face data
    current_dir = os.getcwd()
    facesPath = current_dir + '/faces'
    os.chdir(facesPath)
    facesList = os.listdir()

    # Merging face data
    faces_arr= []
    for i in range(len(facesList)):
        face = np.load(facesList[i])
        face = face.reshape(face.shape[0],-1)
        faces_arr.append(face)
    faces_arr = np.asarray(faces_arr)
    faces_arr = np.vstack(faces_arr)

    # Finding User Name (name to be printed)
    userName = {}
    for i in range (len(facesList)):
        name = facesList[i].split(".")[0]
        userName[i] = name

    # Making Labels for finding closest match
    labels = np.zeros((faces_arr.shape[0],1))

    # Dynamically defining values of Labels
    n = len(faces_arr) // len(facesList)
    for i in range(len(facesList)):
        labels[i*n:,:] = i

    # Finding distance from every element in data with input
    def distance(x1, x2):
        return np.sqrt(sum((x1-x2)**2))

    # Defining input, Data and appending data in list
    def knn(x, train, k = 5):
        d =[]
        n = train.shape[0]
        for i in range (n):
            d.append(distance(x, train[i]))
        d = np.array(d)
        indexes = np.argsort(d)

    # Selecting value for maximum data match
        sortedLabels = labels[indexes][:k]
        count = np.unique(sortedLabels, return_counts = True )
        return count[0][np.argmax(count[1])]



    # Providing facial data
    dataset = cv2.CascadeClassifier('..\data.xml')
    capture = cv2.VideoCapture(0)

    # Opening Camera
    font = cv2.FONT_HERSHEY_COMPLEX

    while True:
        ret, img = capture.read()
        if ret:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = dataset.detectMultiScale(gray, 1.5)
            for x, y, w, h in faces:
                face = gray[y:y + h, x:x + w]
                face = cv2.resize(face, (50, 50)).flatten()
                label = knn(face, faces_arr)
                name = userName[int(label)]
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
                cv2.putText(img, name, (x, y), font, 1, (255, 0, 0), 2)

            cv2.imshow('result', img)

     #Closing Camera
            if cv2.waitKey(1) == 27:
                break
        else:
            print("Camera not working")

    cv2.destroyAllWindows()
    capture.release()