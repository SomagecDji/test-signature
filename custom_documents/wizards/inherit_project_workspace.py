
from datetime import datetime

from odoo import _, api, fields, models
from odoo.exceptions import UserError,ValidationError

class FolderInheritProjectWorkspace(models.TransientModel):
      _name='inherit.projetc.workspace'
      project_name=fields.Char('Nom du projet')
      def inherit_workspace(self):
          main_workspace_id=self.env['documents.folder'].search([('id','=',3)]).id
          document_folder=self.env['documents.folder']
          document_parent_0=documet_folder.create({'name':self.project_name})
          all_subfolders0=self.env['documents.folder'].search([('parent_folder_id','=','main_workspace_id')])
          if len(all_subfolders0)!=0
              for i in all_subfolders0:
                document_folder=self.env['documents.folder']
                document_parent_1=documet_folder.create({'name':i.name,'parent_folder_id':document_parent_0.id})
                all_subfolders1=self.env['documents.folder'].search([('parent_folder_id','=',i.id)])
                if len(all_subfolders1)!=0:
                    for j in all_subfolders1:
                    document_folder=self.env['documents.folder']
                    document_parent_2=documet_folder.create({'name':j.name,'parent_folder_id':document_parent_0.id})
                    all_subfolders2=self.env['documents.folder'].search([('id','=',j.id)]):
            
               
  


