import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE_BINARY = "/usr/local/bin/docker-compose"


def test_dockercompose_binary_exists(host):
    """
    Tests if docker-compose binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_dockercompose_binary_file(host):
    """
    Tests if docker-compose binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_dockercompose_binary_which(host):
    """
    Tests the output to confirm docker-compose's binary location.
    """
    assert host.check_output('which docker-compose') == PACKAGE_BINARY
