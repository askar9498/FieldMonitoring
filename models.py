from sqlalchemy import Boolean, Column, ForeignKey, Integer, BigInteger, String, Float, JSON, text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base, engine
import psycopg2.extras


psycopg2.extras.register_uuid()


class Wells(Base):
    __tablename__ = "wells"
    well_id = Column(UUID(as_uuid=True),
                     primary_key=True,
                     server_default=text("gen_random_uuid()"), unique=True, index=True)
    #well_id = Column(BigInteger, Sequence('wells_well_id_seq', minvalue=-9223372036854775808, start=-9223372036854775808, increment=1), primary_key=True, autoincrement=True, unique=True, index=True)
    well_name = Column(String, index=True, nullable=False)
    country_id = Column(UUID(as_uuid=True), ForeignKey(
        "country.country_id", ondelete='CASCADE'), index=True, nullable=False)
    field_id = Column(UUID(as_uuid=True), ForeignKey(
        "fields.field_id", ondelete='CASCADE'), index=True, nullable=False)
    reservoir_id = Column(UUID(as_uuid=True), ForeignKey(
        "reservoirs.reservoir_id", ondelete='CASCADE'), index=True)
    zone = Column(String, index=True)
    status = Column(String, index=True)
    fluid = Column(String, index=True)
    production = Column(String, index=True)
    design_type = Column(String, index=True)
    designation = Column(String, index=True)
    depth_ref = Column(String, index=True)
    add_by = Column(String, index=True)
    approved_by = Column(String, index=True)
    add_datetime = Column(String, index=True)
    is_approved = Column(Boolean, index=True, default=False)
    lat_start = Column(Float, index=True)
    long_start = Column(Float, index=True)
    lat_end = Column(Float, index=True)
    long_end = Column(Float, index=True)
    activity_log = Column(String, index=True)
    tubulars = relationship("Tubular", backref='wells',
                            cascade="all, delete", passive_deletes=True)
    annuluses = relationship("Annulus", backref='wells',
                             cascade="all, delete", passive_deletes=True)
    survey = relationship("Survey", backref='wells',
                          cascade="all, delete", passive_deletes=True)
    pressureplot = relationship(
        "PressPlot", cascade="all, delete", passive_deletes=True)
    country = relationship("Country", backref='country')
    reservoir = relationship("Reservoirs", backref='reservoirs')
    field = relationship("Fields", backref='fields')


class Survey(Base):
    __tablename__ = "survey"
    item_id = Column(UUID(as_uuid=True),
                     primary_key=True,
                     server_default=text("gen_random_uuid()"), unique=True, index=True)
    #item_id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True, index=True)
    well_id = Column(UUID(as_uuid=True), ForeignKey(
        "wells.well_id", ondelete='CASCADE'))
    well_survey = Column(JSON)
    converted_survey = Column(JSON)
    #annotations = Column(JSON)
    add_by = Column(String, index=True)
    add_datetime = Column(DateTime, index=True)


class PressPlot(Base):
    __tablename__ = "pressplot"
    item_id = Column(UUID(as_uuid=True),
                     primary_key=True,
                     server_default=text("gen_random_uuid()"), unique=True, index=True)
    #item_id = Column(Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    well_id = Column(UUID(as_uuid=True), ForeignKey(
        "wells.well_id", ondelete='CASCADE'))
    press_p = Column(JSON)
    #pore_press = Column(JSON)
    #frac_press = Column(JSON)
    add_by = Column(String, index=True)
    add_datetime = Column(String, index=True)


class Tubular(Base):
    __tablename__ = "tubular"
    tube_id = Column(UUID(as_uuid=True),
                     primary_key=True,
                     server_default=text("gen_random_uuid()"), unique=True, index=True)
    #tube_id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True, index=True)
    well_id = Column(UUID(as_uuid=True), ForeignKey(
        "wells.well_id", ondelete='CASCADE'))
    tube_temp_id = Column(Integer, ForeignKey(
        "tubulartemp.tubulartemp_id"), index=True, nullable=False)
    conn_temp_id = Column(Integer, ForeignKey(
        "tubeconnection.connection_id"), index=True, nullable=False)
    tube_name = Column(String, index=True)
    hole_ID = Column(Float, index=True)
    tube_TVD_from = Column(Float, index=True)
    tube_MD_from = Column(Float, index=True)
    tube_TVD_to = Column(Float, index=True)
    tube_MD_to = Column(Float, index=True)
    cement_TOC = Column(Float, index=True)
    cement_return = Column(Float, index=True)
    cement_log = Column(Integer, index=True)
    formation_FIT = Column(Float, index=True)
    formation_LOT = Column(Float, index=True)
    formation_FBP = Column(Float, index=True)
    add_by = Column(String, index=True)
    add_datetime = Column(String, index=True)
    activity_log = Column(String, index=True)
    tube = relationship("TubularTemp", foreign_keys='Tubular.tube_temp_id')

    #tube = relationship("TubularTemp", backref='tubulartemp')
    connection = relationship("TubeConnection", backref="tubeconnection")
    #wells = relationship("Wells", back_populates="tubular", cascade=True)


class TubularTemp(Base):
    __tablename__ = "tubulartemp"
    # item_id = Column(UUID(as_uuid=True),
    # primary_key=True,
    # server_default=text("gen_random_uuid()"), unique=True, index=True)
    tubulartemp_id = Column(Integer, primary_key=True,
                            autoincrement=True, unique=True, index=True)
    tube_name = Column(String, index=True)
    tube_OD = Column(Float, index=True)  # inch
    tube_ID = Column(Float, index=True)  # inch
    tube_weight = Column(Float, index=True)  # ppf
    tube_grade = Column(String, index=True)
    tube_yield = Column(Float, index=True)  # psi
    tube_int_drift = Column(Float, index=True)  # inch
    tube_burst_press = Column(Float, index=True)  # psi
    tube_collapse_press = Column(Float, index=True)  # psi
    tube_axial = Column(Float, index=True)  # lbf
    tube_uts = Column(Float, index=True)  # psi
    add_by = Column(String, index=True)
    add_datetime = Column(String, index=True)


class TubeConnection(Base):
    __tablename__ = "tubeconnection"
    connection_id = Column(BigInteger, primary_key=True,
                           autoincrement=True, unique=True, index=True)
    tube_OD = Column(Float, index=True)
    tube_weight = Column(Float, index=True)
    tube_grade = Column(String, index=True)
    conn_name = Column(String, index=True)
    conn_type = Column(String, index=True, nullable=True)
    conn_seal_type = Column(String, index=True, nullable=True)
    conn_OD = Column(Float, index=True, nullable=True)
    conn_yield = Column(Float, index=True, nullable=True)
    conn_uts = Column(Float, index=True, nullable=True)
    conn_burst = Column(Float, index=True, nullable=True)
    conn_tension = Column(Float, index=True, nullable=True)
    conn_compression = Column(Float, index=True, nullable=True)
    conn_maxbend = Column(Float, index=True, nullable=True)
    add_by = Column(String, index=True, nullable=True)
    add_datetime = Column(String, index=True, nullable=True)


class Valves(Base):
    __tablename__ = "valves"
    valve_id = Column(UUID(as_uuid=True),
                      primary_key=True,
                      server_default=text("gen_random_uuid()"), unique=True, index=True)
    #valve_id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True, index=True)
    well_id = Column(UUID(as_uuid=True), ForeignKey(
        "wells.well_id", ondelete='CASCADE'))
    valve_name = Column(String, index=True)
    valve_manufacturer = Column(String, index=True)
    valve_partnumber = Column(String, index=True)
    valve_model = Column(String, index=True)
    valve_position = Column(String, index=True)
    valve_relative_position = Column(String, index=True)
    valve_actuation_type = Column(String, index=True)
    valve_size_nominal = Column(Float, index=True)
    valve_press_rating = Column(Float, index=True)
    valve_temp_rating = Column(Float, index=True)
    valve_class = Column(String, index=True)
    valve_bore_diameter = Column(Float, index=True)
    valve_bore_capacity = Column(Float, index=True)
    valve_open_turn = Column(Float, index=True)
    valve_close_turn = Column(Float, index=True)
    valve_stem_length = Column(Float, index=True)
    valve_opening_time = Column(Float, index=True)
    valve_closing_time = Column(Float, index=True)
    valve_safety_status = Column(String, index=True)
    barrier_envelope_category = Column(String, index=True)
    add_by = Column(String, index=True)
    add_datetime = Column(String, index=True)
    activity_log = Column(String, index=True)


class Country(Base):
    __tablename__ = "country"
    country_id = Column(UUID(as_uuid=True),
                        primary_key=True,
                        server_default=text("gen_random_uuid()"), unique=True, index=True)
    country_name = Column(String, index=True)
    #wells = relationship("Wells", backref='Country', passive_deletes=True, lazy='joined')
    fields = relationship("Fields", cascade="all, delete",
                          passive_deletes=True)


class Fields(Base):
    __tablename__ = "fields"
    field_id = Column(UUID(as_uuid=True),
                      primary_key=True,
                      server_default=text("gen_random_uuid()"), unique=True, index=True)
    country_id = Column(UUID(as_uuid=True), ForeignKey(
        "country.country_id", ondelete='CASCADE'))
    #field_id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True, index=True)
    #country_id = Column(Integer, ForeignKey("wells.well_id", ondelete='CASCADE'))
    field_name = Column(String, index=True)
    reservoirs = relationship(
        "Reservoirs", cascade="all, delete", passive_deletes=True)
    #wells = relationship("Wells", backref='Fields', passive_deletes=True, lazy='joined')


class Reservoirs(Base):
    __tablename__ = "reservoirs"
    reservoir_id = Column(UUID(as_uuid=True),
                          primary_key=True,
                          server_default=text("gen_random_uuid()"), unique=True, index=True)
    #res_id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True, index=True)
    field_id = Column(UUID(as_uuid=True), ForeignKey(
        "fields.field_id", ondelete='CASCADE'))
    #wells = relationship("Wells", backref='Reservoirs', passive_deletes=True, lazy='joined')
    reservoir_name = Column(String, index=True)


class ActLog(Base):
    __tablename__ = "actlog"
    act_id = Column(UUID(as_uuid=True),
                    primary_key=True,
                    server_default=text("gen_random_uuid()"), unique=True, index=True)
    #activity_id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True, index=True)
    user_name = Column(String, ForeignKey(
        "users.user_name"), index=True, nullable=False)
    well_id = Column(UUID(as_uuid=True), ForeignKey(
        "wells.well_id"), index=True, nullable=False)
    dt = Column(DateTime, index=True)
    message = Column(String, index=True)
    action_type = Column(String, index=True)
    well = relationship("Wells", backref='wells')
    user = relationship("Users", backref='users')


class Log(Base):
    __tablename__ = "log"
    log_id = Column(UUID(as_uuid=True),
                    primary_key=True,
                    server_default=text("gen_random_uuid()"), unique=True, index=True)
    #activity_id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True, index=True)
    well_name = Column(String(250))
    country_name = Column(String(250))
    field_name = Column(String(250))
    dt = Column(String(250))
    log_message = Column(String(1000))


class Annulus(Base):
    __tablename__ = "annulus"
    annulus_id = Column(UUID(as_uuid=True),
                        primary_key=True,
                        server_default=text("gen_random_uuid()"), unique=True, index=True)
    #annulus_id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True, index=True)
    well_id = Column(UUID(as_uuid=True), ForeignKey(
        "wells.well_id", ondelete='CASCADE'), index=True)
    annulus_designation = Column(String, index=True)
    annulus_name = Column(String, index=True)
    annulus_outer_tube_id = Column(UUID(as_uuid=True), ForeignKey(
        "tubular.tube_id", ondelete='CASCADE'), index=True)
    annulus_inner_tube_id = Column(UUID(as_uuid=True), ForeignKey(
        "tubular.tube_id", ondelete='CASCADE'), index=True)
    annulus_init_press = Column(Float, index=True)
    barrier_envelope_category = Column(String, index=True)
    add_by = Column(String, index=True)
    add_datetime = Column(String, index=True)
    activity_log = Column(String, index=True)

    tube_inner = relationship(
        "Tubular", foreign_keys='Annulus.annulus_inner_tube_id')
    tube_outer = relationship(
        "Tubular", foreign_keys='Annulus.annulus_outer_tube_id')


class Users(Base):
    __tablename__ = "users"
    user_id = Column(UUID(as_uuid=True),
                     primary_key=True,
                     server_default=text("gen_random_uuid()"), unique=True, index=True)
    #user_id = Column(BigInteger, primary_key=True, autoincrement=True, unique=True, index=True)
    user_name = Column(String, index=True, unique=True)
    password = Column(String, index=True)
    personnel_code = Column(String, index=True, unique=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    department = Column(String, index=True)
    is_active = Column(Boolean, index=True)
    authority = Column(String, index=True)


class PrivCat(Base):
    __tablename__ = "privcat"
    cat_id = Column(UUID(as_uuid=True),
                    primary_key=True,
                    server_default=text("gen_random_uuid()"), unique=True, index=True)
    cat_name = Column(String, index=True)
    read = Column(Boolean, index=True)
    write = Column(Boolean, index=True)
    delete = Column(Boolean, index=True)
    user_add = Column(Boolean, index=True)
    user_edit = Column(Boolean, index=True)
    user_delete = Column(Boolean, index=True)
    approve = Column(Boolean, index=True)


class BarElemTemp(Base):
    __tablename__ = "bar_elem_temp"
    item_id = Column(UUID(as_uuid=True),
                     primary_key=True,
                     server_default=text("gen_random_uuid()"), unique=True, index=True)
    element_name = Column(String, index=True)
    add_by = Column(String, index=True)
    add_datetime = Column(String, index=True)


class BarStandard(Base):
    __tablename__ = "bar_standard"
    item_id = Column(UUID(as_uuid=True),
                     primary_key=True,
                     server_default=text("gen_random_uuid()"), unique=True, index=True)
    standard_name = Column(String, index=True)
    standrd_version = Column(String, index=True)
    add_by = Column(String, index=True)
    add_datetime = Column(String, index=True)


class BarElemTempAcc(Base):
    __tablename__ = "bar_elem_temp_acc"
    item_id = Column(UUID(as_uuid=True),
                     primary_key=True,
                     server_default=text("gen_random_uuid()"), unique=True, index=True)
    elem_temp_id = Column(UUID(as_uuid=True), ForeignKey(
        "bar_elem_temp.item_id", ondelete='CASCADE'), index=True)
    standard_id = Column(UUID(as_uuid=True), ForeignKey(
        "bar_standard.item_id", ondelete='CASCADE'), index=True)
    feature = Column(String, index=True)
    acc_criteria = Column(JSON)
    stdr_name = Column(JSON)
    add_by = Column(String, index=True)
    add_datetime = Column(String, index=True)

    # Relationships defined here
    element_temp = relationship(
        "BarElemTemp", foreign_keys="BarElemTempAcc.elem_temp_id")
    standard = relationship(
        "BarStandard", foreign_keys="BarElemTempAcc.standard_id")
