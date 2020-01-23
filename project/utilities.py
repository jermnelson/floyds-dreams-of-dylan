__author__ = "Jeremy Nelson"

from lxml import etree

def add_item(channel, title, description, song_slug):
    item = etree.SubElement(channel, "item")
    title_element = etree.SubElement(item, "title")
    title_element.text = title
    desc = etree.SubElement(item, "description")
    desc.text = description
    add_enclosure(item, song_slug)

def add_enclosure(item, song_slug):
    enclosure = etree.SubElement(item,
        "enclosure",
	attrib={ "url": f"/dylan_covers/{song_slug}",
		 "type": "audio/mp3"})
