from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Date, Integer, Numeric

engine = create_engine('postgresql://dbuser:dbpassword@sqlalchemy-orm-psql/sqlalchemy')

# use session_factory() to get a new Session
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()

def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()

class Record(Base):
    __tablename__ = 'rdat_record'

    id = Column(Integer, primary_key=True)
    str_val = Column(String)
    date_val = Column(Date)
    int_val = Column(Integer)
    num_val = Column(Numeric)

    def __init__(self, str_val, date_val, int_val, num_val):
        self.str_val = str_val
        self.date_val = date_val
        self.int_val = int_val
        self.num_val = num_val


class RecordDatabase:

    def __init__(self):
        pass

    def get_records(self):
        records = self._get_records()
        if len(records) == 0:
            self._create_records()
        ecords = self._get_records()
        return records

    def _get_records(self):
        session = session_factory()
        record_query = session.query(Record)
        session.close()
        return record_query.all()

    def _create_recorde(self):
        session = session_factory()
        r1 = Record("str val 1", date(1984, 10, 20), 182, 84.5)
        r2 = Record("str val 2", date(1990, 5, 17), 173, 90)
        session.add(r1)
        session.add(r2)
        session.commit()
        session.close()
