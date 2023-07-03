import streamlit as st
from bs4 import BeautifulSoup
import re
import pyperclip

count = 0

# st.sidebar.title('Navigation')
# if st.sidebar.button('Go to Page 2'):
#     def display_page_2():
#         st.title('Page 2')
#         st.write('This is the content of Page 2')
# if st.sidebar.button('Go to Page 2'):
#     display_page_2()

def copy_code_to_clipboard(code):
    pyperclip.copy(code)
    st.success("Code copied to clipboard!")

def clean_html(clean):
    clean_code = clean.replace("<table>",'<table class="table table-striped style_table">')


    one = clean_code.replace('<td><p>','<td>')
    two = one.replace('</p></td>','</td>')
    three  = two.replace('\n','')
    four = three.replace('<li>','<li style="text-align: justify;">')
    five = four.replace('<p>','<p style="text-align: justify;">')
    six = five.replace('<td><strong>','<th>')
    seven = six.replace('</strong></td>','</th>')

    eight = seven.replace('<td><strong>','<th>')
    nine = eight.replace('</strong></td>','</th>')
    nine = nine.replace('<td> <p style="text-align: justify;">','<td>')
    nine = nine.replace('</p> </td>','</td>')
    nine = nine.replace('<td><strong>','<th>')
    nine = nine.replace('</strong></td>','</th>')

     ### code for collegedunia news articles
    nine = nine.replace('<p style="text-align: justify;"><strong>Check: </strong>','<p><span style="color: #ff0000;"><strong>Check: </strong></span>')
    nine = nine.replace('<p style="text-align: justify;"><strong>Check:</strong>','<p><span style="color: #ff0000;"><strong>Check: </strong></span>')

    nine = re.sub('''<p style=text-align: justify;"><strong>Check IELTS writing (.*?) samples:</strong></p>''','''<p><span style="color: #ff0000;"><strong>Check IELTS writing \\1 samples:</strong></span></p>''',nine)
    nine = nine.replace('<p style="text-align: justify;"><strong>Explanation</strong>: ','<p><span style="color: #ff0000;"><strong>Explanation</strong>:</span> ')
    nine = nine.replace('<p style="text-align: justify;"><strong>Supporting statement</strong>: ','<p><span style="color: #ff0000;"><strong>Supporting statement</strong>:</span>')
    nine = nine.replace('<p style="text-align: justify;"><strong>Answer</strong>:','<p><span style="color: #ff0000;"><strong>Answer</strong>:</span>')
    nine = nine.replace('<p style="text-align: justify;"><strong>Keywords</strong>: ','<p><span style="color: #ff0000;"><strong>Keywords</strong>:</span> ')
    nine = nine.replace('</h3>','</h3><div style="max-height: 85vh; overflow-y: auto; margin-bottom: 20px;">')
    nine = nine.replace('<p style="text-align: justify;"><strong>Keyword location</strong>: ','<p><span style="color: #ff0000;"><strong>Keyword location</strong>:</span> ')
    # <p style="text-align: justify;"><strong>Check IELTS writing samples:</strong></p>

    return nine

def increment_id(match):
    global count
    count += 1
    tag_name = match.group(1)
    return f'<{tag_name} id="{count}">'

# Streamlit app
def main():
    st.title("News Code HTML Generator")

    # Input text box
    clean = st.text_input("Enter a string")

    # Manipulate button
    if st.button("Manipulate"):
        # Check if input string is empty
        if not clean:
            st.warning("Please enter a string.")
        else:
            result = clean_html(clean)
            from bs4 import BeautifulSoup
            result = result.replace('<p><strong>Also Check:</strong>','<p style="text-align: justify;"><span style="color:#FF0000;"><strong>Also Check:</strong></span></p>')
            result = result.replace('<h1>','')
            result = result.replace('<h1>','')
            result = result.replace('<p>','<p style="text-align: justify;">')
            result = result.replace('<p style="text-align: justify;"><strong>Also Check:</strong>','<p style="text-align: justify;"><span style="color:#FF0000;"><strong>Also Check:</strong></span>')
            soup = BeautifulSoup(result, 'html.parser')


            for a_tag in soup.find_all('a'):
                if not a_tag.has_attr('target'):
                    a_tag['target'] = '_blank'

            # if str(soup).find('collegedunia')>0:
            #     st.write('collegedunia links are present')
            # else:
                # var1= toc_create(soup)
                # var1 = str(var1)
                var2 = str(soup)
                # var2 = var2.replace('<')
                # var3 = "{}  {} ".format(var1, var2)

                st.code(var2, language='html')

                if st.button("Copy Code"):
                    copy_code_to_clipboard(var2)

if __name__ == "__main__":
    main()
