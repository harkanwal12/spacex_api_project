from flask import current_app as app, abort
import requests
import pandas as pd


class SpacexConnection:
    def __init__(self):
        self.conf = app.config
        self.base_url = self.conf["BASE_URL"]

    def fetch_data(self, url, fields=None) -> dict | list[dict]:
        url = self.base_url + url
        try:
            response = requests.get(url, verify=False)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                description = "No data found"
                app.logger.info(description)
                abort(404, description=description)
            app.logger.exception(
                "Error when fetching data from API", exc_info=e
            )
            raise e

        response = response.json()

        if fields:
            if isinstance(response, list):
                response = [
                    {k: d[k] for k in fields if k in d} for d in response
                ]
            else:
                response = {k: response[k] for k in fields}

        return response

    def get_all_launches(self) -> pd.DataFrame:
        url = "/v4/launches"
        fields = ["name", "date_utc", "launchpad", "success", "id", "details"]
        launches = self.fetch_data(url, fields)

        return pd.DataFrame.from_dict(launches)

    def get_all_launchpads(self) -> pd.DataFrame:
        url = "/v4/launchpads"
        fields = {
            "full_name",
            "locality",
            "region",
            "timezone",
            "id",
            "details",
            "status",
            "name",
        }
        launchpads = self.fetch_data(url, fields)
        return pd.DataFrame.from_dict(launchpads)
