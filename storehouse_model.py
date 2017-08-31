# -*- coding: utf-8 -*- 
from odoo import models, fields, api
#class TodoTask(models.Model):
#	_name = 'todo.task'
#	_description = 'To-do Task'
#	name = fields.Char('Description', required = True)
#	is_done = fields.Boolean('Done?')
#	active = fields.Boolean('Active', default = True)

class product(models.Model):
	_name = 'storehouse.product'
	id = fields.Char()
	name = fields.Char()
	barcode = fields.Char()
	box = fields.Many2many("storehouse.box", string="Box")

class box(models.Model):
	_name = 'storehouse.box'
	name = fields.Char()

