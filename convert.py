from xml.etree import ElementTree
import os

def read_and_export(filename):

    # Opens data file

    data_file = open(os.path.join("input", filename))
    output_file = open(os.path.join("output", filename[:-3]+"txt"), 'w')
    xml_data = ElementTree.parse(data_file)
    root = xml_data.getroot()

    pattern_node = root.find("Pattern")
    scantrace_node = pattern_node.find("ScanTrace")

    # Locates angular step parameter
    angle_step = float(scantrace_node.find("AngleStep").text)

    data_node = scantrace_node.find("Data")

    x0 = float(data_node.find("y").attrib.get("x"))
    x = x0

    output_file.write("2theta \t intensity\n")
    for y_node in data_node.findall("y"):
        y_str = y_node.text
        y_entries = y_str.split()

        # Writes entry to file
        for entry in y_entries:
            data_str = str(x)+"\t"+entry+"\n"
            x += angle_step
            output_file.write(data_str)

if __name__ == '__main__':

    for data_file in os.listdir('input'):

        if data_file.endswith(".xml"):

            print "Reading "+data_file
            read_and_export(data_file)