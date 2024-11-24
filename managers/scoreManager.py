import json

class ScoreManager:
    def __init__(self) -> None:
        self.filename = 'database/score.json'

    def getAllData(self):
        json_file = open(self.filename)
        json_data = json.load(json_file)
        json_file.close()
        return json_data
        
    def get_score(self):
        json_data = self.getAllData()
        #Pour imprimer en console le leaderboard
        #for i in json_data['leaderboard']:
        #    print(i)
        return json_data['leaderboard']
    
    def addScore(self, name, score, stage):
        new_data = {"name":name,
                    "score": score,
                    "stage": stage}
        
        json_data = self.getAllData()
        json_data["leaderboard"].append(new_data)
        with open(self.filename,'r+') as file:
            file.seek(0)
            json.dump(json_data, file, indent = 4)  # convert back to json.
        