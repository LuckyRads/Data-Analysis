class EmployeeAttrition():

    def __init__(self, age, attrition, business_travel, daily_rate, department, distance_from_home, education, education_field):
        self.__age = age
        self.__attrition = attrition
        self.__business_travel = business_travel
        self.__daily_rate = daily_rate
        self.__department = department
        self.__distance_from_home = distance_from_home
        self.__education = education
        self.__education_field = education_field

    def get_age(self):
        return self.__age

    def get_attrition(self):
        return self.__attrition

    def get_business_travel(self):
        return self.__business_travel

    def get_daily_rate(self):
        return self.__daily_rate

    def get_department(self):
        return self.__department

    def get_distance_from_home(self):
        return self.__distance_from_home

    def get_education(self):
        return self.__education

    def get_education_field(self):
        return self.__education_field
