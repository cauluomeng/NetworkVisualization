from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout


class VertexInfo(QWidget):
    def __init__(self, v):
        super().__init__()

        self.dict = v.attributes()

        layout = QGridLayout(self)
        topLabel = QLabel("VERTEX INFO")
        topLabel.setAlignment(Qt.AlignCenter)
        topLabel.setFont(QFont("SansSerif", 9, QFont.Bold))

        topLabel.setStyleSheet(
            "QLabel { padding: 2px; color: rgb(220,220,220); background-color: #383838;}")
        layout.addWidget(topLabel, 0, 0, 1, 2)

        count = 2
        for x, y in self.dict.items():
            keyLabel = QLabel(str(x) + ":")
            keyLabel.setWordWrap(True)
            # keyLabel.setFont(QFont("SansSerif", 8))
            keyLabel.setStyleSheet("QLabel {  font-weight: Bold; font-size: 12px;"
                                   "color: rgb(220,220,220);}")
            layout.addWidget(keyLabel, count, 0)
            valueLabel = QLabel(str(y))
            valueLabel.setWordWrap(True)
            valueLabel.setStyleSheet("QLabel {  font-size: 11px; border: 1px solid rgb(150, 150, 150); "
                                     "padding: 2px; color: rgb(220,220,220); background-color: #383838;"
                                     "border-radius: 5px; }")
            layout.addWidget(valueLabel, count, 1)
            count = count + 1
        self.setLayout(layout)
        # print("OK")
