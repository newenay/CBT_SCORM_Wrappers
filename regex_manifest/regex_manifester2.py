#!/usr/bin/env python3
import re, os
# import xml

manifest = "regex_manifest/_resources_imsmanifest.txt"
pattern = r"<file href=\"[\w/.-]+\" />"

if not os.path.exists('regex_manifest/output_file.txt'):
    with open(manifest, 'r') as rf, open('regex_manifest/output_file.txt', 'a') as wf:
        content = rf.read()
        matches = re.findall(pattern, content)
        for match in matches:
            wf.write(match + '\n')
            #if match is None:
                #continue
