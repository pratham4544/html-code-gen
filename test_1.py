import streamlit as st
from bs4 import BeautifulSoup
import re
import pyperclip
count = 0
def clean_html(clean):

    zero = re.sub('<td>\<p>(.*?)</p><p>(.*?)</p></td>','<th>\\1</<br />\\2</th>',clean)
    clean_code = zero.replace("<table>",'<table class="table table-striped style_table">')
    one_clean = clean_code.replace('?</p>','?</strong></p><div class="liv">')
    two_clean = one_clean.replace('<p>Ques','</div><p class="accordio" style="text-align: justify;"><strong>Ques')
    three_clean = two_clean.replace('<td><p>','<td>')
    four_clean = three_clean.replace('</p></td>','</td>')
    five_clean  = four_clean.replace('\n','')
    five_clean_1 = five_clean.replace('<li>','<li style="text-align: left;">')
    five_clean_2 = five_clean_1.replace('<p>','<p style="text-align: justify;">')
    five_clean_3 = five_clean_2.replace('<td><strong>','<th>')
    five_clean_4 = five_clean_3.replace('</strong></td>','</th>')
    six_clean = five_clean_4.replace('<table>','<table class="table table-striped style_table">')
    seven = six_clean.replace('<h2>','\n\n\n<h2>')
    eight = seven.replace('<h3>','\n\n\n<h3>')
    
    nine = re.sub('<h2>(.*?) Courses and Eligibility</h2>', '</div><div class="cdcms_courses">\n<h2>\\1 Courses and Eligibility</h2>', eight)
    ten = re.sub('<h2>(.*?) FAQs</h2>','</div><div class="cdcms_faqs">\n<h2>\\1 FAQs</h2>', nine)
    eleven = re.sub('<h2>(.*?) Cutoff 2023</h2>','</div><div class="cdcms_cut_off">\n<h2> \\1 Cutoff 2023</h2>', ten)
    tweleve = eleven.replace('FAQs</h2>','FAQs</h2>\n<div id="faq_id">')
    thirteen = re.sub('<h2>(.*?) Important Dates</h2>','<div style="background: #eee; border: 1px solid #ccc; padding: 5px 10px;"><strong>Table of Content</strong>\n\n<ol style="margin-bottom: 0px;" type="1">\n\t<li><a href="#1">RTMNU Nagpur Admission 2023: Important Dates </a></li>\n\t<li><a href="#2">RTMNU Nagpur Admission 2023: Courses &amp; Eligibility </a></li>\n\t<li><a href="#3">RTMNU Nagpur Admission 2023: Cut Off 2023 </a></li>\n</ol>\n\n<p style="margin-left: 40px; margin-bottom: 0px;">3.1&nbsp;<a href="#4">MHT-CET Cutoff 2022</a></p>\n\n<p style="margin-left: 40px; margin-bottom: 0px;">3.2&nbsp;<a href="#5">MAH-MCA-CET Cutoff 2022</a></p>\n\n<ol start="4" style="list-style-type: decimal; margin-bottom: 0px;" type="1">\n\t<li><a href="#6">RTMNU Nagpur Admission 2023: FAQs </a></li>\n</ol>\n</div>\n</div>\n\n<div class="cdcms_section1">\n<h2>\\1 Admission 2023: Important Dates</h2>', tweleve)
    fourteen = re.sub('Ans','<strong>Ans</strong>', thirteen)
    fourteen_1 = fourteen.replace('<td><strong>','<th>')
    fourteen_2 = fourteen_1.replace('</strong></td>','</th>')
    
    fourteen_31 = re.sub('<h2>(.*?) Highlights</h2>','<div class="cdcms_college_highlights">\n<h2> \\1 Highlights</h2>', fourteen_2)
    fourteen_3 = re.sub('<h2>(.*?) Rankings</h2>','</div><div class="cdcms_ranking">\n<h2> \\1 Rankings</h2>', fourteen_31)
    fourteen_4 = re.sub('<h2>(.*?) Courses &amp; Fees</h2>','</div><div class="cdcms_courses">\n<h2> \\1 Courses &amp; Fees</h2>', fourteen_3)
    fourteen_5 = re.sub('<h2>(.*?) Cutoff</h2>','</div><div class="cdcms_cut_off">\n<h2> \\1 Cutoff</h2>', fourteen_4)
    fourteen_6 = re.sub('<h2>(.*?) Placement</h2>','</div><div class="cdcms_placement">\n<h2> \\1 Placement</h2>', fourteen_5)
    fourteen_7 = re.sub('<h2>(.*?) Scholarships</h2>','</div><div class="cdcms_scholarships">\n<h2> \\1 Scholarships</h2>', fourteen_6)
    fourteen_8 = re.sub('<h2>(.*?) Facilities</h2>','</div><div class="cdcms_section1">\n<h2> \\1 Facilities</h2>', fourteen_7)
    fourteen_9 = re.sub('<h2>Comparison:','</div><div class="cdcms_comparison">\n<h2> Comparison: ', fourteen_8)
    fourteen_10 = fourteen_9.replace('<p style="text-align: justify;"><strong>Ques','</div><p class="accordio" style="text-align: justify;"><strong>Ques')
    fourteen_11 = fourteen_10.replace('?</strong></p>','?</strong></p><div class="liv">')
    fourteen_12 = re.sub('<h2>(.*?) Ranking</h2>','</div><div class="cdcms_ranking">\n<h2> \\1 Rankings</h2>', fourteen_11)
    fourteen_13 = re.sub('<h2>(.*?) Placements</h2>','</div><div class="cdcms_placement">\n<h2> \\1 Placements</h2>', fourteen_12)
    fourteen_14 = re.sub('<h2>(.*?) and Fees</h2>','</div><div class="cdcms_courses">\n<h2> \\1 and Fees</h2>', fourteen_13)
    fourteen_15 = re.sub('<h2>(.*?) Scholarship</h2>','</div><div class="cdcms_scholarships">\n<h2> \\1 Scholarships</h2>', fourteen_14)
    fourteen_16 = fourteen_15.replace('<br/>','')
    fourteen_17 = fourteen_16.replace('<p></p>','')
    fourteen_18 = fourteen_17.replace('<div class="liv"><div class="liv">','<div class="liv">')
    fourteen_19 = fourteen_18.replace('<div id="faq_id"></div>','<div id="faq_id">')
    fourteen_20 = re.sub('<h2>(.*?) Facilities</h2>','</div><div class="cdcms_section1">\n<h2> \\1 Facilities</h2>',fourteen_19)
    
    
    fifteen = re.sub('<h1>','<div class="cdcms_section2">\n<h1>', fourteen_20)
    fifteen = re.sub('<h2>(.*?) Vs (.*?)</h2>','</div><div class="cdcms_comparison">\n<h2>\\1 Vs \\2', fourteen_20)
    fifteen = re.sub('<h2>(.*?) VS (.*?)</h2>','</div><div class="cdcms_comparison">\n<h2>\\1 Vs \\2', fourteen_20)
    fifteen = re.sub('<h2>(.*?) vs (.*?)</h2>','</div><div class="cdcms_comparison">\n<h2>\\1 vs \\2', fourteen_20)
    fifteen = re.sub('</div><div class="cdcms_section1">\n</div><div class="cdcms_section1">','</div><div class="cdcms_section1">\n',fifteen)
    return fifteen   

def increment_id(match):
    global count
    # count=0
    count += 1
    tag_name = match.group(1)
    return f'<{tag_name} id="{count}">'

def toc_create(soup):
    toc = ''
    
    headings = soup.find_all('h2')
    
    for heading in headings:
        toc+= f'<li><a href="#{heading.get("id")}">{heading.text}</a></li>\n'
    toc += '</ol>\n'
    

    heading_2 = soup.find_all('h3')
    toc_2 = '\n'
    for heading in heading_2:
        toc_2+= f'<p style="margin-left: 40px; margin-bottom: 0px;">3.1 <a href="#{heading.get("id")}">{heading.text}</a></p>\n\n'
    



    con = '<div style="background: #eee; border: 1px solid #ccc; padding: 5px 10px;"><strong>Table of Content</strong>\n<ol style="margin-bottom: 0px;" type="1">\n'
    cat = '''</div>
    </div>
    <div class="cdcms_ranking">


    <ol start="4" style="list-style-type: decimal; margin-bottom: 0px;" type="1">


    '''

    lin = con+toc+toc_2+cat

    return lin


# Streamlit app
def main():
    st.title("College Overview Code HTML Generator")

    # Input text box
    clean = st.text_input("Enter a string")

    # Manipulate button
    if st.button("Manipulate"):
        # Check if input string is empty
        if not clean:
            st.warning("Please enter a string.")
        else:
            clean_2 = clean_html(clean)
            count = 0
            result = re.sub(r'<(h2|h3)>', increment_id, clean_2)


            soup = BeautifulSoup(result, 'html.parser')


            for a_tag in soup.find_all('a'):
                if not a_tag.has_attr('target'):
                    a_tag['target'] = '_blank'

            if str(clean).find('collegedunia')>0:
                print('collegedunia links are present')
            else:    
                var1= toc_create(soup)
                var1 = str(var1)
                var2 = str(soup)
                var3 = "{}  {} ".format(var1, var2)
                pyperclip.copy(var3)
                # print(f'Copied Code Succesfully...\n\n\n')
                # toc_create(soup)
                # print(soup)
                st.write('Copied Code Succesfully...\n\n\n',var3)

if __name__ == "__main__":
    main()
