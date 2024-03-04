[Apple CEOs Redo](https://ccs-full-stack-web-dev.netlify.app/docs/cohorts/cohort17/lectures/week9/day1/EXERCISES#apple-ceos-redo)

## Base -Single Base Class or Separate Base Model?

In SQLAlchemy, Base is a variable name for a base model that is assigned to the result of declarative_base() function call. The base model defines the base class for our models. Its usage remains the same regardless of how you structure your code (Single file or Separate):

    from sqlalchemy.orm import declarative_base
    Base = declarative_base()

1. Define the Base model and Base class(s) in one single file #models.py
   - this is good for simpler apps or when following a more concise coding style

2. Separate the Base model from the our base class(s) by defining the base model in a separate module #Base.py and then import it in the module where we define our base class(s) #CEO. To import it we must specify the directory name, the file name, and the model.
   - this is good in larger apps, broken down organization, and separation of concerns. 
