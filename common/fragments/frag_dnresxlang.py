#!/usr/bin/env python3

#
# Copyright 2025-2026 Aptivi
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the “Software”), to deal in the Software without
# restriction, including without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#

# Configuration module
import adt_conf

# Import necessary components
import os
import xml.etree.ElementTree as XmlElementTree
from datetime import datetime
from common.fragments.frag_dnresxlang_parts import \
    drl_lslangs, \
    drl_getpath, \
    drl_getresxpath, \
    drl_genjson, \
    drl_genjson_final, \
    drl_deserialize


def drl_add_culture(json_path: str, lang: str, cultures: list[str]):
    # User wants to add a culture. Get necessary arguments.
    if (adt_conf.verbose):
        print("drl_add_culture(%s, %s, %s)" % (json_path, lang, cultures))
    if (not lang) or len(lang) == 0:
        raise ValueError("Language not specified")
    if (not cultures) or len(cultures) == 0:
        raise ValueError("Cultures not specified")
    
    # Check the cultures if they already exist
    lang_info = drl_deserialize(json_path, lang)
    for target_culture in cultures:
        if target_culture in lang_info.cultures:
            raise ValueError(f"Localization {target_culture} already exists")

    # Add the localization
    for culture in cultures:
        lang_info.cultures.append(culture)

    # Save the changes
    drl_genjson_final(json_path, lang_info)


def drl_add_loc(json_path: str, lang: str, locs: list[str]):
    # User wants to add a localization. Get necessary arguments.
    if (adt_conf.verbose):
        print("drl_add_loc(%s, %s, %s)" % (json_path, lang, locs))
    if (not lang) or len(lang) == 0:
        raise ValueError("Language not specified")
    if (not locs) or len(locs) == 0:
        raise ValueError("Localizations not specified")
    
    # Check the language and localization if it exists
    lang_info = drl_deserialize(json_path, lang)
    for target_loc_obj in locs:
        for source_loc_obj in lang_info.locs:
            target_loc = target_loc_obj[0]
            source_loc = source_loc_obj["loc"]
            if target_loc == source_loc:
                raise ValueError(f"Localization {target_loc} already exists")

    # Add the localization
    for target_loc_obj in locs:
        lang_info.locs.append({
            'loc': target_loc_obj[0],
            'text': target_loc_obj[1]
        })

    # Save the changes
    drl_genjson_final(json_path, lang_info)


def drl_add_lang(json_path: str, lang: str, cultures: list[str]):
    # User wants to add a language. Get necessary arguments.
    if (adt_conf.verbose):
        print("drl_add_lang(%s, %s, %s)" % (json_path, lang, cultures))
    if (not lang) or len(lang) == 0:
        raise ValueError("Language not specified")
    if (not cultures) or len(cultures) == 0:
        raise ValueError("Cultures not specified")
    
    # Create a JSON file if it doesn't exist, or error if it already exists.
    check_json_path = drl_getpath(json_path, lang)
    if os.path.isfile(check_json_path):
        raise ValueError(f"Language already exists at path {json_path}")
    drl_genjson(json_path, lang, cultures)


def drl_delete_culture(json_path: str, lang: str, cultures: list[str]):
    # User wants to delete a culture. Get necessary arguments.
    if (adt_conf.verbose):
        print("drl_delete_culture(%s, %s, %s)" % (json_path, lang, cultures))
    if (not lang) or len(lang) == 0:
        raise ValueError("Language not specified")
    if (not cultures) or len(cultures) == 0:
        raise ValueError("Cultures not specified")
    
    # Check the cultures if they already exist
    lang_info = drl_deserialize(json_path, lang)
    for target_culture in cultures:
        if target_culture not in lang_info.cultures:
            raise ValueError(f"Culture {target_culture} doesn't exist")

    # Delete the localization
    for culture in cultures:
        lang_info.cultures.remove(culture)

    # Save the changes
    drl_genjson_final(json_path, lang_info)


def drl_delete_loc(json_path: str, lang: str, locs: list[str]):
    # User wants to delete a localization. Get necessary arguments.
    if (adt_conf.verbose):
        print("drl_delete_loc(%s, %s, %s)" % (json_path, lang, locs))
    if (not lang) or len(lang) == 0:
        raise ValueError("Language not specified")
    if (not locs) or len(locs) == 0:
        raise ValueError("Localizations not specified")
    
    # Check the language and localization if it exists
    lang_info = drl_deserialize(json_path, lang)
    deleted_locs = []
    for target_loc_name in locs:
        for source_loc_obj in lang_info.locs:
            target_loc = target_loc_name
            source_loc = source_loc_obj["loc"]
            if target_loc == source_loc:
                deleted_locs.append(source_loc_obj)
    if len(deleted_locs) == 0:
        raise ValueError(f"Loc doesn't exist to delete {locs}")

    # Delete the localization
    for deleted_loc in deleted_locs:
        lang_info.locs.remove(deleted_loc)

    # Save the changes
    drl_genjson_final(json_path, lang_info)


def drl_delete_lang(json_path: str, lang: str, cultures: list[str]):
    # User wants to delete a language. Get necessary arguments.
    if (adt_conf.verbose):
        print("drl_delete_lang(%s, %s, %s)" % (json_path, lang, cultures))
    if (not lang) or len(lang) == 0:
        raise ValueError("Language not specified")
    if (not cultures) or len(cultures) == 0:
        raise ValueError("Cultures not specified")
    
    # Delete a JSON file if it exists, or error if it doesn't exist.
    json_path = drl_getpath(json_path, lang)
    if not os.path.isfile(json_path):
        raise ValueError(f"Language doesn't exist at path {json_path}")
    os.remove(json_path)


def drl_edit_culture(json_path: str, lang: str, cultures: list[str]):
    # User wants to edit a culture. Get necessary arguments.
    if (adt_conf.verbose):
        print("drl_edit_culture(%s, %s, %s)" % (json_path, lang, cultures))
    if (not lang) or len(lang) == 0:
        raise ValueError("Language not specified")
    if (not cultures) or len(cultures) == 0:
        raise ValueError("Cultures not specified")
    
    # Replace the culture list with another list
    lang_info = drl_deserialize(json_path, lang)
    lang_info.cultures = cultures

    # Save the changes
    drl_genjson_final(json_path, lang_info)


def drl_edit_loc(json_path: str, lang: str, locs: list[str]):
    # User wants to edit a localization. Get necessary arguments.
    if (adt_conf.verbose):
        print("drl_edit_loc(%s, %s, %s)" % (json_path, lang, locs))
    if (not lang) or len(lang) == 0:
        raise ValueError("Language not specified")
    if (not locs) or len(locs) == 0:
        raise ValueError("Localizations not specified")
    
    # Check the language and localization if it exists
    lang_info = drl_deserialize(json_path, lang)
    for target_loc_obj in locs:
        exists = False
        idx = 0
        for source_loc_obj in lang_info.locs:
            target_loc = target_loc_obj[0]
            target_text = target_loc_obj[1]
            source_loc = source_loc_obj["loc"]
            if target_loc == source_loc:
                exists = True
                lang_info.locs[idx]["text"] = target_text
            idx += 1
        if not exists:
            raise ValueError(f"Localization {target_loc_obj} doesn't exist")

    # Save the changes
    drl_genjson_final(json_path, lang_info)


def drl_report(json_path: str, lang: str):
    # User wants to make a report.
    if (adt_conf.verbose):
        print("drl_report(%s, %s)" % (json_path, lang))
    langs = [lang]
    if (not lang) or len(lang) == 0:
        langs = drl_lslangs(json_path)
    
    # Make a header
    report = "Languages report\n\n" + \
             f"  Languages: {langs}\n" + \
             f"  Language count: {len(langs)}\n\n"

    # List all language JSONs
    for lang in langs:
        # Get the JSON path
        json_file_path = drl_getpath(json_path, lang)
        report = report + \
            f"Language report for {lang}\n\n" + \
            f"  Language path: {json_file_path}\n"

        # Deserialize the language and make a report about it
        lang_info = drl_deserialize(json_path, lang)
        report = report + \
            f"  Language name: {lang_info.lang}\n" + \
            f"  Language cultures: {len(lang_info.cultures)} cultures\n" + \
            f"                     {lang_info.cultures}\n" + \
            f"  Language localizations: {len(lang_info.locs)} IDs\n"

        # List localizations
        for loc in lang_info.locs:
            report = report + \
                f"    - {loc['loc']}: {loc['text']}\n"
        report = report + "\n\n"

    # Print the report
    current_time = datetime.now()
    report = report + "Report generated on " + \
        f"{current_time}"
    print(report)


def drl_save(json_path: str, resx_path: str):
    # User wants to save JSON to .resx for .NET.
    if (adt_conf.verbose):
        print("drl_save(%s, %s)" % (json_path, resx_path))
    if (not resx_path) or len(resx_path) == 0:
        resx_path = json_path + '/Output'
    if not os.path.isdir(resx_path):
        os.makedirs(resx_path)

    # Get a list of available languages 
    langs = drl_lslangs(json_path)
    for lang in langs:
        # Deserialize the JSON
        lang_info = drl_deserialize(json_path, lang)
        if len(lang_info.cultures) == 0:
            continue

        # We now have the new path, we need to take the most generic culture by
        # taking a culture with the shortest ID so that .NET can use this
        # culture for string management according to
        # System.Globalization.CultureInfo.CurrentUICulture.
        shortest_culture = min(lang_info.cultures, key=len)
        if (adt_conf.verbose):
            print("shortest culture str found (%s)" % (shortest_culture))

        # We need to construct the file path for the resources file for this
        # language for .NET to be able to find them and automatically insert
        # them during the building phase.
        resource_path = drl_getresxpath(resx_path, shortest_culture)
        if (adt_conf.verbose):
            print("res obtained (%s)" % (resource_path))

        # Since we have the .resx file, we need to construct the XML file to
        # generate a valid resources file.
        resources_file = """<?xml version="1.0" encoding="utf-8"?>
<root>
    <xs:schema id="root" xmlns="" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xs:import namespace="http://www.w3.org/XML/1998/namespace" />
    <xs:element name="root" msdata:IsDataSet="true">
        <xs:complexType>
        <xs:choice maxOccurs="unbounded">
            <xs:element name="metadata">
            <xs:complexType>
                <xs:sequence>
                <xs:element name="value" type="xs:string" minOccurs="0" />
                </xs:sequence>
                <xs:attribute name="name" use="required" type="xs:string" />
                <xs:attribute name="type" type="xs:string" />
                <xs:attribute name="mimetype" type="xs:string" />
                <xs:attribute ref="xml:space" />
            </xs:complexType>
            </xs:element>
            <xs:element name="assembly">
            <xs:complexType>
                <xs:attribute name="alias" type="xs:string" />
                <xs:attribute name="name" type="xs:string" />
            </xs:complexType>
            </xs:element>
            <xs:element name="data">
            <xs:complexType>
                <xs:sequence>
                <xs:element name="value" type="xs:string" minOccurs="0" msdata:Ordinal="1" />
                <xs:element name="comment" type="xs:string" minOccurs="0" msdata:Ordinal="2" />
                </xs:sequence>
                <xs:attribute name="name" type="xs:string" use="required" msdata:Ordinal="1" />
                <xs:attribute name="type" type="xs:string" msdata:Ordinal="3" />
                <xs:attribute name="mimetype" type="xs:string" msdata:Ordinal="4" />
                <xs:attribute ref="xml:space" />
            </xs:complexType>
            </xs:element>
            <xs:element name="resheader">
            <xs:complexType>
                <xs:sequence>
                <xs:element name="value" type="xs:string" minOccurs="0" msdata:Ordinal="1" />
                </xs:sequence>
                <xs:attribute name="name" type="xs:string" use="required" />
            </xs:complexType>
            </xs:element>
        </xs:choice>
        </xs:complexType>
    </xs:element>
    </xs:schema>
    <resheader name="resmimetype">
    <value>text/microsoft-resx</value>
    </resheader>
    <resheader name="version">
    <value>2.0</value>
    </resheader>
    <resheader name="reader">
    <value>System.Resources.ResXResourceReader, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
    </resheader>
    <resheader name="writer">
    <value>System.Resources.ResXResourceWriter, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
    </resheader>
</root>
"""

        # Iterate through all localizations
        xml_doc = XmlElementTree.fromstring(resources_file)
        xml_doc_tree = XmlElementTree.ElementTree(xml_doc)
        for loc in lang_info.locs:
            # Get localization ID and value
            loc_id = loc["loc"]
            loc_value = loc["text"]
            if (adt_conf.verbose):
                print("added loc (%s, %s)" % (loc_id, loc_value))

            # Add a data component.
            data_elem = XmlElementTree.Element('data', name=loc_id)
            data_elem.set("{http://www.w3.org/XML/1998/namespace}space",
                          "preserve")
            value_elem = XmlElementTree.SubElement(data_elem, 'value')
            value_elem.text = loc_value
            xml_doc.append(data_elem)

        # Save the XML
        XmlElementTree.indent(xml_doc_tree, space='  ')
        xml_doc_tree.write(resource_path,
                           encoding='utf8',
                           xml_declaration=True)
