from sqlalchemy.orm import declarative_base

Base = declarative_base()

#LEVEL UP- setup separate base model
#Purpose: 
#separation of concerns- cleaner for larger projects, and keeps database model separate from FastApi models
#Reuse & Extend- can easily reuse this base model across multiple modules or applications within the project, allows you to extend the base model with additional functionality or customizations specific to your project requirements without affecting other parts of the application.