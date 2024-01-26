# -*- coding: utf-8 -*-

from matplotlib.backends.backend_qt import _BackendQT, NavigationToolbar2QT, FigureManagerQT
from matplotlib.backends.backend_qtagg import *
from matplotlib.backends.qt_editor import _formlayout
from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.qt_editor._formlayout import FormDialog
import qtawesome as qta
import qdarktheme  # Always import after Qt


class FigureCanvasQTAgg2(FigureCanvasQTAgg):
    def __init__(self, figure=None, *args, **kwargs):
        super().__init__(figure, *args, **kwargs)
        qdarktheme.setup_theme('light')
        # self.figure.set_facecolor('#ebebeb')
        self.figure.set_facecolor('#f8f9fa')


@_BackendQT.export
class _BackendQTAgg(_BackendQT):
    FigureCanvas = FigureCanvasQTAgg2

def fedit2(data, title="", comment="", icon=None, parent=None, apply=None):
    if QtWidgets.QApplication.startingUp():
        _app = QtWidgets.QApplication([])
    dialog = FormDialog(data, title, comment, icon, parent, apply)
    dialog.setStyleSheet("QDialog{background-color: #f8f9fa;}")  # light
    # dialog.setStyleSheet("QDialog{background-color: #202124;}")  # dark
    dialog.setWindowIcon(qta.icon('ph.chart-line'))

    if parent is not None:
        if hasattr(parent, "_fedit_dialog"):
            parent._fedit_dialog.close()
        parent._fedit_dialog = dialog

    dialog.show()


_formlayout.fedit = fedit2


class NV(NavigationToolbar2QT):
    def __init__(self, canvas, parent=None, coordinates=True):
        super().__init__(canvas, parent, coordinates)
        self.setStyleSheet("QToolBar {background : #f8f9fa};")  # light
        # self.setStyleSheet("QToolBar {background : #202124};")  # dark

        btn_reset_zoom = self.actions()[0]
        btn_reset_zoom.setIcon(qta.icon('ph.house'))

        btn_arrow_left = self.actions()[1]
        btn_arrow_left.setIcon(qta.icon('ph.arrow-left'))

        btn_arrow_right = self.actions()[2]
        btn_arrow_right.setIcon(qta.icon('ph.arrow-right'))

        btn_move = self.actions()[4]
        btn_move.setIcon(qta.icon('ph.arrows-out-cardinal'))

        btn_zoom = self.actions()[5]
        btn_zoom.setIcon(qta.icon('ph.magnifying-glass-plus'))

        btn_subplots = self.actions()[6]
        btn_subplots.setIcon(qta.icon('ph.sliders'))

        btn_customize = self.actions()[7]
        btn_customize.setIcon(qta.icon('ph.chart-line'))

        btn_save = self.actions()[9]
        btn_save.setIcon(qta.icon('ph.floppy-disk'))

        self.setMovable(False)


FigureManagerQT._toolbar2_class = NV
