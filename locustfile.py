from locust import HttpUser, task, between

class PruebaAPI(HttpUser):
    @task
    def obtener(self):
        self.client.get("https//thesimpsonapi.com/api/characters/1")