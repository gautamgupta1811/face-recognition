def face_Store():
    import cv2
    import numpy as np
    import os

    name = input("Lets begin with your name: ")
    print("Thank you")

    print("Now let's collect some feature of your face")


    current_dir = os.getcwd()
    facesPath = current_dir + '/faces'
    os.chdir(facesPath)

    dataset = cv2.CascadeClassifier('..\data.xml')
    capture = cv2.VideoCapture(0)

    faceData = []

    while True:
        ret,img = capture.read()
        if ret:
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = dataset.detectMultiScale(gray, 1.2)
            # print(faces)
            for x, y, w, h in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

                face = gray[y:y+h, x:x+w]
                face = cv2.resize(face, (50,50))
                # print(face)
                if len(faceData) < 50:
                    faceData.append(face)
                    print(len(faceData))

            cv2.imshow('result',img)
            if cv2.waitKey(1) == 27 or len(faceData) >= 50:
                break
        else:
            print("Camera not working")

    faceData = np.asarray(faceData)
    np.save(name + '.npy',faceData)
    cv2.destroyAllWindows()
    capture.release()
