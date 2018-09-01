#coding:utf-8
from lxml import etree


def validar_schema(file_schema_xsd, file_xml, lang=None):

    schema = etree.parse(file_schema_xsd)
    xmlschema = etree.XMLSchema(schema)

    try:
        document = etree.parse(file_xml)
        print "Parse complete!"
    except etree.XMLSyntaxError, e:
        print e

    xmlschema.validate(document)

    errors = ''
    
    for error in xmlschema.error_log:
        errors += "ERROR ON LINE %s: %s|" % (error.line, error.message.encode("utf-8"))

