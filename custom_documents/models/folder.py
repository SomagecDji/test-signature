# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
class DocumentFolder(models.Model):
    _description = 'Document folder'
    _inherit = 'documents.folder' 
    admin_group_ids = fields.Many2many('res.groups',  'documents_folder_admin_groups',string="Groupe d'écriture")
    active=fields.Boolean('Active', default=True)
    project_name=fields.Char('Nom du projet')
    def custom_groups(self):
        folders=self.env['documents.folder'].search([])
        for folder in folders:
            if folder.parent_folder_id:
                parent_folder_id=folder.parent_folder_id.id
                #raise UserError(_(folder.group_ids))
                parent_folder=self.env['documents.folder'].search([('id','=',parent_folder_id)])
                if folder.read_group_ids:
                    for id in [group.id for group in  folder.read_group_ids ]:
                        parent_folder.write({'read_group_ids':[(4,id)]})
                if folder.group_ids:
                    for id in [group.id for group in  folder.group_ids ]:
                        parent_folder.write({'read_group_ids':[(4,id)]})
        return()
    def view_inherit_workspace(self):
        form_view = self.env.ref('akwa_purchase.current_rejection_remark_bc_form_view')
        self.ensure_one()
        return {'name': _('Merci de saisir le nom du projet:'),
                'type': 'ir.actions.act_window',
                'res_model': 'documents.folder',
                'view_mode': 'form',
                'view_id': form_view.id,
                'res_id': self.id,
                'target': 'new'}
"""class SignSendRequest(models.Model):
    _description = 'Sign Send Request'
    _inherit = 'sign.send.request' """

