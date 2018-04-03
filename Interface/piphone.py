import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
import os
import serial
import time, sys

ser = serial.Serial('/dev/ttyS0', 19200, timeout=5)


class Ventana:
	global ser

	def __init__(self):
		self.initNumberLabel = "NO NUMBER TYPED"
		self.gladefile = "/home/pi/Desktop/Interfaz/piphone.glade"
		self.builder = Gtk.Builder()
		self.builder.add_from_file(self.gladefile)

		time.sleep(1)
		colorh="#5dca31"
		color=Gdk.RGBA()
		color.parse(colorh)
		color.to_string()

		self.button1 = self.builder.get_object("button1")
		self.button1.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button1.modify_font(Pango.FontDescription("sans 48"))
		self.button1.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.button2 = self.builder.get_object("button2")
		self.button2.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button2.modify_font(Pango.FontDescription("sans 48"))
		self.button2.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.button3 = self.builder.get_object("button3")
		self.button3.modify_font(Pango.FontDescription("sans 48"))
		self.button3.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button3.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.button4 = self.builder.get_object("button4")
		self.button4.modify_font(Pango.FontDescription("sans 48"))
		self.button4.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button4.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.button5 = self.builder.get_object("button5")
		self.button5.modify_font(Pango.FontDescription("sans 48"))
		self.button5.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button5.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.button6 = self.builder.get_object("button6")
		self.button6.modify_font(Pango.FontDescription("sans 48"))
		self.button6.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button6.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.button7 = self.builder.get_object("button7")
		self.button7.modify_font(Pango.FontDescription("sans 48"))
		self.button7.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button7.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.button8 = self.builder.get_object("button8")
		self.button8.modify_font(Pango.FontDescription("sans 48"))
		self.button8.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button8.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.button9 = self.builder.get_object("button9")
		self.button9.modify_font(Pango.FontDescription("sans 48"))
		self.button9.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button9.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.button0 = self.builder.get_object("button0")
		self.button0.modify_font(Pango.FontDescription("sans 48"))
		self.button0.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button0.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.buttonCall = self.builder.get_object("buttonCall")
		self.buttonCall.modify_font(Pango.FontDescription("sans 48"))
		self.buttonCall.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.buttonCall.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.buttonSlash = self.builder.get_object("buttonSlash")
		self.buttonSlash.modify_font(Pango.FontDescription("sans 48"))
		self.buttonSlash.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.buttonSlash.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.buttonStar = self.builder.get_object("buttonStar")
		self.buttonStar.modify_font(Pango.FontDescription("sans 48"))
		self.buttonStar.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.buttonStar.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		
		colorh="#F08080"
		color=Gdk.RGBA()
		color.parse(colorh)
		color.to_string()

		self.buttonDelete = self.builder.get_object("buttonDel")
		self.buttonDelete.modify_font(Pango.FontDescription("sans 48"))
		self.buttonDelete.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.buttonDelete.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.buttonStopCall = self.builder.get_object("buttonStopCall")
		self.buttonStopCall.modify_font(Pango.FontDescription("sans 48"))
		self.buttonStopCall.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.buttonStopCall.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))

		self.phoneNumber = self.builder.get_object('phoneNumber')
		self.phoneNumber.set_text(self.initNumberLabel)
		self.phoneNumber.modify_font(Pango.FontDescription("sans 48"))

		self.bgbox = self.builder.get_object('bgbox')
		self.bgbox.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("#000000"))

		self.grid1 = self.builder.get_object('grid1')
		self.grid1.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("#000000"))

		self.window = self.builder.get_object("window1")
		self.window.fullscreen()
		self.window.show_all()

		self.builder.connect_signals(self)

	def type(self, number):
		text = self.phoneNumber.get_text()
		if(text == self.initNumberLabel):
			text = ""
		text = text+number
		self.phoneNumber.set_text(text)
		return;

	def type1(self, widget):
		self.type("1")

	def type2(self, widget):
		self.type("2")

	def type3(self, widget):
		self.type("3")
		
	def type4(self, widget):
		self.type("4")
		
	def type5(self, widget):
		self.type("5")
		
	def type6(self, widget):
		self.type("6")
		
	def type7(self, widget):
		self.type("7")
		
	def type8(self, widget):
		self.type("8")
		
	def type9(self, widget):
		self.type("9")
		
	def type0(self, widget):
		self.type("0")

	def typeStar(self, widget):
		self.type("*")

	def typeSlash(self, widget):
		self.type("#")

	def delete(self, widget):
		text = self.phoneNumber.get_text()

		if( text != self.initNumberLabel):
			text = text[:-1]
			self.phoneNumber.set_text(text)
		if( text == ""):
			text = self.initNumberLabel
			self.phoneNumber.set_text(text)
	
	def call(self, widget):
		text = self.phoneNumber.get_text()
		self.phoneNumber.set_text("Calling... " + text)
		ser.write('''ATD'''+text+''';\r\n''')
		time.sleep(1)
		ser.write(chr(26))

	def stopCall(self, widget):
		ser.write('''AT+CHUP\r\n''')
		time.sleep(1)
		ser.write(chr(26))
		self.phoneNumber.set_text(self.initNumberLabel)

class Pin:
	global ser

	def __init__(self, menu):
		self.menu = menu
		self.initNumberLabel = "NO NUMBER TYPED"
		self.errorLabel = "WRONG PIN"

		self.builder = Gtk.Builder()
		self.builder.add_objects_from_file("/home/pi/Desktop/Interfaz/piphone.glade", ("pin", ""))
		
		colorh="#5dca31"
		color=Gdk.RGBA()
		color.parse(colorh)
		color.to_string()

		self.button01 = self.builder.get_object("button01")
		self.button01.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button01.modify_font(Pango.FontDescription("sans 48"))
		self.button01.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.button02 = self.builder.get_object("button02")
		self.button02.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button02.modify_font(Pango.FontDescription("sans 48"))
		self.button02.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.button03 = self.builder.get_object("button03")
		self.button03.modify_font(Pango.FontDescription("sans 48"))
		self.button03.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button03.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.button04 = self.builder.get_object("button04")
		self.button04.modify_font(Pango.FontDescription("sans 48"))
		self.button04.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button04.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.button05 = self.builder.get_object("button05")
		self.button05.modify_font(Pango.FontDescription("sans 48"))
		self.button05.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button05.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.button06 = self.builder.get_object("button06")
		self.button06.modify_font(Pango.FontDescription("sans 48"))
		self.button06.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button06.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.button07 = self.builder.get_object("button07")
		self.button07.modify_font(Pango.FontDescription("sans 48"))
		self.button07.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button07.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.button08 = self.builder.get_object("button08")
		self.button08.modify_font(Pango.FontDescription("sans 48"))
		self.button08.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button08.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.button09 = self.builder.get_object("button09")
		self.button09.modify_font(Pango.FontDescription("sans 48"))
		self.button09.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button09.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.button00 = self.builder.get_object("button00")
		self.button00.modify_font(Pango.FontDescription("sans 48"))
		self.button00.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.button00.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.buttonEnter = self.builder.get_object("buttonEnter")
		self.buttonEnter.modify_font(Pango.FontDescription("sans 48"))
		self.buttonEnter.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.buttonEnter.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		
		colorh="#F08080"
		color=Gdk.RGBA()
		color.parse(colorh)
		color.to_string()

		self.buttonDelPin = self.builder.get_object("buttonDelPin")
		self.buttonDelPin.modify_font(Pango.FontDescription("sans 48"))
		self.buttonDelPin.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.buttonDelPin.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))
		self.buttonBack = self.builder.get_object("buttonBac")
		self.buttonBack.modify_font(Pango.FontDescription("sans 48"))
		self.buttonBack.override_background_color(Gtk.StateFlags.NORMAL, color)
		self.buttonBack.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse('#848484'))

		self.phoneNumber = self.builder.get_object('phoneNumber1')
		self.phoneNumber.set_text(self.initNumberLabel)
		self.phoneNumber.modify_font(Pango.FontDescription("sans 48"))

		self.bgbox = self.builder.get_object('bgbox1')
		self.bgbox.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("#000000"))

		self.grid1 = self.builder.get_object('grid2')
		self.grid1.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("#000000"))

		self.pin = self.builder.get_object("pin")
		self.pin.fullscreen()
		self.pin.show_all()

		self.builder.connect_signals(self)

	def type(self, number):
		text = self.phoneNumber.get_text()
		if(text == self.initNumberLabel or text == self.errorLabel ):
			text = ""
		text = text+number
		self.phoneNumber.set_text(text)
		return;

	def type1(self, widget):
		self.type("1")

	def type2(self, widget):
		self.type("2")

	def type3(self, widget):
		self.type("3")
		
	def type4(self, widget):
		self.type("4")
		
	def type5(self, widget):
		self.type("5")
		
	def type6(self, widget):
		self.type("6")
		
	def type7(self, widget):
		self.type("7")
		
	def type8(self, widget):
		self.type("8")
		
	def type9(self, widget):
		self.type("9")
		
	def type0(self, widget):
		self.type("0")

	def delete(self, widget):
		text = self.phoneNumber.get_text()

		if( text == self.errorLabel ):
			self.phoneNumber.set_text(self.initNumberLabel)
		elif( text != self.initNumberLabel):
			text = text[:-1]
			self.phoneNumber.set_text(text)
		if( text == ""):
			text = self.initNumberLabel
			self.phoneNumber.set_text(text)

	def checkPin(self, widget):
		text = self.phoneNumber.get_text()
		ser.write('''AT+CPIN="'''+text+'''"\r\n''')
		time.sleep(1)
		ser.write(chr(26))
		Ventana()
		self.pin.hide()
	
	def goMenu(self, widget):
		self.menu.show()
		self.pin.hide()

class Menu:
	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_objects_from_file("/home/pi/Desktop/Interfaz/piphone.glade", ("menu", ""))
		self.options = self.builder.get_object('options')
		self.options.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("#000000"))
		self.menu = self.builder.get_object("menu")
		self.menu.fullscreen()
		self.menu.show_all()
		self.builder.connect_signals(self)

	def gocall(self, widget):
		Pin(self.menu)
		self.menu.hide()
	
	def goInstructions(self, widget):
		Instructions(self.menu)
		self.menu.hide()

	def goAbout(self, widget):
		About(self.menu)		
		self.menu.hide()

	def exit(self, widget):
		Gtk.main_quit()

class Instructions:
	def __init__(self, menu):
		self.menu = menu
		self.builder = Gtk.Builder()
		self.builder.add_objects_from_file("/home/pi/Desktop/Interfaz/piphone.glade", ("instructions", ""))
		self.instructions = self.builder.get_object("instructions")

		self.instructions = self.builder.get_object("instructions")
		self.instructionsbox = self.builder.get_object("instructionsbox")		
		self.instructionsgrid = self.builder.get_object("instructionsgrid")
		self.instructionstext = self.builder.get_object("instructionstext")	

		self.instructionsbox.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("#000000"))
		self.instructionsgrid.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("#000000"))
		self.instructionstext.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("#000000"))
		self.instructions.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("#000000"))

		self.instructions.fullscreen()
		self.instructions.show_all()
		self.builder.connect_signals(self)

	def goMenu(self, widget):
		self.menu.show()
		self.instructions.hide()

class About:
	def __init__(self, menu):
		self.menu = menu
		self.builder = Gtk.Builder()
		self.builder.add_objects_from_file("/home/pi/Desktop/Interfaz/piphone.glade", ("about", ""))
		self.about = self.builder.get_object("about")

		self.about = self.builder.get_object("about")
		self.aboutbox = self.builder.get_object("aboutbox")		
		self.aboutgrid = self.builder.get_object("aboutgrid")
		self.abouttext = self.builder.get_object("abouttext")	

		self.aboutbox.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("#000000"))
		self.aboutgrid.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("#000000"))
		self.abouttext.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("#000000"))
		self.about.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse("#000000"))

		self.about.fullscreen()
		self.about.show_all()
		self.builder.connect_signals(self)

	def goMenu(self, widget):
		self.menu.show()
		self.about.hide()

def main():
    Menu()
    Gtk.main()

if __name__ == '__main__':
	main()
