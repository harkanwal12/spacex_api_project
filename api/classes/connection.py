from flask import current_app as app
import requests
from api.classes.entities import CompanyInfo, LaunchSite


class SpacexConnection:
    def __init__(self):
        self.conf = app.config
        self.base_url = self.conf["BASE_URL"]

    def get_company_info(self) -> CompanyInfo:
        url = self.base_url + "/v4/company"
        # TODO add exception handling here
        response = requests.get(url, verify=False)
        company_data = response.json()

        return CompanyInfo(**{k: company_data[k] for k in {"name", "founded"}})
