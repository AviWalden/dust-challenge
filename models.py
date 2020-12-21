# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base, DeferredReflection
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

Base = declarative_base(cls=DeferredReflection)

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    create_date = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    last_modifed = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

class ProteinSequence(Base):
    __tablename__ = 'protein_sequences'

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    s3_key = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    last_modifed = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

    @hybrid_method
    def download(self, *, bucket, filename):
        import boto3
        boto3.resource("s3") \
            .Object(bucket_name=bucket, key=self.s3_key) \
            .download_file(filename)


class ProteinSubsequenceMatchStatus(Base):
    __tablename__ = 'protein_subsequence_match_status'

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('protein_subsequence_match_status_id_seq'::regclass)")
    )
    value = Column(Text)


class ProteinSubsequenceMatch(Base):
    __tablename__ = 'protein_subsequence_matches'

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    protein_sequence_id = Column(ForeignKey('protein_sequences.id'), server_default=text("uuid_nil()"), nullable=False)
    status_id = Column(ForeignKey('protein_subsequence_match_status.id'), nullable=False)
    author_id = Column(ForeignKey('users.id'), nullable=False)
    index = Column(Integer, nullable=False, server_default=text("'-1'::integer"))
    subsequence = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    last_modifed = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

    author = relationship('User')
    sequence = relationship('ProteinSequence')
    status = relationship('ProteinSubsequenceMatchStatus')
