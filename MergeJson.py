#!/usr/bin/python
#Usage: merge json files
#Will return the MergeVersion.json file
#Author: Yuting Zhang
''' move this python file into the same folder 
    with those json files, which need to be merged.
    outfile named as the first parameter'''

import json
import os
import sys

#open and load json file
def open_file(filename):
    with open (filename, 'r') as f:
        aa = json.load(f)
    f.close()
    return aa
    #print len(aa)

#Given two dicts, merge them into a new dict as a shallow copy.
def merge_dict(dict1, dict2):
    z = dict1.copy()
    z.update(dict2)
    #print len(z)
    return z

#Save as Json file
def save_json(data, name ):
    print len(data)
    with open(name, 'w') as outfile:
        json.dump(data, outfile)
    outfile.close()

#Get all json files name
def get_filename():
    path_to_json = '.'
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    print "there are",len(json_files),"json files got meraged"
    print json_files
    return json_files

#Main
def main(argv):
    sum= []
    if len(argv) == 1:
        jfilenames = get_filename()
        sum=open_file(jfilenames[0])
        for i in range(2 , len(jfilenames)):
            data=open_file(jfilenames[i])
            sum=merge_dict(sum, data)
        save_json(sum, argv[0])
        print "Done"
    else:
        print "Invalid!! Usage: python MergeJson.py outfile_name.json"


# Start execution here
if __name__ == "__main__":
    main(sys.argv[1:])