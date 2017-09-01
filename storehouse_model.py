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
	######
	#product_id = fields.Char()
	#pname = fields.Char()
	#model = fields.Char()
	#barcodeId = fields.Char()
	#sku = fields.Char()
	#upc = fields.Char()
	#ean = fields.Char()
	#jan = fields.Char()
	#isbn = fields.Char()
	#mpn = fields.Char()
	#p_dimensions = fields.Char()
	#l_class = fields.Char()
	#p_lenght = fields.Char()
	#p_width = fields.Char()
	#p_height = fields.Char()
	#w_class = fields.Char()
	#box_list = fields.Char()
	#status = fields.Boolean()
	#manufacturer = fields.Char()
	#meta_tag_title = fields.Char()
	#primary_image = 
	#image_list =
	#category_id = field.Char()
	#create_user_id = field.Char()
	#create_date = 
	#modify_date = 
	#modify_user_id =



class box(models.Model):
	_name = 'storehouse.box'
	name = fields.Char()

