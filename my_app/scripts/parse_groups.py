#parsing the grouping information from moodle backup after extraction
import xml.etree.ElementTree as ET


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def get_groups(root):
    groups = []
    for group in root.findall('./group'):
        g_id = group.attrib
        name = group.find('name').text
        if name == "Staff":
            staff = g_id["id"]
        else:
            groups.append(g_id["id"])
            
    return groups, staff

