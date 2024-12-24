from ._anvil_designer import SmallCardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class SmallCard(SmallCardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  @property
  def background(self):
    return self._background
  
  @background.setter
  def background(self,value):
    self.card.background = value
    self._background = value
    
  @property
  def heading(self):
    return self._heading
  @heading.setter
  def heading(self,value):
    self._heading = value
    self.heading_label.text = value
    
    
  @property
  def icon(self):
    return self._icon
  @icon.setter
  def icon(self,value):
    self._icon = value
    self.icon_label.icon = value
    
  @property
  def subheading(self):
    return self._subheading
  @subheading.setter
  def subheading(self,value):
    self._subheading = value
    self.subheading_label.text = value 
  