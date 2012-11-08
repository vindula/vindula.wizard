# -*- coding: utf-8 -*-
from vindula.wizard import MessageFactory as _
 
from vindula.wizard.content.interfaces import ISteps

from Products.ATContentTypes.content import schemata, base
from zope.interface import implements
from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from vindula.wizard.config import *


# Interface and schema
Steps_schema =  schemata.ATContentTypeSchema.copy() + Schema((
    
    BooleanField(
        name='status',
        widget=BooleanWidget(
            label=_(u"Ativar o passo"),
            description=_(u"Selecione para ativar o passo no wizard"),
            default = True
        ),
    ),

    StringField(
        name='url',
        widget=StringWidget(
            label='Url',
            description="Insira a url para o passo, sem o domineo",
        ),
    ),

))
finalizeATCTSchema(Steps_schema, folderish=False)


class Steps(base.ATCTContent):
    """ Steps """
    
    security = ClassSecurityInfo()
    implements(ISteps)
    portal_type = 'Steps'
    _at_rename_after_creation = True
    schema = Steps_schema
    
registerType(Steps, PROJECTNAME)