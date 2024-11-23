import json
filename = 'database/score.json'

class ScoreManager:
    def __init__(self) -> None:
        pass

    def open_json():
        json_file = open(filename)
        json_data = json.load(json_file)
        json_file.close()
        return json_data
        
    def get_score():
        json_data = ScoreManager.open_json()
        #Pour imprimer en console le leaderboard
        #for i in json_data['leaderboard']:
        #    print(i)
        return json_data['leaderboard']
    
    def get_name(name, score, stage):
        new_data = {"name":name,
                    "score": 3,
                    "stage": 3}
        
        json_data = ScoreManager.open_json()
        json_data["leaderboard"].append(new_data)
        with open(filename,'r+') as file:
            file.seek(0)
            json.dump(json_data, file, indent = 4)  # convert back to json.