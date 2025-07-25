# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: controller.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from isolate.connections.grpc.definitions import common_pb2 as common__pb2
from isolate.server.definitions import server_pb2 as server__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63ontroller.proto\x12\ncontroller\x1a\x0c\x63ommon.proto\x1a\x0cserver.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xde\x01\n\tHostedMap\x12,\n\x0c\x65nvironments\x18\x01 \x03(\x0b\x32\x16.EnvironmentDefinition\x12\x42\n\x14machine_requirements\x18\x02 \x01(\x0b\x32\x1f.controller.MachineRequirementsH\x00\x88\x01\x01\x12#\n\x08\x66unction\x18\x03 \x01(\x0b\x32\x11.SerializedObject\x12!\n\x06inputs\x18\x04 \x03(\x0b\x32\x11.SerializedObjectB\x17\n\x15_machine_requirements\"\xf6\x01\n\tHostedRun\x12,\n\x0c\x65nvironments\x18\x01 \x03(\x0b\x32\x16.EnvironmentDefinition\x12\x42\n\x14machine_requirements\x18\x02 \x01(\x0b\x32\x1f.controller.MachineRequirementsH\x00\x88\x01\x01\x12#\n\x08\x66unction\x18\x03 \x01(\x0b\x32\x11.SerializedObject\x12*\n\nsetup_func\x18\x04 \x01(\x0b\x32\x11.SerializedObjectH\x01\x88\x01\x01\x42\x17\n\x15_machine_requirementsB\r\n\x0b_setup_func\"\x88\x01\n\x14\x43reateUserKeyRequest\x12\x35\n\x05scope\x18\x01 \x01(\x0e\x32&.controller.CreateUserKeyRequest.Scope\x12\x12\n\x05\x61lias\x18\x02 \x01(\tH\x00\x88\x01\x01\"\x1b\n\x05Scope\x12\t\n\x05\x41\x44MIN\x10\x00\x12\x07\n\x03\x41PI\x10\x01\x42\x08\n\x06_alias\";\n\x15\x43reateUserKeyResponse\x12\x12\n\nkey_secret\x18\x01 \x01(\t\x12\x0e\n\x06key_id\x18\x02 \x01(\t\"\x15\n\x13ListUserKeysRequest\"B\n\x14ListUserKeysResponse\x12*\n\tuser_keys\x18\x01 \x03(\x0b\x32\x17.controller.UserKeyInfo\"&\n\x14RevokeUserKeyRequest\x12\x0e\n\x06key_id\x18\x01 \x01(\t\"\x17\n\x15RevokeUserKeyResponse\"\x93\x01\n\x0bUserKeyInfo\x12\x0e\n\x06key_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x35\n\x05scope\x18\x03 \x01(\x0e\x32&.controller.CreateUserKeyRequest.Scope\x12\r\n\x05\x61lias\x18\x04 \x01(\t\"\xb1\x01\n\x0fHostedRunResult\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\x30\n\x06status\x18\x02 \x01(\x0b\x32\x1b.controller.HostedRunStatusH\x00\x88\x01\x01\x12\x12\n\x04logs\x18\x03 \x03(\x0b\x32\x04.Log\x12,\n\x0creturn_value\x18\x04 \x01(\x0b\x32\x11.SerializedObjectH\x01\x88\x01\x01\x42\t\n\x07_statusB\x0f\n\r_return_value\"\x80\x01\n\x0fHostedRunStatus\x12\x30\n\x05state\x18\x01 \x01(\x0e\x32!.controller.HostedRunStatus.State\";\n\x05State\x12\x0f\n\x0bIN_PROGRESS\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x14\n\x10INTERNAL_FAILURE\x10\x02\"\xa5\x05\n\x13MachineRequirements\x12\x1d\n\x0cmachine_type\x18\x01 \x01(\tB\x02\x18\x01H\x00\x88\x01\x01\x12\x17\n\nkeep_alive\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x17\n\nbase_image\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x19\n\x0c\x65xposed_port\x18\x04 \x01(\x05H\x03\x88\x01\x01\x12\x16\n\tscheduler\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x37\n\x11scheduler_options\x18\x08 \x01(\x0b\x32\x17.google.protobuf.StructH\x05\x88\x01\x01\x12\x1d\n\x10max_multiplexing\x18\x06 \x01(\x05H\x06\x88\x01\x01\x12\x1c\n\x0fmax_concurrency\x18\t \x01(\x05H\x07\x88\x01\x01\x12\x1c\n\x0fmin_concurrency\x18\n \x01(\x05H\x08\x88\x01\x01\x12\x15\n\rmachine_types\x18\x0b \x03(\t\x12\x15\n\x08num_gpus\x18\x0c \x01(\x05H\t\x88\x01\x01\x12\x1c\n\x0frequest_timeout\x18\r \x01(\x05H\n\x88\x01\x01\x12\x1c\n\x0fstartup_timeout\x18\x0e \x01(\x05H\x0b\x88\x01\x01\x12\x1f\n\x12\x63oncurrency_buffer\x18\x0f \x01(\x05H\x0c\x88\x01\x01\x42\x0f\n\r_machine_typeB\r\n\x0b_keep_aliveB\r\n\x0b_base_imageB\x0f\n\r_exposed_portB\x0c\n\n_schedulerB\x14\n\x12_scheduler_optionsB\x13\n\x11_max_multiplexingB\x12\n\x10_max_concurrencyB\x12\n\x10_min_concurrencyB\x0b\n\t_num_gpusB\x12\n\x10_request_timeoutB\x12\n\x10_startup_timeoutB\x15\n\x13_concurrency_buffer\"\x99\x05\n\x1aRegisterApplicationRequest\x12,\n\x0c\x65nvironments\x18\x01 \x03(\x0b\x32\x16.EnvironmentDefinition\x12\x42\n\x14machine_requirements\x18\x02 \x01(\x0b\x32\x1f.controller.MachineRequirementsH\x00\x88\x01\x01\x12#\n\x08\x66unction\x18\x03 \x01(\x0b\x32\x11.SerializedObject\x12*\n\nsetup_func\x18\x04 \x01(\x0b\x32\x11.SerializedObjectH\x01\x88\x01\x01\x12\x1d\n\x10\x61pplication_name\x18\x05 \x01(\tH\x02\x88\x01\x01\x12\x37\n\tauth_mode\x18\x06 \x01(\x0e\x32\x1f.controller.ApplicationAuthModeH\x03\x88\x01\x01\x12 \n\x0fmax_concurrency\x18\x07 \x01(\x05\x42\x02\x18\x01H\x04\x88\x01\x01\x12.\n\x08metadata\x18\x08 \x01(\x0b\x32\x17.google.protobuf.StructH\x05\x88\x01\x01\x12@\n\x13\x64\x65ployment_strategy\x18\t \x01(\x0e\x32\x1e.controller.DeploymentStrategyH\x06\x88\x01\x01\x12\x12\n\x05scale\x18\n \x01(\x08H\x07\x88\x01\x01\x12\x19\n\x0cprivate_logs\x18\x0b \x01(\x08H\x08\x88\x01\x01\x42\x17\n\x15_machine_requirementsB\r\n\x0b_setup_funcB\x13\n\x11_application_nameB\x0c\n\n_auth_modeB\x12\n\x10_max_concurrencyB\x0b\n\t_metadataB\x16\n\x14_deployment_strategyB\x08\n\x06_scaleB\x0f\n\r_private_logs\"7\n\x1dRegisterApplicationResultType\x12\x16\n\x0e\x61pplication_id\x18\x01 \x01(\t\"z\n\x19RegisterApplicationResult\x12\x12\n\x04logs\x18\x01 \x03(\x0b\x32\x04.Log\x12>\n\x06result\x18\x02 \x01(\x0b\x32).controller.RegisterApplicationResultTypeH\x00\x88\x01\x01\x42\t\n\x07_result\"\xbe\x03\n\x18UpdateApplicationRequest\x12\x18\n\x10\x61pplication_name\x18\x01 \x01(\t\x12\x17\n\nkeep_alive\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x1d\n\x10max_multiplexing\x18\x03 \x01(\x05H\x01\x88\x01\x01\x12\x1c\n\x0fmax_concurrency\x18\x04 \x01(\x05H\x02\x88\x01\x01\x12\x1c\n\x0fmin_concurrency\x18\x05 \x01(\x05H\x03\x88\x01\x01\x12\x15\n\rvalid_regions\x18\x06 \x03(\t\x12\x15\n\rmachine_types\x18\x07 \x03(\t\x12\x1c\n\x0frequest_timeout\x18\x08 \x01(\x05H\x04\x88\x01\x01\x12\x1c\n\x0fstartup_timeout\x18\t \x01(\x05H\x05\x88\x01\x01\x12\x1f\n\x12\x63oncurrency_buffer\x18\n \x01(\x05H\x06\x88\x01\x01\x42\r\n\x0b_keep_aliveB\x13\n\x11_max_multiplexingB\x12\n\x10_max_concurrencyB\x12\n\x10_min_concurrencyB\x12\n\x10_request_timeoutB\x12\n\x10_startup_timeoutB\x15\n\x13_concurrency_buffer\"D\n\x17UpdateApplicationResult\x12)\n\nalias_info\x18\x01 \x01(\x0b\x32\x15.controller.AliasInfo\"M\n\x17ListApplicationsRequest\x12\x1d\n\x10\x61pplication_name\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x13\n\x11_application_name\"\x9b\x03\n\x0f\x41pplicationInfo\x12\x16\n\x0e\x61pplication_id\x18\x01 \x01(\t\x12\x17\n\x0fmax_concurrency\x18\x02 \x01(\x05\x12\x18\n\x10max_multiplexing\x18\x03 \x01(\x05\x12\x12\n\nkeep_alive\x18\x04 \x01(\x05\x12\x16\n\x0e\x61\x63tive_runners\x18\x06 \x01(\x05\x12\x17\n\x0fmin_concurrency\x18\x07 \x01(\x05\x12\x15\n\rmachine_types\x18\x08 \x03(\t\x12\x1c\n\x0frequest_timeout\x18\t \x01(\x05H\x00\x88\x01\x01\x12\x1c\n\x0fstartup_timeout\x18\n \x01(\x05H\x01\x88\x01\x01\x12\x15\n\rvalid_regions\x18\x0b \x03(\t\x12\x1f\n\x12\x63oncurrency_buffer\x18\x0c \x01(\x05H\x02\x88\x01\x01\x12.\n\ncreated_at\x18\r \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x12\n\x10_request_timeoutB\x12\n\x10_startup_timeoutB\x15\n\x13_concurrency_buffer\"K\n\x16ListApplicationsResult\x12\x31\n\x0c\x61pplications\x18\x01 \x03(\x0b\x32\x1b.controller.ApplicationInfo\"2\n\x18\x44\x65leteApplicationRequest\x12\x16\n\x0e\x61pplication_id\x18\x01 \x01(\t\"\x19\n\x17\x44\x65leteApplicationResult\"y\n\x0fSetAliasRequest\x12\r\n\x05\x61lias\x18\x01 \x01(\t\x12\x10\n\x08revision\x18\x02 \x01(\t\x12\x37\n\tauth_mode\x18\x03 \x01(\x0e\x32\x1f.controller.ApplicationAuthModeH\x00\x88\x01\x01\x42\x0c\n\n_auth_mode\";\n\x0eSetAliasResult\x12)\n\nalias_info\x18\x01 \x01(\x0b\x32\x15.controller.AliasInfo\"#\n\x12\x44\x65leteAliasRequest\x12\r\n\x05\x61lias\x18\x01 \x01(\t\"%\n\x11\x44\x65leteAliasResult\x12\x10\n\x08revision\x18\x01 \x01(\t\"\x14\n\x12ListAliasesRequest\";\n\x11ListAliasesResult\x12&\n\x07\x61liases\x18\x01 \x03(\x0b\x32\x15.controller.AliasInfo\"\xa2\x03\n\tAliasInfo\x12\r\n\x05\x61lias\x18\x01 \x01(\t\x12\x10\n\x08revision\x18\x02 \x01(\t\x12\x32\n\tauth_mode\x18\x03 \x01(\x0e\x32\x1f.controller.ApplicationAuthMode\x12\x17\n\x0fmax_concurrency\x18\x04 \x01(\x05\x12\x18\n\x10max_multiplexing\x18\x05 \x01(\x05\x12\x12\n\nkeep_alive\x18\x06 \x01(\x05\x12\x16\n\x0e\x61\x63tive_runners\x18\x07 \x01(\x05\x12\x17\n\x0fmin_concurrency\x18\x08 \x01(\x05\x12\x15\n\rmachine_types\x18\t \x03(\t\x12\x1c\n\x0frequest_timeout\x18\n \x01(\x05H\x00\x88\x01\x01\x12\x1c\n\x0fstartup_timeout\x18\x0b \x01(\x05H\x01\x88\x01\x01\x12\x15\n\rvalid_regions\x18\x0c \x03(\t\x12\x1f\n\x12\x63oncurrency_buffer\x18\r \x01(\x05H\x02\x88\x01\x01\x42\x12\n\x10_request_timeoutB\x12\n\x10_startup_timeoutB\x15\n\x13_concurrency_buffer\">\n\x10SetSecretRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\x05value\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_value\"\x13\n\x11SetSecretResponse\"\x14\n\x12ListSecretsRequest\"^\n\x06Secret\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x35\n\x0c\x63reated_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x88\x01\x01\x42\x0f\n\r_created_time\":\n\x13ListSecretsResponse\x12#\n\x07secrets\x18\x01 \x03(\x0b\x32\x12.controller.Secret\"(\n\x17ListAliasRunnersRequest\x12\r\n\x05\x61lias\x18\x01 \x01(\t\"C\n\x18ListAliasRunnersResponse\x12\'\n\x07runners\x18\x01 \x03(\x0b\x32\x16.controller.RunnerInfo\"\xf7\x01\n\nRunnerInfo\x12\x11\n\trunner_id\x18\x01 \x01(\t\x12\x1a\n\x12in_flight_requests\x18\x02 \x01(\x05\x12!\n\x14\x65xpiration_countdown\x18\x03 \x01(\x05H\x00\x88\x01\x01\x12\x0e\n\x06uptime\x18\x04 \x01(\x02\x12\x10\n\x08revision\x18\x06 \x01(\t\x12\r\n\x05\x61lias\x18\x07 \x01(\t\x12\x37\n\x11\x65xternal_metadata\x18\x05 \x01(\x0b\x32\x17.google.protobuf.StructH\x01\x88\x01\x01\x42\x17\n\x15_expiration_countdownB\x14\n\x12_external_metadata\"&\n\x11KillRunnerRequest\x12\x11\n\trunner_id\x18\x01 \x01(\t\"\x14\n\x12ListRunnersRequest\">\n\x13ListRunnersResponse\x12\'\n\x07runners\x18\x01 \x03(\x0b\x32\x16.controller.RunnerInfo\"\x14\n\x12KillRunnerResponse*:\n\x13\x41pplicationAuthMode\x12\x0b\n\x07PRIVATE\x10\x00\x12\n\n\x06PUBLIC\x10\x01\x12\n\n\x06SHARED\x10\x02*/\n\x12\x44\x65ploymentStrategy\x12\x0c\n\x08RECREATE\x10\x00\x12\x0b\n\x07ROLLING\x10\x01\x32\xaa\x0b\n\x11IsolateController\x12=\n\x03Run\x12\x15.controller.HostedRun\x1a\x1b.controller.HostedRunResult\"\x00\x30\x01\x12=\n\x03Map\x12\x15.controller.HostedMap\x1a\x1b.controller.HostedRunResult\"\x00\x30\x01\x12V\n\rCreateUserKey\x12 .controller.CreateUserKeyRequest\x1a!.controller.CreateUserKeyResponse\"\x00\x12S\n\x0cListUserKeys\x12\x1f.controller.ListUserKeysRequest\x1a .controller.ListUserKeysResponse\"\x00\x12V\n\rRevokeUserKey\x12 .controller.RevokeUserKeyRequest\x1a!.controller.RevokeUserKeyResponse\"\x00\x12h\n\x13RegisterApplication\x12&.controller.RegisterApplicationRequest\x1a%.controller.RegisterApplicationResult\"\x00\x30\x01\x12`\n\x11UpdateApplication\x12$.controller.UpdateApplicationRequest\x1a#.controller.UpdateApplicationResult\"\x00\x12]\n\x10ListApplications\x12#.controller.ListApplicationsRequest\x1a\".controller.ListApplicationsResult\"\x00\x12`\n\x11\x44\x65leteApplication\x12$.controller.DeleteApplicationRequest\x1a#.controller.DeleteApplicationResult\"\x00\x12\x45\n\x08SetAlias\x12\x1b.controller.SetAliasRequest\x1a\x1a.controller.SetAliasResult\"\x00\x12N\n\x0b\x44\x65leteAlias\x12\x1e.controller.DeleteAliasRequest\x1a\x1d.controller.DeleteAliasResult\"\x00\x12N\n\x0bListAliases\x12\x1e.controller.ListAliasesRequest\x1a\x1d.controller.ListAliasesResult\"\x00\x12J\n\tSetSecret\x12\x1c.controller.SetSecretRequest\x1a\x1d.controller.SetSecretResponse\"\x00\x12P\n\x0bListSecrets\x12\x1e.controller.ListSecretsRequest\x1a\x1f.controller.ListSecretsResponse\"\x00\x12_\n\x10ListAliasRunners\x12#.controller.ListAliasRunnersRequest\x1a$.controller.ListAliasRunnersResponse\"\x00\x12M\n\nKillRunner\x12\x1d.controller.KillRunnerRequest\x1a\x1e.controller.KillRunnerResponse\"\x00\x12P\n\x0bListRunners\x12\x1e.controller.ListRunnersRequest\x1a\x1f.controller.ListRunnersResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'controller_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MACHINEREQUIREMENTS'].fields_by_name['machine_type']._loaded_options = None
  _globals['_MACHINEREQUIREMENTS'].fields_by_name['machine_type']._serialized_options = b'\030\001'
  _globals['_REGISTERAPPLICATIONREQUEST'].fields_by_name['max_concurrency']._loaded_options = None
  _globals['_REGISTERAPPLICATIONREQUEST'].fields_by_name['max_concurrency']._serialized_options = b'\030\001'
  _globals['_APPLICATIONAUTHMODE']._serialized_start=5647
  _globals['_APPLICATIONAUTHMODE']._serialized_end=5705
  _globals['_DEPLOYMENTSTRATEGY']._serialized_start=5707
  _globals['_DEPLOYMENTSTRATEGY']._serialized_end=5754
  _globals['_HOSTEDMAP']._serialized_start=124
  _globals['_HOSTEDMAP']._serialized_end=346
  _globals['_HOSTEDRUN']._serialized_start=349
  _globals['_HOSTEDRUN']._serialized_end=595
  _globals['_CREATEUSERKEYREQUEST']._serialized_start=598
  _globals['_CREATEUSERKEYREQUEST']._serialized_end=734
  _globals['_CREATEUSERKEYREQUEST_SCOPE']._serialized_start=697
  _globals['_CREATEUSERKEYREQUEST_SCOPE']._serialized_end=724
  _globals['_CREATEUSERKEYRESPONSE']._serialized_start=736
  _globals['_CREATEUSERKEYRESPONSE']._serialized_end=795
  _globals['_LISTUSERKEYSREQUEST']._serialized_start=797
  _globals['_LISTUSERKEYSREQUEST']._serialized_end=818
  _globals['_LISTUSERKEYSRESPONSE']._serialized_start=820
  _globals['_LISTUSERKEYSRESPONSE']._serialized_end=886
  _globals['_REVOKEUSERKEYREQUEST']._serialized_start=888
  _globals['_REVOKEUSERKEYREQUEST']._serialized_end=926
  _globals['_REVOKEUSERKEYRESPONSE']._serialized_start=928
  _globals['_REVOKEUSERKEYRESPONSE']._serialized_end=951
  _globals['_USERKEYINFO']._serialized_start=954
  _globals['_USERKEYINFO']._serialized_end=1101
  _globals['_HOSTEDRUNRESULT']._serialized_start=1104
  _globals['_HOSTEDRUNRESULT']._serialized_end=1281
  _globals['_HOSTEDRUNSTATUS']._serialized_start=1284
  _globals['_HOSTEDRUNSTATUS']._serialized_end=1412
  _globals['_HOSTEDRUNSTATUS_STATE']._serialized_start=1353
  _globals['_HOSTEDRUNSTATUS_STATE']._serialized_end=1412
  _globals['_MACHINEREQUIREMENTS']._serialized_start=1415
  _globals['_MACHINEREQUIREMENTS']._serialized_end=2092
  _globals['_REGISTERAPPLICATIONREQUEST']._serialized_start=2095
  _globals['_REGISTERAPPLICATIONREQUEST']._serialized_end=2760
  _globals['_REGISTERAPPLICATIONRESULTTYPE']._serialized_start=2762
  _globals['_REGISTERAPPLICATIONRESULTTYPE']._serialized_end=2817
  _globals['_REGISTERAPPLICATIONRESULT']._serialized_start=2819
  _globals['_REGISTERAPPLICATIONRESULT']._serialized_end=2941
  _globals['_UPDATEAPPLICATIONREQUEST']._serialized_start=2944
  _globals['_UPDATEAPPLICATIONREQUEST']._serialized_end=3390
  _globals['_UPDATEAPPLICATIONRESULT']._serialized_start=3392
  _globals['_UPDATEAPPLICATIONRESULT']._serialized_end=3460
  _globals['_LISTAPPLICATIONSREQUEST']._serialized_start=3462
  _globals['_LISTAPPLICATIONSREQUEST']._serialized_end=3539
  _globals['_APPLICATIONINFO']._serialized_start=3542
  _globals['_APPLICATIONINFO']._serialized_end=3953
  _globals['_LISTAPPLICATIONSRESULT']._serialized_start=3955
  _globals['_LISTAPPLICATIONSRESULT']._serialized_end=4030
  _globals['_DELETEAPPLICATIONREQUEST']._serialized_start=4032
  _globals['_DELETEAPPLICATIONREQUEST']._serialized_end=4082
  _globals['_DELETEAPPLICATIONRESULT']._serialized_start=4084
  _globals['_DELETEAPPLICATIONRESULT']._serialized_end=4109
  _globals['_SETALIASREQUEST']._serialized_start=4111
  _globals['_SETALIASREQUEST']._serialized_end=4232
  _globals['_SETALIASRESULT']._serialized_start=4234
  _globals['_SETALIASRESULT']._serialized_end=4293
  _globals['_DELETEALIASREQUEST']._serialized_start=4295
  _globals['_DELETEALIASREQUEST']._serialized_end=4330
  _globals['_DELETEALIASRESULT']._serialized_start=4332
  _globals['_DELETEALIASRESULT']._serialized_end=4369
  _globals['_LISTALIASESREQUEST']._serialized_start=4371
  _globals['_LISTALIASESREQUEST']._serialized_end=4391
  _globals['_LISTALIASESRESULT']._serialized_start=4393
  _globals['_LISTALIASESRESULT']._serialized_end=4452
  _globals['_ALIASINFO']._serialized_start=4455
  _globals['_ALIASINFO']._serialized_end=4873
  _globals['_SETSECRETREQUEST']._serialized_start=4875
  _globals['_SETSECRETREQUEST']._serialized_end=4937
  _globals['_SETSECRETRESPONSE']._serialized_start=4939
  _globals['_SETSECRETRESPONSE']._serialized_end=4958
  _globals['_LISTSECRETSREQUEST']._serialized_start=4960
  _globals['_LISTSECRETSREQUEST']._serialized_end=4980
  _globals['_SECRET']._serialized_start=4982
  _globals['_SECRET']._serialized_end=5076
  _globals['_LISTSECRETSRESPONSE']._serialized_start=5078
  _globals['_LISTSECRETSRESPONSE']._serialized_end=5136
  _globals['_LISTALIASRUNNERSREQUEST']._serialized_start=5138
  _globals['_LISTALIASRUNNERSREQUEST']._serialized_end=5178
  _globals['_LISTALIASRUNNERSRESPONSE']._serialized_start=5180
  _globals['_LISTALIASRUNNERSRESPONSE']._serialized_end=5247
  _globals['_RUNNERINFO']._serialized_start=5250
  _globals['_RUNNERINFO']._serialized_end=5497
  _globals['_KILLRUNNERREQUEST']._serialized_start=5499
  _globals['_KILLRUNNERREQUEST']._serialized_end=5537
  _globals['_LISTRUNNERSREQUEST']._serialized_start=5539
  _globals['_LISTRUNNERSREQUEST']._serialized_end=5559
  _globals['_LISTRUNNERSRESPONSE']._serialized_start=5561
  _globals['_LISTRUNNERSRESPONSE']._serialized_end=5623
  _globals['_KILLRUNNERRESPONSE']._serialized_start=5625
  _globals['_KILLRUNNERRESPONSE']._serialized_end=5645
  _globals['_ISOLATECONTROLLER']._serialized_start=5757
  _globals['_ISOLATECONTROLLER']._serialized_end=7207
# @@protoc_insertion_point(module_scope)
