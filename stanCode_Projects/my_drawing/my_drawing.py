"""
File: my_drawing.py
Name: Ester
----------------------
Go Green!
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    減少碳排放，救救極地動物，Go Fresh!
    """
    window = GWindow(1000, 600)
    sea = GRect(1000, 350, x=0, y=250)
    sea.filled = True
    sea.fill_color = 'lightsteelblue'
    sea.color = 'skyblue'
    window.add(sea)
    air1 = GOval(400, 100, x=300, y=180)
    air1.filled = True
    air1.fill_color = 'lightslategray'
    air1.color = 'lightslategray'
    air2 = GOval(200, 100, x=200, y=160)
    air2.filled = True
    air2.fill_color = 'lightslategray'
    air2.color = 'darkgray'
    air3 = GOval(200, 100, x=300, y=100)
    air3.filled = True
    air3.fill_color = 'lightslategray'
    air3.color = 'lightslategray'
    air4 = GOval(200, 100, x=480, y=110)
    air4.filled = True
    air4.fill_color = 'lightslategray'
    air4.color = 'darkgray'
    air5 = GOval(200, 100, x=550, y=170)
    air5.filled = True
    air5.fill_color = 'lightslategray'
    air5.color = 'darkgray'
    air6 = GOval(150, 150, x=450, y=80)
    air6.filled = True
    air6.fill_color = 'lightslategray'
    air6.color = 'lightslategray'
    air7 = GOval(50, 50, x=830, y=30)
    air7.filled = True
    air7.fill_color = 'lightslategray'
    air7.color = 'lightslategray'
    air8 = GOval(70, 60, x=850, y=25)
    air8.filled = True
    air8.fill_color = 'lightslategray'
    air8.color = 'lightslategray'
    air9 = GOval(90, 50, x=870, y=30)
    air9.filled = True
    air9.fill_color = 'lightslategray'
    air9.color = 'lightslategray'
    air10 = GOval(200, 80, x=-35, y=-10)
    air10.filled = True
    air10.fill_color = 'lightslategray'
    air10.color = 'lightslategray'
    air11 = GOval(170, 80, x=-75, y=15)
    air11.filled = True
    air11.fill_color = 'lightslategray'
    air11.color = 'lightslategray'
    window.add(air1)
    window.add(air2)
    window.add(air3)
    window.add(air4)
    window.add(air5)
    window.add(air6)
    window.add(air7)
    window.add(air8)
    window.add(air9)
    window.add(air10)
    window.add(air11)
    ice_land1 = GArc(250, 310, 0, 180)
    ice_land1.filled = True
    ice_land1.fill_color = 'white'
    ice_land1.color = 'white'
    window.add(ice_land1, x=(window.width-ice_land1.width)/2, y=window.height-ice_land1.height)
    head1 = GPolygon()
    head1.add_vertex((500, 100))
    head1.add_vertex((485, 120))
    head1.add_vertex((550, 115))
    head1.filled = True
    head1.fill_color = 'white'
    head1.color = 'white'
    head2 = GPolygon()
    head2.add_vertex((485, 120))
    head2.add_vertex((550, 115))
    head2.add_vertex((525, 140))
    head2.filled = True
    head2.fill_color = 'plum'
    head2.color = 'plum'
    head3 = GPolygon()
    head3.add_vertex((500, 100))
    head3.add_vertex((450, 123))
    head3.add_vertex((460, 150))
    head3.filled = True
    head3.fill_color = 'gainsboro'
    head3.color = 'gainsboro'
    head4 = GPolygon()
    head4.add_vertex((448, 198))
    head4.add_vertex((450, 123))
    head4.add_vertex((475, 190))
    head4.filled = True
    head4.fill_color = 'silver'
    head4.color = 'silver'
    mouse1 = GPolygon()
    mouse1.add_vertex((590, 135))
    mouse1.add_vertex((550, 115))
    mouse1.add_vertex((525, 140))
    mouse1.filled = True
    mouse1.fill_color = 'darkgray'
    mouse1.color = 'gray'
    mouse2 = GPolygon()
    mouse2.add_vertex((590, 135))
    mouse2.add_vertex((550, 150))
    mouse2.add_vertex((525, 140))
    mouse2.filled = True
    face1 = GPolygon()
    face1.add_vertex((485, 120))
    face1.add_vertex((550, 150))
    face1.add_vertex((475, 190))
    face1.filled = True
    face1.fill_color = 'darkgray'
    face1.color = 'gray'
    face2 = GPolygon()
    face2.add_vertex((555, 165))
    face2.add_vertex((550, 150))
    face2.add_vertex((475, 190))
    face2.filled = True
    face3 = GPolygon()
    face3.add_vertex((485, 120))
    face3.add_vertex((460, 150))
    face3.add_vertex((475, 190))
    face3.filled = True
    body1 = GPolygon()
    body1.add_vertex((448, 198))
    body1.add_vertex((555, 165))
    body1.add_vertex((500, 250))
    body1.filled = True
    body1.fill_color = 'gainsboro'
    body1.color = 'gray'
    body2 = GPolygon()
    body2.add_vertex((565, 220))
    body2.add_vertex((555, 165))
    body2.add_vertex((500, 250))
    body2.filled = True
    body2.fill_color = 'white'
    body2.color = 'white'
    body3 = GPolygon()
    body3.add_vertex((500, 250))
    body3.add_vertex((565, 220))
    body3.add_vertex((490, 300))
    body3.filled = True
    body4 = GPolygon()
    body4.add_vertex((500, 250))
    body4.add_vertex((485, 320))
    body4.add_vertex((435, 270))
    body4.filled = True
    body4.fill_color = 'darkgray'
    body4.color = 'gray'
    body5 = GPolygon()
    body5.add_vertex((565, 220))
    body5.add_vertex((565, 250))
    body5.add_vertex((500, 290))
    body5.filled = True
    body5.fill_color = 'darkgray'
    body5.color = 'gray'
    body6 = GPolygon()
    body6.add_vertex((485, 320))
    body6.add_vertex((457, 410))
    body6.add_vertex((400, 385))
    body6.filled = True
    body7 = GPolygon()
    body7.add_vertex((430, 460))
    body7.add_vertex((457, 410))
    body7.add_vertex((400, 385))
    body7.filled = True
    wing1 = GPolygon()
    wing1.add_vertex((448, 198))
    wing1.add_vertex((500, 250))
    wing1.add_vertex((400, 290))
    wing1.filled = True
    wing1.fill_color = 'gray'
    wing1.color = 'gray'
    wing2 = GPolygon()
    wing2.add_vertex((485, 320))
    wing2.add_vertex((425, 260))
    wing2.add_vertex((375, 355))
    wing2.filled = True
    wing2.fill_color = 'dimgray'
    wing2.color = 'gray'
    wing3 = GPolygon()
    wing3.add_vertex((561, 330))
    wing3.add_vertex((541, 380))
    wing3.add_vertex((580, 410))
    wing3.filled = True
    wing4 = GPolygon()
    wing4.add_vertex((485, 320))
    wing4.add_vertex((388, 350))
    wing4.add_vertex((350, 435))
    wing4.filled = True
    wing4.fill_color = 'darkgray'
    wing4.color = 'darkgray'
    belly1 = GPolygon()
    belly1.add_vertex((500, 290))
    belly1.add_vertex((565, 250))
    belly1.add_vertex((565, 320))
    belly1.filled = True
    belly1.fill_color = 'gainsboro'
    belly1.color = 'gainsboro'
    belly2 = GPolygon()
    belly2.add_vertex((500, 290))
    belly2.add_vertex((520, 430))
    belly2.add_vertex((565, 320))
    belly2.filled = True
    belly2.fill_color = 'silver'
    belly2.color = 'silver'
    belly3 = GPolygon()
    belly3.add_vertex((500, 270))
    belly3.add_vertex((520, 430))
    belly3.add_vertex((457, 410))
    belly3.filled = True
    belly3.fill_color = 'white'
    belly3.color = 'white'
    belly4 = GPolygon()
    belly4.add_vertex((430, 460))
    belly4.add_vertex((457, 410))
    belly4.add_vertex((520, 430))
    belly4.filled = True
    belly4.fill_color = 'dimgray'
    belly4.color = 'dimgray'
    belly5 = GPolygon()
    belly5.add_vertex((430, 460))
    belly5.add_vertex((500, 448))
    belly5.add_vertex((520, 430))
    belly5.filled = True
    belly5.fill_color = 'gray'
    belly5.color = 'gray'
    foot1 = GPolygon()
    foot1.add_vertex((430, 460))
    foot1.add_vertex((500, 460))
    foot1.add_vertex((485, 455))
    foot1.filled = True
    foot2 = GPolygon()
    foot2.add_vertex((530, 460))
    foot2.add_vertex((475, 448))
    foot2.add_vertex((550, 448))
    foot2.filled = True
    window.add(head1)
    window.add(head2)
    window.add(head3)
    window.add(head4)
    window.add(mouse1)
    window.add(mouse2)
    window.add(face1)
    window.add(face2)
    window.add(face3)
    window.add(belly3)
    window.add(body1)
    window.add(body2)
    window.add(body3)
    window.add(body4)
    window.add(body5)
    window.add(body6)
    window.add(body7)
    window.add(belly1)
    window.add(belly2)
    window.add(belly4)
    window.add(foot2)
    window.add(belly5)
    window.add(wing2)
    window.add(wing1)
    window.add(foot1)
    window.add(wing3)
    window.add(wing4)


if __name__ == '__main__':
    main()
