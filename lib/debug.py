#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy_sandbox import Student

Base = declarative_base()


engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()
