import cv2

def img():
    image = cv2.imread('variant-2.jpg')
    blurred = cv2.GaussianBlur(image, (7, 7), 0)


def tracking():
    cap = cv2.VideoCapture(1)
    fly = cv2.imread('fly64.png')

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)  # Размытие

        # Применить пороговое значение для бинаризации изображения
        ret, threshold = cv2.threshold(gray, threshold_value, 255,
                                       cv2.THRESH_BINARY)
        # Найти контуры на изображении
        contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)
        # Отобразить контуры на изображении
        cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

        largest_contour = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(largest_contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        if iterations == 5:
            center_x = int(x + w / 2)
            center_y = int(y + h / 2)
            print(f"Координаты метки: ({center_x}, {center_y})")
            # Записать координаты метки в файл
            f.write(f"Координаты метки: ({center_x}, {center_y})n")
            iterations = 0

        # Отобразить фрейм
        cv2.imshow("Video", frame)

        # Ожидание нажатия клавиши "q" для выхода из программы
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        iterations += 1
    cap.release()
    cv2.destroyAllWindows()
