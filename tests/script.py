import json


def add_ids_to_json(json_data):
    if isinstance(json_data, list):
        for i, item in enumerate(json_data, start=1):
            item["id"] = i
    return json_data

if __name__ == '__main__':
    datafile = r"/home/maxiwere45/PycharmProjects/seriesNet/data/seriesInfos.json"

    with open(datafile, "r") as f:
        data = json.load(f)
        data = add_ids_to_json(data)
        with open(datafile, "w") as f:
            json.dump(data, f, indent=4)
