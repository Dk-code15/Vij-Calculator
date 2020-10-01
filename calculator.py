# calculator.py
#
# Copyright 2011 Vijeenrosh P.W <hsorhteeniv@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston
# MA 02110-1301, USA.


import wx  # Importing wx
import CalcFrame  # importing calcframe
class App(wx.App):
	def OnInit(self):
		calc = CalcFrame.Calculator((250,300))
		calc.Show()
		return True
app = App()
app.MainLoop()

		
