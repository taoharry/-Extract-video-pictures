#coding:utf8

import os

from PyQt4 import QtGui,QtCore
import sys


def mv_to_img():
    cmd = 'ffmpeg -i text.avi -r 3   text/%05d.png'
    os.system(cmd)
def makedir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

class get_imginmv(QtGui.QWidget):
    def __init__(self):
        super(get_imginmv,self).__init__()

        self.initUI()

    def initUI(self):

        mv = QtGui.QLabel('mv name', self)
        self.mvEdit = QtGui.QLineEdit()
        
        img = QtGui.QLabel('frame', self)
        self.imgEdit = QtGui.QLineEdit()

        pic = QtGui.QLabel('pic format', self)
        self.picEdit = QtGui.QLineEdit()
        
        okButton = QtGui.QPushButton("PUSH")
        self.connect(okButton,QtCore.SIGNAL('clicked()'),self.run)

        grid = QtGui.QGridLayout()
        grid.setSpacing(4)

        grid.addWidget(mv,1,0)
        grid.addWidget(self.mvEdit,1,1)

        grid.addWidget(img,2,0)
        grid.addWidget(self.imgEdit,2,1)

        grid.addWidget(pic,3,0)
        grid.addWidget(self.picEdit,3,1)

        grid.addWidget(okButton,4,1)

        self.setLayout(grid)

        self.setWindowTitle('main window')
        self.resize(300, 150)
    def run(self):
        if not self.mvEdit.text():
            QMessageBox.information(self, '提示', '请输入视频文件路径加名字')
            return
        if not self.imgEdit.text():
            QMessageBox.information(self, '提示', '请输入采样频率')
            return
        if not self.picEdit.text():
            QMessageBox.information(self, '提示', '请输入图片后缀名')
            return
        mv = str(self.mvEdit.text().toUtf8())
        frame = float(self.imgEdit.text())
        picfile = mv.split('.')[0]
        print type(picfile),picfile
        makedir(picfile.decode('utf-8').encode('gbk'))
        #os.mkdir(picfile)
        formatl = self.picEdit.text()
        cmd = 'ffmpeg -i {mvname} -r {frame} {picfile}/%05d.{formatl}'\
              .format(mvname=mv.decode('utf-8').encode('gbk'),frame=frame,picfile=picfile.decode('utf-8').encode('gbk'),formatl=formatl)
        os.system(cmd)
        
app = QtGui.QApplication(sys.argv)
ex = get_imginmv()
ex.show()
sys.exit(app.exec_())
