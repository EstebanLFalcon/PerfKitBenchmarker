# Copyright 2015 PerfKitBenchmarker Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Module containing flags applicable across benchmark run on AWS."""

from perfkitbenchmarker import flags

flags.DEFINE_string('aws_user_name', 'ubuntu',
                    'This determines the user name that Perfkit will '
                    'attempt to use. This must be changed in order to '
                    'use any image other than ubuntu.')
flags.DEFINE_integer('aws_provisioned_iops', None,
                     'IOPS for Provisioned IOPS (SSD) volumes in AWS.')

flags.DEFINE_string('aws_emr_loguri', None,
                    'The log-uri parameter to pass to AWS when creating a '
                    'cluster.  If not set, a bucket will be created.')
flags.DEFINE_integer('aws_emr_job_wait_time', None,
                     'The time to wait for an EMR job to finish, in seconds')

flags.DEFINE_string('s3_custom_endpoint', None,
                    'If given, a custom endpoint to use for S3 transfers. If '
                    'this flag is not given, use the standard endpoint for the '
                    'storage region.')
flags.DEFINE_boolean('aws_spot_instances', False,
                     'Whether to use AWS spot instances for any AWS VMs.')
flags.DEFINE_float('aws_spot_price', 0.0,
                   'The spot price to bid for AWS spot instances.')
flags.DEFINE_integer('aws_boot_disk_size', None,
                     'The boot disk size in GiB for AWS VMs.')
flags.DEFINE_string('kops', 'kops',
                    'The path to the kops binary.')
flags.DEFINE_string('edw_redshift_cluster_version', 'redshift-1.0',
                    'The redshift version to use for the cluster.')
flags.DEFINE_string('aws_image_name_filter', None,
                    'The filter to use when searching for an image for a VM.')
