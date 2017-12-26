import requests

class PublicNeeds(object):
    def __init__(self):
        pass

    def requesting_from_api(self, page=1, limit=1000, last_page=4):
        '''
        Method is taking 3 inputs in form of int, returning list of jsons.
        Input:
            page == this parameter is used for needs of iteration.
            Iteration starts exactly from page1 according to kwarg
            limit == this parameter is responsible to narrow output of each page.
            By default we are using limit=1000
            last_page == this parameter is used as the end of in range iteration.
            By default its set to 4. It seems that there are no more than 3 pages in one region.
        Output:
            As output we are taking list of jsons requested in iteration.
        '''
        requested_pages = []
        for public_data_json in range(page, last_page):
            req = requests.get('https://api-v3.mojepanstwo.pl/dane/zamowienia_publiczne.json?page={}&limit={}'.format(page, limit)).json()
            page+=1
            requested_pages.append(req)
        return(requested_pages)

    def service_information(self, region):
        requested_jsons = self.requesting_from_api()
        json_for_api = {}
        for single_json in requested_jsons:
            for orders in single_json["Dataobject"]:
                if orders["data"]["zamowienia_publiczne.zamawiajacy_wojewodztwo"] == region:
                    json_for_api[orders["data"]["zamowienia_publiczne.nazwa"]] = {'rodzaj robot': orders["data"]["zamowienia_publiczne_rodzaje.nazwa"], 'wykonawca' : orders["data"]["zamowienia_publiczne.wykonawca_str"]}
        return json_for_api

def main():
    PubNeed = PublicNeeds()
    PubNeed.requesting_from_api()

if __name__ == '__main__':
    main()
