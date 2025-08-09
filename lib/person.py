#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self,name="Unknown",job="Engineer"): # Constructor method
        self.name = name
        if not isinstance(name, str) or len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self.name = name.title()

        self.job = job

    @property
    def job(self):
        return self._job        
    
    @job.setter
    def job(self, value):
        if value not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self._job = value

