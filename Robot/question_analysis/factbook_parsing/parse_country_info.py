from pathlib import Path
import re
import pickle

from bs4 import BeautifulSoup


def _save_countries_info(countries):
    with open('countries_dump', 'wb') as saved_countries:
        pickle.dump(countries, saved_countries)


def _data_has_subset(tag):
    to_remove = ['\n', ' ']
    contents = [child for child in tag.td.contents if child not in to_remove]
    return len(contents) > 1


def _has_span_as_child(tag):
    return 'span' in [child.name for child in tag.children]


def _parse_data_with_subset(data_block):
    element = data_block.td.contents[1]
    field_info = []

    while element != '\n' and element is not None:
        if element.name == 'div':
            info_block = _parse_div(element)
            if element.next_sibling == '\n':
                element = element.next_sibling
        else:
            element, info_block = _parse_span(element)
        field_info.append(info_block)
        element = element.next_sibling
    return field_info


def _parse_div(div_element):

    if _has_span_as_child(div_element):
        info_name, info_details = div_element.text.split(':', 1)
        info_name = info_name.replace(':', '').strip()
        info_details = info_details.strip()
        info_block = {info_name: info_details}
    else:
        """
        if div_element.text.find(':') != -1 and div_element.text.find('%') == -1:
            print(div_element.prettify())
        """
        info_block = div_element.text
        info_block = info_block.strip()

    return info_block


def _parse_span(span_element):
    info_name = span_element.text
    span_element = span_element.find_next('span')
    info_details = span_element.text
    info_name = info_name.replace(':', '').strip()
    info_details = info_details.strip()
    return span_element, {info_name: info_details}


def _parse_single_subset(field_data):
    if _has_span_as_child(field_data.td.div):
        info_name, info_block = field_data.td.div.text.split(':', 1)
        info_name = info_name.strip()
        info_block = info_block.strip()
        field_info = {info_name: info_block}
    else:
        field_info = field_data.td.div.text.strip()
    return field_info


def _format_field_info_list(field_info):
    str_position = []
    for index, item in enumerate(field_info):
        if isinstance(item, str):
            str_position.append(index)

    if len(str_position) == 1:
        field_info[str_position[0]] = {'description': field_info[str_position[0]]}
        str_position = []

    if not str_position:
        new_field_info = {}
        for item in field_info:
            new_field_info.update(item)
        field_info = new_field_info
    return field_info


def _parse_panels(panels):
    country_info = {}
    for panel in panels:
        for child in panel.find('table').contents[1::6]:
            field_name = child.td.div.a.text.replace(':', '').strip()
            field_data = child.next_sibling.next_sibling

            if _data_has_subset(field_data):
                field_info = _parse_data_with_subset(field_data)
                field_info = _format_field_info_list(field_info)
            else:
                field_info = _parse_single_subset(field_data)

            country_info[field_name] = field_info
    return country_info


def parse_country_info():
    countries = {}
    country_data_dir = Path('./factbook/geos')

    for country_file in country_data_dir.glob('*.html'):
        with country_file.open() as country_data:
            country_soup = BeautifulSoup(country_data, 'lxml')
            country_name = country_soup.find(class_='region_name1').text
            panels = country_soup.find_all(id=re.compile('CollapsiblePanel1'))
            countries[country_name] = _parse_panels(panels)
    _save_countries_info(countries)
parse_country_info()