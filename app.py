import requests

class PublicNeeds(object):
    def __init__(self):
        pass

    def requesting(self, page=1, limit=1000, last_page=4):
        '''
        Kwarg page will be used in for to iterate from this number to last_page
        Limit is also used with default value of 100 as recommended in api docs.
        For now i willl use self.requested_pages to append
        '''
        requested_pages = []
        for dictionary in range(page, last_page):
            req = requests.get('https://api-v3.mojepanstwo.pl/dane/zamowienia_publiczne.json?page={}&limit={}'.format(page, limit)).json()
            page+=1
            requested_pages.append(req)
            return(requested_pages)

    def service_information(self, region):
        requested_jsons = self.requesting()
        without_executor = []
        output_dict = {}
        for single_json in requested_jsons:
            for orders in single_json["Dataobject"]:
                if orders["data"]["zamowienia_publiczne.zamawiajacy_wojewodztwo"] == region:
                    output_dict[orders["data"]["zamowienia_publiczne.nazwa"]] = {'rodzaj robot': orders["data"]["zamowienia_publiczne_rodzaje.nazwa"], 'wykonawca' : orders["data"]["zamowienia_publiczne.wykonawca_str"]}
        return output_dict

def main():
    print('done')
    pubs = PublicNeeds()

if __name__ == '__main__':
    main()
