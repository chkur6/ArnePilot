import sys
import json
phantom_file = "/data/phantom.json"

def write_file(status, speed, angle, time):
  status = True if status.lower() == "true" else False
  with open(phantom_file, "w") as phantom:
    json.dump({"status": status, "speed": speed, "angle": angle, "time": time}, phantom)

if __name__ == "__main__":
  write_file(str(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))