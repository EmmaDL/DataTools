import unittest

from ProjetFinal import extract_movie_info, get_html_from_link


def test_extract_movie_info():
    #Given
    link = f'https://www.senscritique.com//film/12_hommes_en_colere/370894'
    html = get_html_from_link(link)

    expected_output = ('12 hommes en colère', '(1957)', '8.7', 'Sidney Lumet', 'Policier', 'Henry Fonda')
    
    #When
    output = extract_movie_info(html)
    
    #Then
    assert expected_output == output