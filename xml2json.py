import json
import xmltodict
import sys
import os

def get_args():
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        print("expected an xml file as an arg!")
        exit(1)
    return fname


def read_in_xml(fname):
    print(f"trying to open {fname}...")
    with open(fname) as f:
        res = xmltodict.parse(f.read())
    return res


def convert_2_json(map):
    print("converting to json...")
    obj = json.dumps(map)
    return obj


def save_json(obj, fname):
    new_file = "".join(os.path.splitext(fname)[0]) + ".json"
    print(f"writing {new_file} to disk...")
    with open(new_file, "w") as f:
        f.write(obj)


def main():
    fname = get_args()
    obj = read_in_xml(fname)
    json_data = convert_2_json(obj)
    save_json(json_data, fname)
    print("complete")
    exit(0)

if __name__ == "__main__":
    main()
