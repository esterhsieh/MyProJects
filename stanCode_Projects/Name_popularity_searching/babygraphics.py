"""
File: babygraphics.py
Name: Ester
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui
from random import choice


FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 500
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_distance = (width-2*GRAPH_MARGIN_SIZE)//len(YEARS)
    if year_index >= len(YEARS):
        x_coordinate = GRAPH_MARGIN_SIZE+x_distance*(year_index-1)
    else:
        x_coordinate = GRAPH_MARGIN_SIZE + x_distance * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # draw horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)

    # draw vertical line
    for year in YEARS:
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, YEARS.index(year)), 0,
                           get_x_coordinate(CANVAS_WIDTH, YEARS.index(year)), CANVAS_HEIGHT,
                           width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, YEARS.index(year))+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE+TEXT_DX,
                           text=year, anchor=tkinter.NW, font=('Corbel', 10))


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        line_color = COLORS[i%len(COLORS)]
    # for name in lookup_names:
        result = []  # 將每個名字對應的資料儲存在不同的list
        # line_color = choice(COLORS)
        for year in YEARS:
            if str(year) in name_data[name] and int(name_data[name][str(year)]) <= 1000:
                result.append((year, name, name_data[name][str(year)]))
                # result[year] = [name, name_data[name][str(year)]]
            else:
                result.append((year, name, "*"))
                # result[year] = [name, "*"]

        # draw line chart
        for j in range(len(result)):
            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j), get_y_coordinate(CANVAS_HEIGHT, result, j),
                               get_x_coordinate(CANVAS_WIDTH, j + 1), get_y_coordinate(CANVAS_HEIGHT, result, j + 1),
                               width=LINE_WIDTH, fill=line_color)
            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j) + TEXT_DX,
                               get_y_coordinate(CANVAS_HEIGHT, result, j),
                               text=name + " " + result[j][2], anchor=tkinter.SW, font=('Corbel', 10), fill=line_color)


def get_y_coordinate(height, result, result_index):  # get y coordinate
    y_distance = (height - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK
    if result_index >= len(result):
        if result[result_index - 1][2] is "*":
            y_coordinate = GRAPH_MARGIN_SIZE + y_distance * MAX_RANK
        else:
            y_coordinate = GRAPH_MARGIN_SIZE + y_distance * int(result[result_index-1][2])
    else:
        if result[result_index][2] is "*":
            y_coordinate = GRAPH_MARGIN_SIZE + y_distance * MAX_RANK
        else:
            y_coordinate = GRAPH_MARGIN_SIZE+y_distance*(int(result[result_index][2]))
    return y_coordinate


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
