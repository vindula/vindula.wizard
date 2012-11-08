# -*- coding: utf-8 -*-
from five import grok

from Products.CMFCore.interfaces import ISiteRoot
from plone.app.layout.navigation.interfaces import INavigationRoot
from zope.interface import Interface

from random import random

from vindula.network.browser.utils import ToolBox

# View
class VindulaWizardView(grok.View):
    grok.context(Interface)
    grok.name('vindula-wizard')
    grok.require('cmf.ManagePortal')
    
    
    def update(self):
        self.tool = ToolBox(self)
        form = self.request.form 
        session = self.context.REQUEST.SESSION
        
        self.url = ''
        self.titulo = ''
        self.descricao = ''
        
        self.anterior = ''
        self.atual = ''
        
        #passos =  self.tool.properties.get('vindula_wizard','')
        #status_passos = self.tool.properties.get('vindula_status_wizard','')
        passos = self.getStepsConfg(True)
        
        if 'form.proximo' in form.keys():
            atual = eval(form.get('atual','()'))
        
            #status_passos._setPropValue(atual[0],False)
            obj = passos.get(atual[0])
            if obj:
                obj.setStatus(False)
        
        elif 'form.voltar' in form.keys():
            anterior = eval(form.get('anterior','()'))
            
            #status_passos._setPropValue(anterior[0],True)
            obj = passos.get(anterior[0])
            if obj:
                obj.setStatus(True)

        for item in self.getStepsConfg():
            #if item != 'title' and status_passos.getProperty(item):
            valor = item.getUrl()
            if item.getStatus():
            
                self.url = self.tool.site.absolute_url() + valor + '?ajax_load=%s&ajax_include_head=%s&wizard=true'%(random(),random())
                self.titulo = item.Title()
                self.descricao = item.Description()
                
                #session['ajax_load'] = random()
                #session['ajax_include_head'] = random()
                
                self.atual = (item.getId(), valor)
                
                break
            else:
                self.anterior = (item.getId(), valor)


    def getStepsConfg(self,obj=False):
        if 'control-panel-objects' in self.tool.site.objectIds():
            control = self.tool.site['control-panel-objects']
        
            if 'vindula_wizard' in control.objectIds():
                wizard = control['vindula_wizard']
                if obj:
                    return wizard
                else:
                    return wizard.objectValues()
        
        return []

    