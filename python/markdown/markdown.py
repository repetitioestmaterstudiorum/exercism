import re

# ------------

def parse(markdown):
    lines = markdown.splitlines() # use specific function if exists
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        print("-------- line: ", i)
        if re.match('###### (.*)', i): # "is not none" is redundant
            i = f"<h6>{i[7:]}</h6>" # f strings are easier to read than string concatenations
        elif re.match('## (.*)', i):
            i = f"<h2>{i[3:]}</h2>"
        elif re.match('# (.*)', i):
            i = f"<h1>{i[2:]}</h1>"
        m = re.match(r'\* (.*)', i)
        print(m)
        if m:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = True
                i = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                if is_italic:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = '<p>' + i + '</p>'
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res

# --- tests to keep passing (for AREPL during development)
assert(parse("This will be a paragraph") == "<p>This will be a paragraph</p>")
assert(parse("_This will be italic_") == "<p><em>This will be italic</em></p>")
assert(parse("__This will be bold__") == "<p><strong>This will be bold</strong></p>")
assert(parse("This will _be_ __mixed__") == "<p>This will <em>be</em> <strong>mixed</strong></p>")
assert(parse("# This will be an h1") == "<h1>This will be an h1</h1>")
assert(parse("## This will be an h2") == "<h2>This will be an h2</h2>")
assert(parse("###### This will be an h6") == "<h6>This will be an h6</h6>")
assert(parse("* Item 1\n* Item 2") == "<ul><li>Item 1</li><li>Item 2</li></ul>")
assert(parse("# Header!\n* __Bold Item__\n* _Italic Item_") == "<h1>Header!</h1><ul><li><strong>Bold Item</strong></li><li><em>Italic Item</em></li></ul>")
assert(parse("# This is a header with # and * in the text") == "<h1>This is a header with # and * in the text</h1>")
assert(parse("* Item 1 with a # in the text\n* Item 2 with * in the text") == "<ul><li>Item 1 with a # in the text</li><li>Item 2 with * in the text</li></ul>")
assert(parse("This is a paragraph with # and * in the text") == "<p>This is a paragraph with # and * in the text</p>")
assert(parse("# Start a list\n* Item 1\n* Item 2\nEnd a list") == "<h1>Start a list</h1><ul><li>Item 1</li><li>Item 2</li></ul><p>End a list</p>")