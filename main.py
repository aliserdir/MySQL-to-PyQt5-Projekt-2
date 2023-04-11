import sys
from GUI import *
from connDB import*
from PyQt5.QtWidgets import QTableWidgetItem

class MiApp(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Form() 
		self.ui.setupUi(self)

		self.dataTotal = registerDaten()
		self.ui.btnErfrischen.clicked.connect(self.btnErfrischenClick)
		self.ui.btnHinzufugen.clicked.connect(self.btnHinzufugenClick)
		self.ui.btnSuche.clicked.connect(self.btnSucheClick)
		self.ui.btnDelete.clicked.connect(self.btnDeleteClick)
		self.ui.btnUpdate.clicked.connect(self.btnUpdateClick)
		
		self.ui.tblErfrischen.setColumnWidth(0,98)
		self.ui.tblErfrischen.setColumnWidth(1,100)
		self.ui.tblErfrischen.setColumnWidth(2,98)
		self.ui.tblErfrischen.setColumnWidth(3,98)
		self.ui.tblErfrischen.setColumnWidth(4,98)

		self.ui.tblDelete.setColumnWidth(0,98)
		self.ui.tblDelete.setColumnWidth(1,100)
		self.ui.tblDelete.setColumnWidth(2,98)
		self.ui.tblDelete.setColumnWidth(3,98)
		self.ui.tblDelete.setColumnWidth(4,98)

		self.ui.tblSuche.setColumnWidth(0,98)
		self.ui.tblSuche.setColumnWidth(1,100)
		self.ui.tblSuche.setColumnWidth(2,98)
		self.ui.tblSuche.setColumnWidth(3,98)
		self.ui.tblSuche.setColumnWidth(4,98)

		self.btnErfrischenClick()

	def btnErfrischenClick(self):
		data = self.dataTotal.produktAlleAufliste()

		self.ui.tblErfrischen.setRowCount(0)
		self.ui.tblErfrischen.insertRow(0)


		for row, form in enumerate(data):
			for column, item in enumerate(form):
				self.ui.tblErfrischen.setItem(row, column, QTableWidgetItem(str(item)))

			row_position = self.ui.tblErfrischen.rowCount()
			self.ui.tblErfrischen.insertRow(row_position)

	def btnHinzufugenClick(self):

		produktCode = self.ui.textCodeH.text()
		produktName = self.ui.textNameH.text()
		produktModell = self.ui.textModellH.text()
		produktPreis = self.ui.textPreisH.text()
		produktMenge = self.ui.textMengeH.text()

		self.dataTotal.produktHinzufugen(produktCode, produktName, produktModell, produktPreis, produktMenge)  ##bu satırın yeri önemli.

		self.ui.textCodeH.clear()
		self.ui.textNameH.clear()
		self.ui.textModellH.clear()
		self.ui.textPreisH.clear()
		self.ui.textMengeH.clear()

	def btnUpdateClick(self):
		ID = self.ui.tetxtIDU.text()

		if ID != None:
			self.ui.idSuche.setText("ACTUALIZAR")
			produktCodeU = self.ui.textCodeU.text()
			produktNameU = self.ui.textNameU.text()
			produktModellU = self.ui.textModellU.text()
			produktPreisU = self.ui.textPreisU.text()
			produktMengeU = self.ui.textMengeU.text()
			act = self.dataTotal.produktUpdate(produktCodeU, produktNameU, produktModellU, produktPreisU, produktMengeU, ID)
			if act == 1:
				self.ui.idSuche.setText("ACTUALIZADO")
				self.ui.textCodeU.clear()
				self.ui.textNameU.clear()
				self.ui.textModellU.clear()
				self.ui.textPreisU.clear()
				self.ui.textMengeU.clear()
				self.ui.tetxtIDU.clear()
			elif act == 0:
				self.ui.idSuche.setText("ERROR")
			else:
				self.ui.idSuche.setText("INCORRECTO")
		else:
			self.ui.idSuche.setText("NO EXISTE")

		self.btnErfrischenClick()



	def btnSucheClick(self):
		nombre_producto = self.ui.textCodeS.text()
		datosB = self.dataTotal.produktSuche(nombre_producto)
		i = len(datosB)

		self.ui.tblSuche.setRowCount(i)
		for row_number, row_data in enumerate(datosB):
			for column_number, data in enumerate(row_data):
				self.ui.tblSuche.setItem(row_number, column_number, QTableWidgetItem(str(data)))

	def btnDeleteClick(self):
		eliminar = self.ui.textIDD.text()
		datos = self.dataTotal.produktAlleAufliste()

		self.ui.tblDelete.setRowCount(0)
		self.ui.tblDelete.insertRow(0)

		for row, form in enumerate(datos):
			for column, item in enumerate(form):
				self.ui.tblDelete.setItem(row, column, QTableWidgetItem(str(item)))

			row_position = self.ui.tblDelete.rowCount()
			self.ui.tblDelete.insertRow(row_position)

		resp = self.dataTotal.produktDelete(eliminar)
		if resp == None or resp == 0:
			self.ui.deleteOk.setText("NO EXISTE")
		else:
			self.ui.deleteOk.setText("SE ELIMINO")
		self.btnErfrischenClick()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mi_app = MiApp()
	mi_app.show()
	sys.exit(app.exec_())
