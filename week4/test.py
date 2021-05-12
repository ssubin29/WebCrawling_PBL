from PyQt5.QtGui import QPalette, QTextCharFormat
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QCalendarWidget

class MyCalendar(QCalendarWidget):
    def __init__(self):
        super().__init__()
        self.begin_date = None
        self.end_date = None
        print(self.selectedDate())

        self.highlight_format = QTextCharFormat()
        self.highlight_format.setBackground(self.palette().brush(QPalette.Highlight))
        self.highlight_format.setForeground(self.palette().color(QPalette.HighlightedText))

        self.clicked.connect(self.date_is_clicked)
        print(super().dateTextFormat())

    def format_range(self, format):
        if self.begin_date and self.end_date:
            d0 = min(self.begin_date, self.end_date)
            d1 = max(self.begin_date, self.end_date)
            while d0 <= d1:
                self.setDateTextFormat(d0, format)
                d0 = d0.addDays(1)


    def date_is_clicked(self, date):
        # reset highlighting of previously selected date range
        self.format_range(QTextCharFormat())
        if QApplication.instance().keyboardModifiers() & Qt.ShiftModifier and self.begin_date:
            self.end_date = date
            # set highilighting of currently selected date range
            self.format_range(self.highlight_format)
        else:
            self.begin_date = date
            self.end_date = None

if __name__ == "__main__":
    app = QApplication([])
    calendar = MyCalendar()
    calendar.show()
    app.exec()
