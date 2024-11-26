from langchain.tools import Tool
import json
import env

import xml.etree.ElementTree as ET
import re
import nltk
from nltk.corpus import stopwords, words
from nltk.tokenize import word_tokenize
import xml.etree.ElementTree as ET

def xml_to_text(xml_content):
    # Parse XML
    root = ET.fromstring(xml_content)

    def extract_text(node, level=0):
        # Indentation for readability based on level of depth
        indentation = ' ' * (level * 4)

        # Get the text content of the node if available
        text_content = node.get('text')

        # Only include nodes that have non-empty text fields
        result = ""
        if text_content:
            result += f"{indentation}{text_content}\n"

        # Process child nodes recursively
        for child in node:
            result += extract_text(child, level + 1)

        return result

    # Generate and return the structured text with only 'text' fields
    return extract_text(root)

print(xml_to_text("""
<?xml version="1.0" encoding="UTF-8"?><node index="0" text="" resource-id="com.oplus.securitypermission:id/topPanel" class="android.widget.LinearLayout" package="com.oplus.securitypermission" content-desc="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[48,1710][1032,1936]">
    <node index="0" text="" resource-id="com.oplus.securitypermission:id/alert_title_scroll_view" class="android.widget.ScrollView" package="com.oplus.securitypermission" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[120,1782][960,1918]">
      <node index="0" text=" &quot;SweetMeet&quot;  requires permission: Read your app list." resource-id="com.oplus.securitypermission:id/alertTitle" class="android.widget.TextView" package="com.oplus.securitypermission" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[120,1782][960,1918]"/>
    </node>
  </node>
"""))