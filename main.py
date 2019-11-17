import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.listWidget.currentItemChanged.connect(self.change_coffee)
        self.load_data_base()

        self.title_font = QFont()
        self.title_font.setPixelSize(26)

        self.details_font = QFont()
        self.details_font.setPixelSize(18)

        self.html = '''
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:28pt;">{name}</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:11pt;">Степень обжарки: {roaster}</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:11pt;">{ground}</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:11pt;">{taste}</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:11pt;">Цена: {price}</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:11pt;">Объём: {volume}</span></p></body></html>
        '''

    def load_data_base(self):
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()
        data = cur.execute('SELECT * FROM coffes').fetchall()
        titles = list(map(lambda elem: elem[1], data))
        self.listWidget.addItems(titles)
        con.close()

    def change_coffee(self, item):
        name = item.text()
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()
        coffee_data = cur.execute('''
        SELECT name, roaster, ground, taste, price, volume FROM coffes WHERE name = ?''',
                                  (name,)).fetchall()
        if coffee_data:
            coffee_data = coffee_data[0]
            html = self.html
            html = html.replace('{name}', str(coffee_data[0]))
            html = html.replace('{roaster}', str(coffee_data[1]))
            html = html.replace('{ground}', 'Молотый' if coffee_data[2] else 'В зернах')
            html = html.replace('{taste}', str(coffee_data[3]))
            html = html.replace('{price}', str(coffee_data[4]))
            html = html.replace('{volume}', str(coffee_data[5]))
            self.textBrowser.setHtml(html)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
