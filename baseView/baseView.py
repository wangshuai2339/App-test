class BaseView(object):
    def __init__(self,dirver):
        self.dirver=dirver

    def find_element(self,*loc):
        self.dirver.implicitly_wait(50)
        return self.dirver.find_element(*loc)

    def find_elements(self,*loc):
        self.dirver.implicitly_wait(50)
        return self.dirver.find_elements(*loc)

    def get_window_size(self):
        return self.dirver.get_window_size()

    def swipe(self,start_x,start_y,end_x,end_y,duration):
        return self.dirver.swipe(start_x,start_y,end_x,end_y,duration)

