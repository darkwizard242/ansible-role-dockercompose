[![build-test](https://github.com/darkwizard242/ansible-role-dockercompose/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-dockercompose/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-dockercompose/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-dockercompose/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/47543?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/47543?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/47543?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-dockercompose&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-dockercompose) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-dockercompose&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-dockercompose) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-dockercompose&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-dockercompose) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-dockercompose&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-dockercompose) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-dockercompose?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-dockercompose?color=orange&style=flat-square)

# Ansible Role: dockercompose

Role to install (_by default_) [docker-compose](https://github.com/docker/compose/) on **Debian/Ubuntu** and **EL** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
dockercompose_app: docker-compose
dockercompose_version: 2.11.0
dockercompose_os: "linux"
dockercompose_arch: "x86_64"
dockercompose_dl_url: https://github.com/docker/compose/releases/download/v{{ dockercompose_version }}/{{ dockercompose_app }}-{{ dockercompose_os }}-{{ dockercompose_arch }}
dockercompose_bin_path: /usr/local/bin
dockercompose_file_owner: root
dockercompose_file_group: root
dockercompose_file_mode: '0755'
```

### Variables table:

Variable                | Description
----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------
dockercompose_app       | Defines the app to install i.e. **docker-compose**
dockercompose_version   | Defined to dynamically fetch the desired version to install. Defaults to: **2.11.0**
dockercompose_os        | Defines OS type. Used for obtaining the correct type of binaries based on OS. Defaults to: **linux**
dockercompose_arch      | Defines Architecture type. Used for obtaining the correct type of binaries based on Architecture. Defaults to: **x86_64**
dockercompose_dl_url    | Defines URL to download the docker-compose binary from.
dockercompose_bin_path  | Defined to dynamically set the appropriate path to store docker-compose binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**
dockercompose_owner     | Owner for the binary file of docker-compose.
dockercompose_group     | Group for the binary file of docker-compose.
dockercompose_file_mode | Mode for the binary file of docker-compose.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **dockercompose**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.dockercompose
```

For customizing behavior of role (i.e. specifying the desired **dockercompose** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.dockercompose
  vars:
    dockercompose_version: 1.26.0
```

For customizing behavior of role (i.e. placing binary of **dockercompose** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.dockercompose
  vars:
    dockercompose_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-dockercompose/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
