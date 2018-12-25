"""
Plots exported RT60 Data from text files
"""
import os
import pandas as pd
import matplotlib
import sys
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO

pd.set_option('display.expand_frame_repr', False)

def extract_data(original_file):
    new_file_contents = str()
    for line in original_file:
        if line.startswith("Format is "):
            line = line.replace("Format is ", "")
            new_file_contents += line
        elif line[0].isdigit():
            new_file_contents += line
    return new_file_contents

def csv_transform(relative_path, i):
    #TODO: remove spaces from beginning of column headers
    current_path = os.path.dirname(__file__)
    file_path = os.path.relpath(relative_path, current_path)
    original_file = open(file_path, 'r')
    csv_data = extract_data(original_file)
    csv_path = os.path.relpath("../csv/{}.csv".format(i), current_path)
    csv = open(csv_path, 'w')
    csv.write(csv_data)
    csv.close()
    return csv_data

def graph_data(x, y, csv_data, png_filename, i):
    df = pd.read_csv(StringIO(csv_data))
    x_values = df[x].values.tolist()
    plot = df.plot.scatter(x = x, y = y, grid = True, logx = True, title = "Reverberation Time vs Frequency with {} People".format(i), xticks = x_values)
    plot.set_xticklabels(x_values)
    figure = plot.get_figure()
    figure.savefig(png_filename)

def Main(relative_path, x, y, png_filename, i):
    csv_data = csv_transform(relative_path, i)
    graph_data(x, y, csv_data, png_filename, i)

if __name__ == "__main__":
    for i in range(0,4):
        Main("../data/RT60/{}.txt".format(i), "freq Hz", " T20 s", "../images/{}.png".format(i), i)
