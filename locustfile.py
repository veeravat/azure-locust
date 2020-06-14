from locust import TaskSet, task, between
from locust.contrib.fasthttp import FastHttpLocust

class MyTaskSet(TaskSet):
    @task
    def index(self):
        response = self.client.get("/")
        response = self.client.get("/fetch-data")

class MyLocust(FastHttpLocust):
    task_set = MyTaskSet
    wait_time = between(1, 60)