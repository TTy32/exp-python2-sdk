from .. import api_utils

class Device(object):

  def __init__(self, document, _new=True):
    self.document = document
    self._new = _new

  def save(self):
    if self._new:
      self.document = api_utils.post("/api/devices", payload=self.document)
      self._new = False
    else:
      self.document = api_utils.patch("/api/devices/" + self.document["uuid"], payload=self.document)
    return self

  def delete(self):
    api_utils.delete("/api/devices/" + self.document["uuid"])
    return self


  
