import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_dockercompose_binary_exists(host):
    assert host.file('/usr/local/bin/docker-compose').exists


def test_dockercompose_binary_file(host):
    assert host.file('/usr/local/bin/docker-compose').is_file


def test_dockercompose_binary_which(host):
    assert host.check_output('which docker-compose') == \
      '/usr/local/bin/docker-compose'
