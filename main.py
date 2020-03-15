import json
import sys, os
import time

from helpers import clean_folder, get_api, write_json, file_exists, directory_exists, dd


def get_by_hash_tag(hash_tag, since="2014-07-12"):
    # build directory for hashtag data if it is not already there
    dir_path = os.path.join(os.getcwd(), "#{}".format(hash_tag))
    if not directory_exists(dir_path):
        os.mkdir(dir_path)
    print(dir_path)
    clean_folder(dir_path)
    api = get_api()
    raw_query = "q=%23{}&count=100&include_entities=true&result_type=recent&since={}".format(hash_tag, since)
    results = api.GetSearch(raw_query=raw_query, return_json=True)
    i = 1
    filepath = os.path.join(dir_path, str(i) + "_" + "out.json")

    print(json.dumps(results,indent=2))
    write_json(filepath, json.dumps(results, indent=2))
    while True:
        i += 1
        # time.sleep(30)
        if results['search_metadata'] and 'next_results' in results['search_metadata']:
            results = api.GetSearch(
                raw_query=results['search_metadata']['next_results'][1:],
                return_json=True
            )
            print(json.dumps(results, indent=2))
            filepath = os.path.join(dir_path, str(i) + "_" + "out.json")
            write_json(filepath, json.dumps(results, indent=2))
        else:
            break


if __name__ == '__main__':
    get_by_hash_tag(hash_tag="کرونا")
