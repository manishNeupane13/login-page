from bs4 import BeautifulSoup
import requests

daily_share_data = []
dictfile_list = {}



def request_method(page_number):

    page_request = requests.get(
        f'http://www.nepalstock.com/main/todays_price/index/{page_number}/').text

    website_html_content = BeautifulSoup(page_request, 'lxml')

    table_contents = website_html_content.find_all(
        "table", class_='table table-condensed table-hover')
    return table_contents


# list for storing all the share data of each companies
list_of_table_data = []
# getting heading of the table


def get_heading_list(table_contents):
    for inside_table in table_contents:
        table_header = inside_table.find_all("tr", class_="unique")[
            0].text.strip().split("\n")
    return(table_header)
# getting content of table data


def get_table_data(table_contents):

    for count_table_row in range(2, 22):
        for inside_table in table_contents:
            table_data = inside_table.find_all("tr")[count_table_row].text.strip().split("\n")

            list_of_table_data.append(table_data)
    return(list_of_table_data)




def get_jason_file(heading_list,table_data):
    global daily_share_data, dictfile_list

    for list_row_value in table_data:
        for count in range(len(heading_list)):
            dictfile_list[heading_list[count]] = list_row_value[count]
        daily_share_data.append(dict(dictfile_list))

    return((daily_share_data))
def get_jason_data():
    for page_number in range(1,12):
        # page_number = int(input("Enter the page number of transaction :: "))
        table_contents = request_method(page_number)
        heading_list = (get_heading_list(table_contents))
        table_data = (get_table_data(table_contents))
    return get_jason_file(heading_list, table_data)

if __name__ == '__main__':
    get_jason_data()

   
