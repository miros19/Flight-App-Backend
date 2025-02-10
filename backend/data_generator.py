class DataGenerator():
    
    def __init__(self):
        self.planes = {"AAAA":[0,0],"AAAB":[1,0],"AAAC":[2,0],"AAAD":[3,0],"AAAE":[4,0],"AAAF":[5,0],"AAAG":[6,0],"AAAH":[7,0],"AAAI":[8,0],"AAAJ":[9,0]}
        self.data = [800, 0.0, 0.2864788975654116, 9000]
        
    
    def generate_frames(self):
        frames = []
        for plane, data in self.planes.items():
            frames.append(self._generate_frame(plane, data))
        return frames
            
    def _generate_frame(self, plane, data):
        data[0] += self.data[1]
        data[1] += self.data[2]
        frame = {
            "icao": plane,
            "speed": self.data[0],
            "lat": data[0],
            "lon": data[1],
            "alt": self.data[3]
        }
        return frame