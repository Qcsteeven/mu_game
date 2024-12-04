import json

class Adapter:
    @classmethod
    def adapt(cls,path = "config.json"):
        with open(path, "r") as rfile:
            data = json.load(rfile)
        height=data["options"]["height"]
        width=data["options"]["width"]
        print(type(width))
        pmap = data["map"]
        count = 0
        counth = 0
        arr = [[]*width for i in range(height)]
        for i in pmap.values():
            if count==width:
                counth+=1
                count=0
            if counth==height:
                break
            arr[counth].append(i)
            print(count)
            count+=1
        return arr

Adapter.adapt()
