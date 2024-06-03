import xml.sax
import os

class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.system_ids = set()
        self.referanse_ids = set()
        self.current_tag = ""

    def startElement(self, tag, attributes):
        self.current_tag = tag

    def endElement(self, tag):
        self.current_tag = ""

    def characters(self, content):
        content = content.strip()
        if content:
            if self.current_tag == "systemID":
                self.system_ids.add(content)
            elif self.current_tag == "referanseTilMappe":
                self.referanse_ids.add(content)

def validate_uuids(xml_file):
    try:
        # Create XML handler
        handler = XMLHandler()

        # Parse the XML file using SAX parser
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse(xml_file)

        # Debug: Print the extracted UUIDs
        print("systemID values:")
        for system_id in handler.system_ids:
            print(system_id)

        print("\nreferanseTilMappe values:")
        for referanse_id in handler.referanse_ids:
            print(referanse_id)

        # Check if all referanse_ids exist in system_ids
        invalid_referanse_ids = [id for id in handler.referanse_ids if id not in handler.system_ids]

        if not invalid_referanse_ids:
            print("\nAll <referanseTilMappe> UUIDs are valid.")
        else:
            print("\nInvalid UUIDs found in <referanseTilMappe>:")
            for id in invalid_referanse_ids:
                print(id)

            # Write the invalid UUIDs to a text file
            output_file = os.path.join(os.path.dirname(xml_file), 'invalid_referanseTilMappe.txt')
            with open(output_file, 'w') as f:
                for id in invalid_referanse_ids:
                    f.write(f"{id}\n")
            print(f"\nInvalid UUIDs have been written to {output_file}")

    except Exception as e:
        print(f"Error parsing XML file: {e}")

# Replace 'your_file.xml' with the path to your XML file
xml_file = "4643_004_Websak_(2005-2019)-papir.xml"
validate_uuids(xml_file)


