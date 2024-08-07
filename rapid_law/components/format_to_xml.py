import xml.etree.ElementTree as ET


def xml_format(data : list[dict]):
    root = ET.Element("documents")

    # Populate the XML
    for item in data:
        doc = ET.SubElement(root, "document")
        ET.SubElement(doc, "chapter").text = item['chapter']
        ET.SubElement(doc, "title").text = item['title']
        ET.SubElement(doc, "subchapter").text = item['subchapter']
        ET.SubElement(doc, "section").text = item['section']
        
        section_content = ET.SubElement(doc, "section_content")
        paragraphs = item['section_content'].split('  ')
        for para in paragraphs:
            if para.strip():
                ET.SubElement(section_content, "paragraph").text = para.strip()
        
        ET.SubElement(doc, "url").text = item['url']

    # Convert to XML string
    xml_str = ET.tostring(root, encoding='unicode', method='xml')

    # Print the XML string
    return str(xml_str)