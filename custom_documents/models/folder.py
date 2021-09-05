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
        form_view = self.env.ref('custom_documents.inherit_workspace_form_view')
        self.ensure_one()
        return {'name': _('Merci de saisir le nom du projet:'),
                'type': 'ir.actions.act_window',
                'res_model': 'documents.folder',
                'view_mode': 'form',
                'view_id': form_view.id,
                'res_id': self.id,
                'target': 'new'}
    def inherit_workspace(self):
        main_workspace_id=self.env['documents.folder'].search([('id','=',3)]).id
        document_folder=self.env['documents.folder']
        document_parent_0=document_folder.create({'name':self.project_name})
        all_subfolders0=self.env['documents.folder'].search([('parent_folder_id','=','main_workspace_id')])
        raise UserError(_(all_subfolders0))
        if len(all_subfolders0)!=0:
            for i in all_subfolders0:
                document_folder=self.env['documents.folder']
                document_parent_1=document_folder.create({'name':i.name,'parent_folder_id':document_parent_0.id})
                all_subfolders1=self.env['documents.folder'].search([('parent_folder_id','=',i.id)])
                if len(all_subfolders1)!=0:
                    for j in all_subfolders1:
                        document_folder=self.env['documents.folder']
                        document_parent_2=document_folder.create({'name':j.name,'parent_folder_id':document_parent_0.id})
                        all_subfolders2=self.env['documents.folder'].search([('id','=',j.id)])
        return {'type': 'ir.actions.act_window_close'}     
"""class SignSendRequest(models.Model):
    _description = 'Sign Send Request'
    _inherit = 'sign.send.request' """

