import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
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
        self.add_btn.clicked.connect(self.add_coffee)
        self.edit_btn.clicked.connect(self.edit_coffee)
        self.listWidget.currentItemChanged.connect(self.change_coffee)
        self.load_data_base()

        self.title_font = QFont()
        self.title_font.setPixelSize(26)

        self.details_font = QFont()
        self.details_font.setPixelSize(18)

    def load_data_base(self):
        old_row = 0
        if self.listWidget.currentRow() > 0:
            old_row = self.listWidget.currentRow()
        self.listWidget.clear()
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()
        data = cur.execute('SELECT * FROM coffes').fetchall()
        titles = sorted(list(map(lambda elem: elem[1], data)))
        self.listWidget.addItems(titles)
        self.listWidget.setCurrentRow(old_row)
        con.close()

    def change_coffee(self, item):
        if self.listWidget.currentItem():
            self.edit_btn.setDisabled(False)
        if not item:
            return
        name = item.text()
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()
        coffee_data = cur.execute('''
        SELECT name, roaster, ground, taste, price, volume FROM coffes WHERE name = ?''',
                                  (name,)).fetchall()
        if coffee_data:
            coffee_data = coffee_data[0]
            roaster = cur.execute('''SELECT name from roasters WHERE id = ?''',
                                  (coffee_data[1],)).fetchone()[0]
            html = self.html
            html = html.replace('{name}', str(coffee_data[0]))
            html = html.replace('{roaster}', str(roaster))
            html = html.replace('{ground}', 'Молотый' if coffee_data[2] else 'В зёрнах')
            html = html.replace('{taste}', str(coffee_data[3]))
            html = html.replace('{price}', str(coffee_data[4]))
            html = html.replace('{volume}', str(coffee_data[5]))
            self.textBrowser.setHtml(html)
        con.close()

    def add_coffee(self):
        self.edit_form = AddCoffeeForm()
        self.edit_form.finished.connect(self.load_data_base)
        self.edit_form.exec()

    def edit_coffee(self):
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()
        coffee_data = cur.execute('SELECT * FROM coffes WHERE name = ?',
                                  (self.listWidget.currentItem().text(),)).fetchone()
        self.edit_form = AddCoffeeForm(coffee_data)
        self.edit_form.finished.connect(self.load_data_base)
        self.edit_form.exec()


class AddCoffeeForm(QDialog):
    def __init__(self, coffee_data=None):
        super().__init__()
        uic.loadUi('add_coffee_form.ui', self)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.buttonBox.clicked.connect(self.click_btn_box)
        self.taste_edit_btn.clicked.connect(self.edit_taste)
        self.init_roaster_combo_box()
        self.coffee_data = coffee_data
        if coffee_data:
            self.id = coffee_data[0]
            self.initUI()
        else:
            self.id = None

    def initUI(self):
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()

        name = self.coffee_data[1]
        roaster = cur.execute('SELECT name FROM roasters WHERE id = ?',
                              (self.coffee_data[2],)).fetchone()[0]
        ground = self.coffee_data[3]
        self.taste = self.coffee_data[4]
        price = self.coffee_data[5]
        volume = self.coffee_data[6]

        self.name_lineEdit.setText(name)
        self.roaster_comboBox.setCurrentText(roaster)
        if ground:
            self.taste_radioButton.setChecked(True)
        else:
            self.grains_radioButton.setChecked(True)
        self.price_spinBox.setValue(price)
        self.volume_spinBox.setValue(volume)

        con.close()

    def init_roaster_combo_box(self):
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()

        roasters = cur.execute('SELECT name FROM roasters').fetchall()
        self.roaster_comboBox.addItems(list(map(lambda data: data[0], roasters)))

        con.close()

    def click_btn_box(self, btn):
        btn_text = btn.text()
        if btn_text == 'OK':
            con = sqlite3.connect('coffee.db')
            cur = con.cursor()

            name = self.name_lineEdit.text()
            roaster = cur.execute('SELECT id FROM roasters WHERE name = ?',
                                  (self.roaster_comboBox.currentText(),)).fetchone()[0]
            ground = 1 if self.taste_radioButton.isChecked() else 0
            taste = self.taste
            price = self.price_spinBox.value()
            volume = self.volume_spinBox.value()

            if name and roaster and taste and price and volume:
                if self.id:
                    cur.execute('''UPDATE coffes SET name = ?, roaster = ?, ground = ?, taste = ?,
                    price = ?, volume = ? WHERE id = ?''',
                                (name, roaster, ground, self.taste, price, volume, self.id,))
                else:
                    cur.execute('''INSERT INTO coffes(name, roaster, ground, taste, price, volume)
                     VALUES (?, ?, ?, ?, ?, ?)''',
                                (name, roaster, ground, self.taste, price, volume,))
                con.commit()
                con.close()
        self.close()

    def edit_taste(self):
        if self.coffee_data:
            self.edit_taste_dialog = EditTaste(self.enter_edit_taste, self.name_lineEdit.text(),
                                               self.id, self.taste)
        else:
            self.edit_taste_dialog = EditTaste(self.enter_edit_taste, self.name_lineEdit.text())
        self.edit_taste_dialog.exec()

    def enter_edit_taste(self, new_taste):
        self.taste = new_taste


class EditTaste(QDialog):
    def __init__(self, enter_edit_taste_func, name_coffee, id=None, old_taste=None):
        super().__init__()
        uic.loadUi('edit_taste_form.ui', self)
        self.setWindowTitle(name_coffee)
        self.name_label.setText(name_coffee)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.buttonBox.clicked.connect(self.click_btn_box)
        self.enter_edit_taste_func = enter_edit_taste_func
        self.id = id

        font = QFont()
        font.setPixelSize(16)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setPlainText(old_taste)

    def click_btn_box(self, btn):
        btn_text = btn.text()
        if btn_text == 'OK':
            con = sqlite3.connect('coffee.db')
            cur = con.cursor()

            new_taste = self.plainTextEdit.toPlainText()
            if not new_taste:
                return
            self.enter_edit_taste_func(new_taste)

            con.commit()
            con.close()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
