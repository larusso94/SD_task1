# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: methods.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='methods.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rmethods.proto\"^\n\x07message\x12\r\n\x05\x65rror\x18\x01 \x01(\x05\x12\x0c\n\x04node\x18\x02 \x01(\x05\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\x12\x0b\n\x03url\x18\x04 \x01(\t\x12\x0c\n\x04list\x18\x05 \x01(\t\x12\x0c\n\x04\x65num\x18\x06 \x01(\t24\n\x0cworkerCreate\x12$\n\x0cworkerCreate\x12\x08.message\x1a\x08.message\"\x00\x32\x34\n\x0cworkerDelete\x12$\n\x0cworkerDelete\x12\x08.message\x1a\x08.message\"\x00\x32\x32\n\x0blistWorkers\x12#\n\x0blistWorkers\x12\x08.message\x1a\x08.message\"\x00\x32\x30\n\ncountWords\x12\"\n\ncountWords\x12\x08.message\x1a\x08.message\"\x00\x32\x38\n\x0e\x65numerateWords\x12&\n\x0e\x65numerateWords\x12\x08.message\x1a\x08.message\"\x00\x62\x06proto3'
)




_MESSAGE = _descriptor.Descriptor(
  name='message',
  full_name='message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='message.error', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node', full_name='message.node', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count', full_name='message.count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='message.url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='list', full_name='message.list', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enum', full_name='message.enum', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=111,
)

DESCRIPTOR.message_types_by_name['message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

message = _reflection.GeneratedProtocolMessageType('message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'methods_pb2'
  # @@protoc_insertion_point(class_scope:message)
  })
_sym_db.RegisterMessage(message)



_WORKERCREATE = _descriptor.ServiceDescriptor(
  name='workerCreate',
  full_name='workerCreate',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=113,
  serialized_end=165,
  methods=[
  _descriptor.MethodDescriptor(
    name='workerCreate',
    full_name='workerCreate.workerCreate',
    index=0,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORKERCREATE)

DESCRIPTOR.services_by_name['workerCreate'] = _WORKERCREATE


_WORKERDELETE = _descriptor.ServiceDescriptor(
  name='workerDelete',
  full_name='workerDelete',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=167,
  serialized_end=219,
  methods=[
  _descriptor.MethodDescriptor(
    name='workerDelete',
    full_name='workerDelete.workerDelete',
    index=0,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORKERDELETE)

DESCRIPTOR.services_by_name['workerDelete'] = _WORKERDELETE


_LISTWORKERS = _descriptor.ServiceDescriptor(
  name='listWorkers',
  full_name='listWorkers',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=221,
  serialized_end=271,
  methods=[
  _descriptor.MethodDescriptor(
    name='listWorkers',
    full_name='listWorkers.listWorkers',
    index=0,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LISTWORKERS)

DESCRIPTOR.services_by_name['listWorkers'] = _LISTWORKERS


_COUNTWORDS = _descriptor.ServiceDescriptor(
  name='countWords',
  full_name='countWords',
  file=DESCRIPTOR,
  index=3,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=273,
  serialized_end=321,
  methods=[
  _descriptor.MethodDescriptor(
    name='countWords',
    full_name='countWords.countWords',
    index=0,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COUNTWORDS)

DESCRIPTOR.services_by_name['countWords'] = _COUNTWORDS


_ENUMERATEWORDS = _descriptor.ServiceDescriptor(
  name='enumerateWords',
  full_name='enumerateWords',
  file=DESCRIPTOR,
  index=4,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=323,
  serialized_end=379,
  methods=[
  _descriptor.MethodDescriptor(
    name='enumerateWords',
    full_name='enumerateWords.enumerateWords',
    index=0,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENUMERATEWORDS)

DESCRIPTOR.services_by_name['enumerateWords'] = _ENUMERATEWORDS

# @@protoc_insertion_point(module_scope)
