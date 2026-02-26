class Repository:
    def from_api(self, response: dict) -> dict:
        repos = dict()
        for index, item in enumerate(response):
            repos.update({
                index: {
                    'name': item.get('name'),
                    'full_name': item.get('full_name'),
                    'html_url': item.get('html_url'),
                    'language': item.get('language'),
                    'stargazers_count': item.get('stargazers_count'),
                    'forks_count': item.get('forks_count'),
                    'updated_at': item.get('updated_at'),                
                }})
        return repos
