# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName

def createSteps(context):    
    portal = context.getSite()

    portal.portal_types.get('Folder').global_allow = False

    if 'control-panel-objects' in portal.objectIds():
        control = portal['control-panel-objects']
        
        if not 'vindula_wizard' in control.objectIds():
            portal.portal_types.get('Folder').global_allow = True
            
            control.invokeFactory('Folder', 
                                  id='vindula_wizard', 
                                  title='Configuração do Vindula Wizard',
                                  description='Pasta que guardar os passos de configuração do Vindula.',
                                  excludeFromNav = True)
        
            folder_steps = control['vindula_wizard']
            folder_steps.setConstrainTypesMode(1)
            folder_steps.setLocallyAllowedTypes(('Steps','Folder',))
        
            portal.portal_types.get('Folder').global_allow = False
            print 'Create Vindula Wizard object.'
    

