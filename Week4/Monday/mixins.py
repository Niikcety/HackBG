import json
import xml.etree.ElementTree as ET

class WithSetAttributes:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)


class WithEqualAttributes:
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Jsonable:
    def to_json(self, indent=4):
        name = self.__class__.__name__

        attributes = self.__dict__

        return json.dumps({'type': name, 'dict': attributes}, indent=indent)

    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)

        class_name = data['type']

        if class_name != cls.__name__:
            raise ValueError('Wrong type.')

        attributes = data['dict']

        return cls(**attributes)

class Xmlable:
    def to_xml(self):
        root = ET.Element(self.__class__.__name__)

        return ET.tostring(root)

    @classmethod
    def from_xml(xml_string):
        pass


if __name__ == '__main__':
    main()
