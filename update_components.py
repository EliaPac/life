import os

if __name__ == '__main__':
    root_dir = './'
    for item in os.listdir(root_dir):
        current_dir = os.path.join(root_dir, item)
        if item in ('it', 'en') and os.path.isdir(current_dir):
            components_dir = os.path.join(root_dir, item, 'components')
            components_dir = components_dir if os.path.isdir(components_dir) else None
            if components_dir:
                footer = os.path.join(components_dir, 'footer.html')
                footer = footer if os.path.isfile(footer) else None
                header = os.path.join(components_dir, 'header.html')
                header = header if os.path.isfile(header) else None
                navbar = os.path.join(components_dir, 'navbar.html')
                navbar = navbar if os.path.isfile(navbar) else None
                file_names = [file_name for file_name in os.listdir(current_dir) if file_name.endswith('.html')]
                for file_name in file_names:
                    file_path = os.path.join(current_dir, file_name)
                    with open(file_path, 'r') as file_handle:
                        file_html = file_handle.readlines()
                        header_start = None
                        header_end = None
                        nav_start = None
                        nav_end = None
                        for i, line in enumerate(file_html):
                            header_start = i + 1 if line.strip() == '<!-- INSERT HEADER HERE -->' else header_start
                            header_end = i if line.strip() == '<!-- END OF HEADER -->' else header_end
                            nav_start = i + 1  if line.strip() == '<!-- INSERT NAVBAR HERE -->' else nav_start
                            nav_end = i + 1  if line.strip() == '<!-- END OF NAVBAR -->' else nav_end
                        print(header_start)
                        print(nav_start)
                    if header_start:
                        with open(header, 'r') as _:
                            header_html = _.readlines()
                            header_html[-1] = header_html[-1]+'\n'
                        file_html = file_html[:header_start] + header_html + file_html[header_end:]
                        header_len = len(header_html)-(header_end-header_start-1)-1
                    else:
                        print(f'Header not inserted in {file_path}')
                        header_len = 0
                    if nav_start:
                        with open(navbar, 'r') as _:
                            nav_html = _.readlines()
                            nav_html[-1] = nav_html[-1]+'\n'
                        file_html = file_html[:nav_start+header_len] + nav_html + file_html[nav_end+header_len-1:]
                    else:
                        print(f'Navbar not inserted in {file_path}')
                    with open(file_path, 'w') as file_handle:
                        file_handle.writelines(file_html)
            else:
                raise FileNotFoundError('Folder "components" was not found in {current_dir}')
