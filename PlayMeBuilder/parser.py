
from xml.etree import ElementTree


class API(object):

    def __init__(self, file_):

        self._tree = ElementTree.parse(file_)
        self._element = self._tree.getroot()
        self.name = self._element.attrib['name']
        self.uri = self._element.attrib['uri']
        self.version = self._element.attrib['version']

        self.entities = self._element.find('entities')
        if not self.entities is None:
            self.entities = [Entity(element)
                             for element in list(self.entities)]


class Entity(object):

    def __init__(self, element):
        self._element = element
        self.name = element.attrib['name']
        self.methods = element.find('methods')
        if not self.methods is None:
            self.methods = [Method(element) for element in list(self.methods)]


class Method(object):

    def __init__(self, element):

        self._element = element
        self.name = element.attrib['name']
        self.public = False
        self.created = element.attrib['created']

        if element.attrib.get('public', '').lower() in ('true', '1'):
            self.public = True

        self.description = element.find('description')
        if not self.description is None:
            self.description = self.description.text.strip()

        self.request = element.find('request')
        if not self.request is None:
            self.request = Request(self.request)


class Request(object):

    def __init__(self, element):

        self._element = element        
        self.methods = [elem.attrib['name'].upper()
                        for elem in list(element.find('methods'))]
        self.fields = {'required': [], 'optional': [], 'all': []}

        for elem in list(element.find('fields')):

            field = Field(elem)

            self.fields['all'].append(field)

            if field.required:
                self.fields['required'].append(field)
            else:
                self.fields['optional'].append(field)


class Field(object):

    def __init__(self, element):

        self._element = element
        self.name = element.attrib['name']
        self.required = element.attrib.get('required', '').lower()
        self.default = element.attrib.get('default', None)

        if self.required in ('true', '1'):
            self.required = True
        else:
            self.required = False

        self.description = element.find('description')
        if not self.description is None:
            self.description = self.description.text.strip()
