import cv2 as cv



class camera: 

        def __init__(self) -> None:
            self.camera = cv.VideoCapture(0)
            self.camera.set(cv.CAP_PROP_FRAME_WIDTH, 640)
            self.camera.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
            self.camera.set(cv.CAP_PROP_FPS, 30)
            self.frame = None
            self.running = True
            if not self.camera.isOpened():
                  print("Cannot open camera")

        def __delete__(self):
              self.camera.release
              cv.destroyAllWindows()
              print("Camera closed")

        def get_frame(self):
            if self.camera.isOpened():
                  ret, frame = self.camera.read()

                  if ret:
                        return (ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
                  else:
                        return (ret, None)
            else:
                  return None
            
        
        
        
            

