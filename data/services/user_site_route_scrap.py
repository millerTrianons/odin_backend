from presentation.user_site_scrap_data import UserSiteScrapData

class UserSiteScrapService:
    def __init__(self) -> None:
        pass

    async def scrap_user_site_route(self,  content: list[UserSiteScrapData]) -> object:
        scraped_items = []

        for item in content:
            print(item)
        

#
       # site = requests.get(url, headers = headers)
#
       # soup = BeautifulSoup(site.content, 'html.parser')
#
       # page_header = soup.find('div', {'class': 'fusion-header'})
#
       # print(page_header)

       # print(content)

        return {}