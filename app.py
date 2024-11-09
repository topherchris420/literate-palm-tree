import math
import json
import sys

class CymaticPattern:
    def __init__(self, resolution=100):
        self.resolution = resolution
        
    def generate_pattern(self, frequency, amplitude):
        pattern = []
        for y in range(self.resolution):
            row = []
            for x in range(self.resolution):
                # Normalize coordinates to [-2, 2]
                nx = (x / self.resolution) * 4 - 2
                ny = (y / self.resolution) * 4 - 2
                
                # Calculate radius and angle
                r = math.sqrt(nx * nx + ny * ny)
                theta = math.atan2(ny, nx)
                
                # Generate pattern
                val = amplitude * math.sin(2 * math.pi * frequency * r)
                val += amplitude * math.cos(theta * frequency)
                
                # Normalize to [0, 255]
                val = int(((val + 2) / 4) * 255)
                row.append(val)
            pattern.append(row)
        return pattern

def main():
    generator = CymaticPattern()
    while True:
        try:
            line = input()
            if line.strip():
                freq, amp = map(float, line.split(','))
                pattern = generator.generate_pattern(freq, amp)
                print(json.dumps(pattern))
                sys.stdout.flush()
        except EOFError:
            break
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == '__main__':
    main()